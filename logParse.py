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

plt.close("all")
parser = argparse.ArgumentParser(description="V vs C viz script to visualize rslt channel")
parser.add_argument('-v', '--Vfile', help='RTL result file name', required=True, type=str)
parser.add_argument('-c', '--Cfile', help='C result file name', required=True, type=str)
args = parser.parse_args()

'''Vfile = '/home/vikram/FG/algLogs/fgAlgTrkrDscWithGocEn.log'
Cfile = '/home/vikram/FG/algLogs/jITech3AhDscRsltRnd.log'
'''

def parseV(nibble, posn):
    tempList = []
    binaryList = []
    with open(args.Vfile, mode='rt') as f:
        f.readline()
        for line in f:
            tempList.append(line.split()[11])
    for n in range(0, len(tempList)):
        val = "{0:04b}".format(int(tempList[n][nibble], 16))
        binaryList.append(val[posn])

    return binaryList
def parseC(flagCol):
    CbinList = []
    with open(args.Cfile, mode='rt') as cf:
        cf.readline()
        for line in cf:
            CbinList.append(line.split()[flagCol])
    for n in range(len(CbinList)):
        if CbinList[n] == 'false':
            CbinList[n] = 0
        else:
            CbinList[n] = 1
    return CbinList

def doPlot(figNum, listToPlot, label):
    plt.figure(figNum)
    plt.plot(listToPlot)
    plt.ylabel(label)
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

bSocDeltaBin = parseV(7, 2)
CbSocDelta = parseC(20) #for 2.0
'''doPlot(1, bSocDeltaBin, "VbSocDelta")
doPlot(2, CbSocDelta, "CbSocDelta")'''
do2Plot(1, bSocDeltaBin, "VbSocDelta", CbSocDelta, "CbSocDelta")
'''-------------'''
mSocDeltaBin = parseV(7, 1)
CmSocDelta = parseC(21) #for 2.0
'''doPlot(3, mSocDeltaBin, "VmSocDelta")
doPlot(4, CmSocDelta, "CmSocDelta")'''
do2Plot(2, mSocDeltaBin, "VmSocDelta", CmSocDelta, "CmSocDelta")
'''-------------'''
mSocLowBin = parseV(7, 0)
CmSocLow = parseC(17)
'''doPlot(5, mSocLowBin, "mSocLow")
doPlot(6, CmSocLow, "CmSocLow")'''
do2Plot(3, mSocLowBin, "mSocLowBin", CmSocLow, "CmSocLow")
'''-------------'''
mSocEmptyBin = parseV(6, 3)
CmSocEmpty = parseC(16)
'''doPlot(7, mSocEmptyBin, "mSocEmpty")
doPlot(8, CmSocEmpty, "CmSocEmpty")'''
do2Plot(4, mSocEmptyBin,"mSocEmptyBin", CmSocEmpty, "CmSocEmpty")
plt.show()
