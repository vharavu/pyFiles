__author__ = 'vikram'
import sys
import os
from os import listdir
from os.path import isfile, join
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines

plt.close("all")

file1 = '/home/vikram/FG/algLogs/fgAlgTrkrCrg.log'
#file1 = '/home/vikram/FG/algLogs/fgAlgTrkr.log' # with workaround
Cfile = '/home/vikram/FG/algLogs/jITech3AhCrgRsltRnd.log'
def parseV(nibble, posn):
    tempList = []
    binaryList = []
    with open(file1, mode='rt') as f:
        f.readline()
        for line in f:
            tempList.append(line.split()[11])
    for n in range(0, len(tempList)):
        val = "{0:04b}".format(int(tempList[n][nibble], 16))
        binaryList.append(val[posn])

    return binaryList
def parseC(flagCol):
    CbinList = []
    with open(Cfile, mode='rt') as cf:
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

bSocDeltaBin = parseV(7, 2)
CbSocDelta = parseC(19)
doPlot(1, bSocDeltaBin, "VbSocDelta")
doPlot(2, CbSocDelta, "CbSocDelta")
'''-------------'''
mSocDeltaBin = parseV(7, 1)
CmSocDelta = parseC(18)
doPlot(3, mSocDeltaBin, "VmSocDelta")
doPlot(4, CmSocDelta, "CmSocDelta")
'''-------------'''
mSocLowBin = parseV(7, 0)
CmSocLow = parseC(17)
'''doPlot(5, mSocLowBin, "mSocLow")
doPlot(6, CmSocLow, "CmSocLow")'''
'''-------------'''
mSocEmptyBin = parseV(6, 3)
CmSocEmpty = parseC(16)
'''doPlot(7, mSocEmptyBin, "mSocEmpty")
doPlot(8, CmSocEmpty, "CmSocEmpty")'''

plt.show()
