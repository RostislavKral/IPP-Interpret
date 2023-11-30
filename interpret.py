'''
    @Author: Rostislav Kral xkralr06
'''


import xml.etree.ElementTree as ET
import argparse as ag
import re
from synsem import *
import argparse
import os


parser = argparse.ArgumentParser(description="Interpret", add_help=False)
parser.add_argument('--source', help='File for input')
parser.add_argument('--input', help="STDIN input")
parser.add_argument('--help', action='store_true')
parser.add_argument('-h', action='store_true')
args = parser.parse_args()

#print(args.source or args.input)


## Check arguments

if (args.help or args.h) and (args.source or args.input):
   exit(10)

if(args.help or args.h):
    print("usage: interpret.py [-h] [--source SOURCE] [--input INPUT]Interpret \n optional arguments -h, --help\n  show this help message and exit --source SOURCE  File for input --input INPUT    STDIN input")
    exit(0)

if( args.source != None):
    if not os.path.isfile(args.source):
        exit(10)
        parser.error('XML file or input was not specified/valid!')

if(args.source == None):
    args.source = sys.stdin

if(args.source == None):
    exit(10)
try:
    tree = ET.parse(args.source)
    root = tree.getroot()
except:
    exit(10)
if(root.tag != 'program' or root.get('language') != 'IPPcode23'):
    exit(32)


instructions = []
labels = []
orders = []

i=0
rootList = list(root)
while( i < len(rootList)):
    if rootList[i].tag != "instruction":
        exit(32)
    opcode = rootList[i].attrib['opcode']
    try:
        order = int(rootList[i].attrib['order'])
    except:
        exit(32)
    
    if order in orders or order <= 0:
        exit(32)

    orders.append(order)
    children = list(rootList[i])
    args = []
    for child in children:
        splitArg = re.search(r'arg(1|2|3)$', child.tag)
        if splitArg == None:
            exit(32)
        splitArg = int(splitArg.group(0).split('arg')[1])
        
        args.append({"type": child.attrib['type'], "val": child.text, "order": splitArg})
    instructions.append({'name': opcode,"args":args, 'order': int(order)})
    i+=1




analyzer = Analyzer(instructions)

analyzer.escape_sequences()

analyzer.interpret() #interpretation
