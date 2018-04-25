# -*- coding: UTF-8 -*-
from datetime import datetime
from csv import DictReader
import getopt
import argparse
import sys

def txt_to_vw(loc_txt, loc_output, train=True):
  """
  Munges a TXT file (loc_txt) to a VW file (loc_output). Set "train"
  to False when munging a test set.
  """
  start = datetime.now()
  print("\nTurning %s into %s. Is_train_set? %s"%(loc_txt,loc_output,bool(train)))
  
  with open(loc_output,"w") as outfile, open(loc_txt) as infile:
    for e,l in enumerate(infile):
        
        line = l.split('\t')
        #Creating the features
        numerical_features = ""
        categorical_features = ""
        for idx, v in enumerate(line[1:]):
            if idx < 13 and is_number(v) and len(str(v)) > 0: #find nonempty numerical values
                numerical_features += " %s:%s" % (idx,v)
            elif len(str(v)) > 0: #nonempty categorical values
                categorical_features += " %s" % v
                
        #Creating the labels		  
        if train: #we care about labels
            if line[0] == "1":
                label = 1
            else:
                label = -1 #we set negative label to -1
            outfile.write( "%s |i%s |c%s" % (label,numerical_features,categorical_features) )
            
        else: #we dont care about labels
            outfile.write( "|i%s |c%s" % (numerical_features,categorical_features) )
        
	    # Reporting progress
        if e % 100000 == 0:
          print("%s\t%s"%(e, str(datetime.now() - start)))

    print("\n %s Task execution time:\n\t%s"%(e, str(datetime.now() - start)))

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
    txt_to_vw( args.input, args.output, args.train)

if __name__ == "__main__":
    TRAIN = True
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help="Input File", required=True)
    parser.add_argument('-o', '--output', type=str, help="Output File", required=True)
    parser.add_argument('-t', '--train', type=str2bool, nargs='?', const=True, default=TRAIN, help="Training? (Default: yes)")
    args = parser.parse_args()
    main(args)

#txt_to_vw("/data/vw/criteo-display-advertising-dataset/train.txt", "criteo/click.train.vw",train=True)
#txt_to_vw("/data/vw/criteo-display-advertising-dataset/test.txt", "criteo/click.test.vw",train=False)