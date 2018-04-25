# -*- coding: UTF-8 -*-
from datetime import datetime
import argparse
import sys
import os

"""
Munges a collection of TXT files from a path into a single VW file (loc_output). 
Set "TRAIN" to False when munging a test set (can be done with -t cli flag).
"""

TRAIN = True
PATH = 'netflix/train_small'
OUT = 'netflix.train.vw'

def netflix_train(loc_txt, loc_output):
    """
    loc_text should point to a folder containing a collection of text files.
    Each text file should contain all ratings for a single movie. 
    
    First line contains the movie ID. subsequent line format: userid,score,date

    Example for movie id 20, mv_0000020.txt:

    20:
    2625420,2,2004-06-03
    1508073,3,2004-12-02
    1371016,3,2005-05-26
    ...

    Sample output (we're not interested in the date for now):

    2 |u 2625420 |i 20
    3 |u 1508073 |i 20
    3 |u 1371016 |i 20
    ...


    """
    start = datetime.now()
    print("\nTurning %s into %s. Training Set"%(loc_txt,loc_output))

    with open(loc_output,"w") as outfile:
        tot = 0    
        #for each file
        for filename in os.listdir(loc_txt):
            with open(loc_txt +'/'+ filename,'r') as infile:
                #get movie m_id from first line
                m_id = infile.readline()[:-2]
                for l in infile:
                    #write each line to file in vw format
                    row = l.split(',')
                    outfile.write("%s |u %s |i %s" % (row[1],row[0],m_id))
    	            # Reporting progress
                    tot += 1

                    if tot % 1000000 == 0:
                        print("%s\t%s"%(tot, str(datetime.now() - start)))

        print("\n %s Task execution time:\n\t%s"%(tot, str(datetime.now() - start)))

def netflix_test(loc_txt, loc_output):
    """
    Convert single validation file into VW format
    """
    start = datetime.now()
    print("\nTurning %s into %s. Validation Set"%(loc_txt,loc_output))

    with open(loc_output,"w") as outfile, open(loc_txt,"r") as infile:
        m_id = ''
        for idx,l in enumerate(infile):
            #get movie id
            
            if(l[-2] == ':'):
                m_id = l[:-2]
            else:
                row = l.split(',')
                outfile.write("|u %s |i %s\n" % (row[0],m_id))
            # Reporting progress

            if idx % 500000 == 0:
                print("%s\t%s"%(idx, str(datetime.now() - start)))

        print("\n %s Task execution time:\n\t%s"%(idx, str(datetime.now() - start)))
                    
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main(args):

    if(args.train):
        netflix_train( args.input, args.output)
    else:
        netflix_test(args.input, args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help="Input Folder", default=PATH)
    parser.add_argument('-o', '--output', type=str, help="Output File", default=OUT)
    parser.add_argument('-t', '--train', type=str2bool, nargs='?', const=True, default=TRAIN, help="Training? (Default: yes)")
    args = parser.parse_args()
    main(args)