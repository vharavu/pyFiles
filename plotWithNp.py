# -*- coding: utf-8 -*-
"""
@author: vharavu
"""

import sys
import os
from os import listdir
from os.path import isfile, join
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines

plt.close("all")

current = []
voltage = []
soc = []
vOcv = []

file1 = '../../log/smplLogs/cITech3Ah.txt'
file2 = '../../log/smplLogs/jITech3Ah.txt'

with open(file2, mode='rt') as f:
    f.readline()
    for line in f:
        current.append(line.split()[13])
        voltage.append(line.split()[12])
        soc.append(line.split()[1])
        vOcv.append(line.split()[8])
#voltage.remove('vBt')
#current.remove('iBt')
#soc.remove('soc')
#vOcv.remove('vOcv')

plt.figure(1)
plt.subplot(411)
plt.plot(voltage, ':')
plt.ylabel("vBt")

plt.subplot(412)
plt.plot(current)
plt.axis([0, 2500, -2.1, 0.6])
plt.ylabel("iBt")

plt.subplot(413)
plt.plot(soc, '--')
plt.ylabel("SoC")

plt.subplot(414)
plt.plot(vOcv)
plt.ylabel("vOcv")

plt.show()
