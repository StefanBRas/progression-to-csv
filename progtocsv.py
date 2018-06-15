#!/usr/bin/env python3

import base64
import json
import argparse
import csv
import sys


STANDARD = ["startTime","name","weight","reps"]


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("backup_file",type = str, help="Location of .progressionbackupfile")
    parser.add_argument("-c","--command",type = str, help="command (full or standard)")
    parser.add_argument("-o","--output",type = str, help="Location of output")
    return parser.parse_args(args)

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
            try:
                sets_target_note = sets_target["note"]
            except KeyError:
                 sets_target_note = ""
            sets_targe_restPerSet = sets_target["restPerSet"]
            sets_targe_groupindex = sets_target["groupIndex"]
            sets_target = sets_target["parameters"]
            for target_set in sets_target:
                target_set["note"]= sets_target_note
                target_set["restPerset"] = sets_targe_restPerSet 
                target_set["groupIndex"] = sets_targe_groupindex 
                keys = [key for key in target_set.keys()]
                for key in keys:
                    new_key = "_".join([key,"target"])
                    target_set[new_key] = target_set.pop(key)                
            for _set,target_set in zip(sets,sets_target):
                new_set = {**workout,**lift,**_set,**target_set}
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


def export_to_csv(sets,output,attributes = None):
    if attributes is None:
        attributes = sets[0].keys()
    else:
        new_sets = []
        for _set in sets:
            new_sets.append({x:_set[x] for x in attributes if x in _set})
            sets = new_sets
    if output:
        with open(output,"w") as f:
            writer = csv.DictWriter(f,attributes)
            writer.writeheader()
            writer.writerows(sets)
    else:
        writer = csv.DictWriter(sys.stdout,attributes)
        writer.writeheader()
        writer.writerows(sets)
        

def main(args):
    sets = get_sets(args.backup_file)
    if args.command == "full":
        export_to_csv(sets,args.output)
    else:
        export_to_csv(sets,args.output,STANDARD)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args)    
        
        