__author__ = 'vikram'
import sys
import os
import argparse
from os import listdir
from os.path import isfile, join
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines
import pandas as pd

parser = argparse.ArgumentParser(description="V vs C viz script to visualize SoC and other results")
parser.add_argument('-v', '--Vfile', help='RTL result file name', required=True, type=str)
parser.add_argument('-c', '--Cfile', help='C result file name', required=True, type=str)
args = parser.parse_args()

print args.Vfile, args.Cfile

def do2Plot(figNum, vArray, vLabel, cArray, cLabel):
    """

    :rtype : no return value.
    """
    plt.figure(figNum)
    ax1 = plt.subplot(211)
    ax1.plot(vArray)
    plt.ylabel(vLabel)

    ax2 = plt.subplot(212, sharex=ax1, sharey=ax1)
    ax2.plot(cArray)
    plt.ylabel(cLabel)
    plt.xlabel("FG cycle")


def parseAndBuild(fileString, posn):
    """

    :rtype : List
    """
    retArray = []
    with open(fileString, mode='rt') as vf:
        vf.readline()
        for line in vf:
            retArray.append(line.split()[posn])
    return retArray


plt.close("all")
Cdf = pd.read_table(args.Cfile, delim_whitespace=True)
Vdf = pd.read_table(args.Vfile, delim_whitespace=True)

VsocLiteMon = parseAndBuild(args.Vfile, 4)
CsocLiteMon = parseAndBuild(args.Cfile, 4)
do2Plot(1, VsocLiteMon, "VsocLiteMon", CsocLiteMon, "CsocLiteMon")
#do2Plot(5, Vdf.socLiteMon, "VsocLiteMon", Cdf.socLiteMon, "CsocLiteMon")

Vesr = parseAndBuild(args.Vfile, 3)
Cesr = parseAndBuild(args.Cfile, 3)
do2Plot(2, Vesr, "Vesr", Cesr, "Cesr")

do2Plot(3, parseAndBuild(args.Vfile, 2), "VvBt16", parseAndBuild(args.Cfile, 2), "CvBt16")
do2Plot(4, parseAndBuild(args.Vfile, 1), "ViBt16", parseAndBuild(args.Cfile, 1), "CiBt16")

plt.show()
#print Vdf.socLiteMon
#print Cdf.socLiteMon