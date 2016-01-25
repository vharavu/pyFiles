# -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:37:50 2015

@author: jblackma
"""

import sys, os
""", xlrd <-- what is this xlrd??
"""
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines
import numpy as np
"""unused import csv
import pickle
import itertools
import math
"""

plt.close("all")

current = []
voltage = []
soc = []

f = open('../../log/smplLogs/cITech3Ah.txt','r')
for line in f:
    if line[0] != '#':
        current.append(line.split()[13])
        voltage.append(line.split()[12])
        soc.append(line.split()[1])

###print(current)
voltage.pop(0) ## remove the heading "vBt"
current.pop(0) ## remove the heading "iBt"
soc.pop(0)
###print(voltage)

plt.figure(1)
plt.plot(voltage)
plt.title("voltage")

plt.figure(2)
plt.plot(current)
plt.title("current")

plt.figure(3)
plt.plot(soc)
plt.title("SoC")

plt.show()

