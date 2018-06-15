#!/usr/bin/env python3

import base64
import json
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("-b","--backup_file_location")
parser.add_argument("-c","--command")
parser.add_argument("-o","--output",type = string, help="Location of output")
args = parser.parse_args()
backup_file = args.backup_file_location

STANDARD = ["startTime","name","weight","reps"]

def get_sets(backup_file):
    all_sets = []
    with open(backup_file,"r") as f:
        file_content = f.read()
    content = base64.b64decode(file_content)
    content = content.decode("UTF-8")
    content = json.loads(content)
    workouts = json.loads(content["fws.json"])
    for workout in workouts:
        full_dict = workout
        activities = workout.pop("activities")
        for lift in activities:
            sets = lift.pop("performance")
            sets = sets["completedSets"]
            sets_target = lift.pop("performanceTarget")
    #        print(sets_target.keys())
  #          sets_target = sets_target["parameters"]
   #         print(sets_target[0].keys())
     #       for target_set in sets_target:
      #          keys = [key for key in target_set.keys()]
       #         for key in keys:
        #            new_key = "_".join([key,"target"])
         #           target_set[new_key] = target_set.pop(key)
#            for _set,target_set in zip(sets,sets_target):
#                new_set = {**workout,**lift,**_set,**target_set}
#                all_sets.append(new_set)
            for _set in sets:
                new_set = {**workout,**lift,**_set}
                all_sets.append(new_set)
    return(all_sets)
def get_program(backup_file):
    with open(backup_file,"r") as f:
        file_content = f.read()
    content = base64.b64decode(file_content)
    content = content.decode("UTF-8")
    content = json.loads(content)
    program = json.loads(content["up.json"])
    return(program)


def export_to_csv(sets,file,attributes = None):

	if attributes is None:
		attributes = sets[0].keys()
	else:
		new_sets = []
		for _set in sets:
			new_sets.append({x:_set[x] for x in attributes if x in _set})
		sets = new_sets
	with open(file,"w") as f:
		writer = csv.DictWriter(f,attributes)
		writer.writeheader()
		writer.writerows(sets)

def show_attributes():
    pass
if __name__ == "__main__":
    sets = get_sets(args.backup_file_location)
    if args.command = "standard":
        export_to_csv(sets,args.backup_file_location,STANDARD)
    if args.command = "full"
        export_to_csv(sets,args.backup_file_location)
        