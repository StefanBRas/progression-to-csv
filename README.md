# progression-to-csv
Python script to exports training data from .progressionbackup files created by the Progression app for Android to csv files.

It creates a csv file where each row is one set.

Feel free to use the issue-tracker to request features or report bugs.

I have only tested it on my own data, so it's (very possible) that there are somethings it doesn't handle well.

## "Installation"
1. Clone/download this repo
2. Run progtocsv.py with python3

## Data format

There are two formats included:

### STANDARD

A csv-file where each row is a set with the attributes:

1. **startTime** - Time of the start of the workout in the unix time
2. **name** - Name of the exercise
3. **weight** - Weight (I think it uses the metric from you phone) - BW if bodyweight.
4. **reps** - Amount of repetitions if applicable
5. **duration** - Duration, if timed set,0 if not (i think)

### FULL

A csv-file with where each row is a set with all attributes from the fil

## Uses
1. standard - save all workouts to a specified location with a subset of attributes

```bash
python3 progtocsv.py <backup file location> -c standard -o <.csv location>
```

2. full - save all workouts to a specified location with a subset of attributes

```bash
python3 progtocsv.py <backup file location> -c full -o <.csv location>
```
3. omit -o to print to stdout:

```bash
python3 progtocsv.py <backup file location> -c full
```

Omitting the "-c" flag will default til standard.

## Other
The test doesn't actually test that the output is correct, just that running the main function doesn't throw errors.

