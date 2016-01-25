__author__ = 'vikram'
import sys
import os
from os import listdir
from os.path import isfile, join
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines

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

Vfile = '/home/vikram/FG/algLogs/fgAlgTrkrDis.log'
Cfile = '/home/vikram/FG/algLogs/jITech3AhDscRsltRnd.log'

VsocLiteMon = parseAndBuild(Vfile, 4)
CsocLiteMon = parseAndBuild(Cfile, 4)
do2Plot(1, VsocLiteMon, "VsocLiteMon", CsocLiteMon, "CsocLiteMon")

Vesr = parseAndBuild(Vfile, 3)
Cesr = parseAndBuild(Cfile, 3)
do2Plot(2, Vesr, "Vesr", Cesr, "Cesr")
plt.show()
