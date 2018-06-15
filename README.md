# progression-to-csv
Python script exports training data from .progressionbackup files to csv

## "Installation"
1. Clone/download this repo
2. Run progression-to-csv.py with python3
## Data format.
There are two standard formats included, but you can specify what attributes you want:

### STANDARD

A csv-file with where each row is a set with the attributes:

1. **startTime** - Time of the start of the workout in the unix time
2. **name** - Name of the exercise
3. **weight** - Weight (I think it uses the metric from you phone) - BW if bodyweight.
4. **reps** - Amount of repetitions if applicable
(TODO: include time for things like plan)

### FULL

A csv-file with where each row is a set with the attributes:

(pending, the list is long)

(Also, not showing target weights yet)
### CUSTOM
Choose exactly what attributes to include
(not yet implemented)
## Uses
1. standard - save all workouts to a specified location with a subset of attributes

```bash
python3 progression-to-csv.py <backup file location> -c standard -o <.csv location>
```

2. full - save all workouts to a specified location with a subset of attributes

```bash
python3 progression-to-csv.py <backup file location> -c full -o <.csv location>
```

## TODOS
1. Add stuff
2. List dependencies
3. Tests