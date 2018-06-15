# progression-to-csv
Python script that adds csv export to [progression-app-perl](https://github.com/bartman/progression-app-perl) by bartman.

This is really just a wrapper for his script so all credit goes to him.

## "Installation"
1. Go to the link above and clone the repo (or just download "weightxreps.pl")
2. Clone/download this repo
3. Put them in the same folder.
4. Run progression-to-csv.py with python3
## Data format.

It saves to a single specified file where each row is one set. The headers are:
1. **Workout_date** - Date of workout in the format "YYYY/MM/DD"
2. **Workout_time** - Time of the start of the workout in the format "HH:MM:SS"
3. **Workout_duration** - Duration of workout in hours,
4. **Workout_name** - Name of the workout or *"<improvised>"* if none is given.
5. **exercise** - Name of the exercise
6. **weight** - Weight (I think it uses the metric from you phone) - BW if bodyweight.
7. **reps** - Amount of repetitions if applicable
8. **time** - Time in seconds of each set if applicable (e.g. planks)
9. **comment** - Comment given to the set (prefixed by two spaces af of now)

## Uses
1. save_all - save all workouts to a specified location

```bash
python3 progression-to-csv.py <backup file location> save_all
```

2. save_workout - save a single workout

```bash
python3 progression-to-csv.py <backup file location> save_workout -i <index of workout> 
```

3. show_all - show a summary of all workouts


```bash
python3 progression-to-csv.py <backup file location> show_all
```

## TODOS
1. Expand explanation
1. List dependencies
2. Tests
3. Add stuff