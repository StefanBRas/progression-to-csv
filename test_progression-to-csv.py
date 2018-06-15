import pytest
from progtocsv import get_sets,export_to_csv,main,parse_args

def test_argparse():
    parser = parse_args(["test"])
    assert parser.backup_file == "test"
def test_full_output_file():
    parser = parse_args(["test.progressionbackup","-c","full","-o","test.csv"])
    main(parser)
def test_full_output_stdout():
    parser = parse_args(["test.progressionbackup","-c","full"])
    main(parser)
def test_standard_output_stdout():
    parser = parse_args(["test.progressionbackup","-c","standard","-o","test.csv"])
    main(parser)
def test_standard_output_stdout():
    parser = parse_args(["test.progressionbackup","-c","standard"])
    main(parser)