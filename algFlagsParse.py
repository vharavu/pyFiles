__author__ = 'vikram'
import sys
import os
from os import listdir
from os.path import isfile, join
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines
import argparse
import pandas as pd

plt.close("all")
parser = argparse.ArgumentParser(description="V vs C viz script to visualize rslt channel")
parser.add_argument('-v', '--Vfile', help='RTL result file name', required=True, type=str)
parser.add_argument('-c', '--Cfile', help='C result file name', required=True, type=str)
args = parser.parse_args()

def parseV(nibble, posn):
    tempList = []
    binaryList = []
    with open(args.Vfile, mode='rt') as f:
        f.readline()
        for line in f:
            tempList.append(line.split()[11])
            #templist will contain the 'nibble+1'th nibble in algFlags col
    for n in range(0, len(tempList)):
        val = "{0:04b}".format(int(tempList[n][nibble], 16))
        #val is the string "0101" if the nibble is 0x5
        binaryList.append(val[posn])
        #posn should be the position counting from left to right of the nibble; dont confuse with lsb/msb notation
    return binaryList

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

df = pd.read_table(args.Cfile, delim_whitespace=True)

bSocDeltaBin = parseV(7, 2)
do2Plot(1, bSocDeltaBin, "VbSocDelta", df.bSocDelta, "CbSocDelta")
mSocDeltaBin = parseV(7, 1)
do2Plot(2, mSocDeltaBin, "VmSocDelta", df.mSocDelta, "CmSocDelta")
VmSocLow = parseV(7, 0)
do2Plot(3, VmSocLow, "VmSocLow", df.mSocLow, "CmSocLow")
VmSocEmpty = parseV(6, 3)
do2Plot(4, VmSocEmpty, "VmSocEmpty", df.mSocEmpty, "CmSocEmpty")

VmSocHigh = parseV(6, 2)
do2Plot(5, VmSocHigh, "VmSocHigh", df.mSocHigh, "CmSocHigh")
VmSocFull = parseV(6, 1)
do2Plot(6, VmSocFull, "VmSocFull", df.mSocFull, "CmSocFull")

VmSocLTOtgThr = parseV(6, 0)
do2Plot(7, VmSocLTOtgThr, "VmSocLTOtgThr", df.mSocLTOtgThr, "CmSocLTOtgThr")
VmSocLTCrgReThr = parseV(5, 3)
do2Plot(8, VmSocLTCrgReThr, "VmSocLTCrgReThr", df.mSocLTCrgReThr, "CmSocLTCrgReThr")

ViBtLTCrgTrm0Thr = parseV(5, 2)
do2Plot(9, ViBtLTCrgTrm0Thr, "ViBtLTCrgTrm0Thr", df.iBtLTCrgTrm0Th, "CiBtLTCrgTrm0Thr")

plt.show()
