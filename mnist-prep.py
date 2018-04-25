# -*- coding: UTF-8 -*-
from datetime import datetime
import argparse
import sys
import os

"""
Converts the mnist-8m dataset to VW format
"""

TRAIN = True
PATH = 'mnist/mnist8m-head'
OUT = 'mnist/mnist.train.vw'

def mnist_to_vw(loc_txt, loc_output, train):
    start = datetime.now()
    print("\nTurning %s into %s. Training Set"%(loc_txt,loc_output))
    with open(loc_output,"w") as outfile, open(loc_txt) as infile:
        for e,l in enumerate(infile):
            if train:
                outfile.write(" | ".join(l.split(" ", 1)))
            else: #ignore labels
                outfile.write("| " + l[2:])
        # Reporting progress
        if e % 100000 == 0:
          print("%s\t%s"%(e, str(datetime.now() - start)))

    print("\n %s Task execution time:\n\t%s"%(e, str(datetime.now() - start)))


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main(args):
    mnist_to_vw(args.input, args.output, args.train)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help="Input Folder", default=PATH)
    parser.add_argument('-o', '--output', type=str, help="Output File", default=OUT)
    parser.add_argument('-t', '--train', type=str2bool, nargs='?', const=True, default=TRAIN, help="Training? (Default: yes)")
    args = parser.parse_args()
    main(args)