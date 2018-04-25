# -*- coding: UTF-8 -*-
from datetime import datetime
from csv import DictReader
import getopt
import argparse
import sys

TRAIN = True
PATH = 'netflix/train_small'

def netflix_to_vw(loc_txt, loc_output, train):
    """
    Munges a collection of TXT files from a path into a single VW file (loc_output). 
    Set "TRAIN" to False when munging a test set (can be done with -t cli flag).

    loc_text should point to a folder containing a collection of text files.
    Each text file should contain all ratings for a single movie. 
    
    First line contains the movie ID. 

    Each rating contains 3 columns: userid:score:date

    Example for movie id 20:

    20:
    2625420,2,2004-06-03
    1508073,3,2004-12-02
    1371016,3,2005-05-26
    1374336,4,2004-09-26
    1254903,3,2005-06-15
    ...

    """
    start = datetime.now()
    print("\nTurning %s into %s. Is_train_set? %s"%(loc_txt,loc_output,bool(train)))

    """
    TODO: Process
    """

    with open(loc_output,"w") as outfile:
        1+1


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main(args):
    netflix_to_vw( args.input, args.output, args.train)

if __name__ == "__main__":
    TRAIN = True
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help="Input File", required=True)
    parser.add_argument('-o', '--output', type=str, help="Output File", required=True)
    parser.add_argument('-t', '--train', type=str2bool, nargs='?', const=True, default=TRAIN, help="Training? (Default: yes)")
    args = parser.parse_args()
    main(args)