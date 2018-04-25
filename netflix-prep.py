# -*- coding: UTF-8 -*-
from datetime import datetime
from csv import DictReader
import getopt
import argparse
import sys

def netflix_to_vw(loc_txt, loc_output, train=True):
    """
    Munges a TXT file (loc_txt) to a VW file (loc_output). Set "train"
    to False when munging a test set.
    """
    start = datetime.now()
    print("\nTurning %s into %s. Is_train_set? %s"%(loc_txt,loc_output,bool(train)))

    """
    TODO: Process
    """


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