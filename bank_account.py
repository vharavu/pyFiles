bank_account.pyc                                                                                    0000664 0001750 0001750 00000003167 12603320762 013600  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 �
�Vc           @   s   d  Z  d d d �  �  YZ d S(   t   vikramt   BankAccountc           B   sA   e  Z d  d � Z d �  Z d �  Z d �  Z d �  Z d �  Z RS(   i    c         C   s   | |  _  d GH|  j �  d S(   s    open an accts   Account openedN(   t   balancet   print_balance(   t   selfR   (    (    s'   /home/vikram/FG/plot/py/bank_account.pyt   __init__   s    	c         C   s+   |  j  | 7_  d j | � GH|  j �  d S(   s    deposit some moneys   ${} deposited.N(   R   t   formatR   (   R   t   amount(    (    s'   /home/vikram/FG/plot/py/bank_account.pyt   deposit
   s    c         C   s+   |  j  | 8_  d j | � GH|  j �  d  S(   Ns   ${} withdrawn.(   R   R   R   (   R   R   (    (    s'   /home/vikram/FG/plot/py/bank_account.pyt   withdraw   s    c         C   s   d j  |  j � GHd  S(   Ns   Account balance is ${}.(   R   R   (   R   (    (    s'   /home/vikram/FG/plot/py/bank_account.pyR      s    c         C   s   d j  |  j � S(   Ns   !!Account with balance of ${}(   R   R   (   R   (    (    s'   /home/vikram/FG/plot/py/bank_account.pyt   __str__   s    c         C   s   d j  |  j � S(   Ns   BankAccount(balance={})(   R   R   (   R   (    (    s'   /home/vikram/FG/plot/py/bank_account.pyt   __repr__   s    (   t   __name__t
   __module__R   R   R	   R   R
   R   (    (    (    s'   /home/vikram/FG/plot/py/bank_account.pyR      s   				N(    (   t
   __author__R   (    (    (    s'   /home/vikram/FG/plot/py/bank_account.pyt   <module>   s                                                                                                                                                                                                                                                                                                                                                                                                            classes.py                                                                                          0000664 0001750 0001750 00000006143 12576632434 012453  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'


class Fruit(object):
    """A class that makes various tasty fruits."""

    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

    def how_big(self):
        if self.name == "lemon":
            print "%s is a medium sized fruit" % (self.name)
        elif self.name == "mango":
            print "Mango is a large fruit"
        else:
            print "I dont know how big a %s is" % self.name


lemon = Fruit("lemon", "yellow", "sour", False)
mango = Fruit("mango", "yellow", "sweet", False)
papaya = Fruit("papaya", "yellow", "sweet", False)
lemon.description()
lemon.is_edible()
mango.how_big()
lemon.how_big()
papaya.how_big()


class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add your method here!
    def description(self):
        print self.name
        print self.age


hippo = Animal("fatty", 3)
hippo.description()


class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."


my_cart = ShoppingCart("Vik")
my_cart.add_item("pant", 40)
my_cart.add_item("pant", 43)


class Shape(object):
    """Makes shapes!"""

    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        assert isinstance(hours, int)
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)
print milton.calculate_wage(10)
                                                                                                                                                                                                                                                                                                                                                                                                                             csvFileIO.py                                                                                        0000664 0001750 0001750 00000000601 12605777610 012631  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'

import csv
capitals = {}
with open('us-state-capitals.csv', mode='rt') as csv_file:
    reader = csv.DictReader(csv_file)
    print reader
    for row in reader:
        print row
        capitals[row['state']] = row['capital']
print capitals

capitals = {}
with open('us-state-capitals.csv', mode='rt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for                                                                                                                               dataclass.py                                                                                        0000664 0001750 0001750 00000005266 12603100764 012745  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'
'module data provides class Data(object)'

from pprint import pformat

class Data(object):
    "represents arbitrary data; provides functionality for displaying itself"\
    " properly"

    def __init__(self, *args, **kwargs):
        if args:
            self.args = args
        for key, value in kwargs.items():
            self.__dict__[key] = value
        self.assert_data()

    def __repr__(self):
        if 'args' in self.__dict__:
            args = map(repr, self.args)
        else:
            args = []
        for key, value in self.__dict__.items():
            if key != 'args':
                args.append('%s=%r' % (key, value))
        return self.__class__.__name__ + '(' + (', '.join(args)) + ')'

    def __str__(self):
        return self.formatted()

    def assert_data(self):
        "to be overridden for internal asserts after creation"

    def stringify_arg(key, value, indent=None, variables=None):
        if indent is None:
            indent = '  '
        if isinstance(value, Data):
            if variables is None:
                variables = {}
            keys, values = variables.keys(), variables.values()
            try:
                i = values.index(value)
            except ValueError:
                return ('%s%s = %s' %
                        (indent, key,
                         value.formatted(indent=indent).
                         replace('\n', '\n%s%*s' % (indent, len(key)+3, ''))))
            else:
                return ('%s%s = %s' %
                        (indent, key, keys[i]))
        else:
            return ('%s%s = %s' %
                    (indent, key,
                     pformat(value).replace('\n',
                                            '\n%s%*s' %
                                            (indent, len(key)+3, ''))))

    stringify_arg = staticmethod(stringify_arg)

    def formatted(self, indent=None, variables=None):
        result = [ self.__class__.__name__ + ':' ]
        if 'args' in self.__dict__:
            result.append(Data.stringify_arg('args', self.args,
                                             indent=indent,
                                             variables=variables))
        for key, value in self.__dict__.items():
            if key != 'args':
                result.append(Data.stringify_arg(key, value,
                                                 indent=indent,
                                                 variables=variables))
        return '\n'.join(result)

oneReg = Data(name = 'rgWDStsT', member1=(1, 'wDogExp'), member2=(8, 'wDogCntObs'))
print oneReg
print oneReg.member1
print oneReg.member2[0]
print type(oneReg.member2[0])
print "rgWDSts" + '_' + oneReg.member1[1]
                                                                                                                                                                                                                                                                                                                                          even.py                                                                                             0000664 0001750 0001750 00000007144 12575115063 011746  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'


def is_even(x):
    """

    :rtype : bool
    """
    if not x % 2:
        return True
    else:
        return False


def is_int(x):
    if abs(x - round(x)) > 0:
        print("float")
        return False
    else:
        print("int")
        return True


def digit_sum(n):
    sumOfN = 0
    i = 1
    while n != 0:
        modN = n % (10 ** 1)
        sumOfN += modN
        n = (n - modN) / 10
        print(n, modN, sumOfN)


def factorial(x):
    i = 4
    fact = 1
    while x > 1:
        fact = x * fact
        print(fact)
        x -= 1
        print(x)
        i -= 1
    print("final %d" % fact)
    return fact


def newfact(x):
    if x == 1:
        return 1
    else:
        return x * newfact(x - 1)


# is_even(3)
# is_int(-3)
# is_int(-1.3)
# is_int(4)
# digit_sum(189805)
# print factorial(8)
# print newfact(8)

def is_prime(x):
    prime = 0
    if x != 0:
        for n in range(2, x, 1):
            if x % n == 0:
                prime = 0
                break
            else:
                prime = 1
        print n
        if prime:
            return True
        else:
            return False


# print is_prime(0)

def reverse(text):
    print text
    sizeText = len(text)
    revText = ""
    print sizeText
    print text[sizeText - 1]
    for n in range(sizeText - 1, -1, -1):
        print text[n]
        revText = revText + text[n]
    return revText


# print reverse("hello6565g")

def anti_vowel(text):
    outtext = ""
    for n in range(len(text)):
        if text[n] not in "aeiouAEIOU":
            outtext = outtext + text[n]
    return outtext


# print anti_vowel("hello@ 897 #$wwer")

def trial_list(glist):
    if 'c' in glist:
        print("got it")
    else:
        print("no")


# trial_list(['a', 'b', 'd'])

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    scrab_sum = 0
    word = word.lower()
    for letter in range(len(word)):
        scrab_sum += score[word[letter]]
    return scrab_sum


# print scrabble_score("SDKLSDLKoiuJSDLKJSDKLJdslkdsjdklj")

def censor(text, word):
    textSplit = text.split()
    for item in range(len(textSplit)):
        if word == textSplit[item]:
            textSplit[item] = "*" * len(word)
    return " ".join(textSplit)


# print censor("hello how sdkfjsdlfkjhowlskdjf are you", "are")

def count(sequence, item):
    num = 0
    print(type(sequence))
    for member in range(len(sequence)):
        if item == sequence[member]:
            num += 1
    return num


# print count([2, 3, 4, 2], 3)
# print count("asdfa", "d")
# print count([[1, 2, 3], [2, 3, 4], [7, 8, 9]], [7, 80, 9])

def purify(nums):
    purified = []
    for num in nums:
        if not num % 2:
            purified.append(num)
    return purified

#print purify([1, 2, 3, 4, 5, 6, 7, 8, 90])

def product(nums):
    answer = 1
    for num in nums:
        answer *= num
    return answer

def remove_duplicates(nums):
    numbers = []
    for n in nums:
        numbers.append(n)
    unique = []
    numbers.sort()
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique
#print remove_duplicates([4, 2, 1, 4, 3, 2, 4, 5, 6, 3])

def median(nums):
    numList = nums
    size = len(numList)
    numList.sort()
    print(numList, size)
    if size%2 == 1:
        return numList[size/2]
    else:
        return (numList[size/2] + numList[(size - 1)/2])/2.0
print median([1, 1, 2, 5, 4, 4])                                                                                                                                                                                                                                                                                                                                                                                                                            exceptions.py                                                                                       0000664 0001750 0001750 00000000075 12605030244 013155  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'

while True:
    number = int(input())
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   experimentNumpy.py                                                                                  0000664 0001750 0001750 00000002253 12634353601 014214  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'
import sys
import os
from os import listdir
from os.path import isfile, join
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines

plt.close("all")

t = np.arange(0, 10, 0.01)

ax1 = plt.subplot(211)

ax1.plot(t, np.sin(2*np.pi*t))

ax2 = plt.subplot(212, sharex=ax1)

ax2.plot(t, np.sin(4*np.pi*t))

#plt.show()


# create some data to use for the plot
dt = 0.001
t = np.arange(0.0, 10.0, dt)
r = np.exp(-t[:1000]/0.05)               # impulse response
x = np.random.randn(len(t))
s = np.convolve(x, r)[:len(x)]*dt  # colored noise

# the main axes is subplot(111) by default
plt.plot(t, s)
plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])
plt.xlabel('time (s)')
plt.ylabel('current (nA)')
plt.title('Gaussian colored noise')

# this is an inset axes over the main axes
a = plt.axes([.65, .6, .2, .2], axisbg='y')
n, bins, patches = plt.hist(s, 400, normed=1)
plt.title('Probability')
plt.xticks([])
plt.yticks([])

# this is another inset axes over the main axes
a = plt.axes([0.2, 0.6, .2, .2], axisbg='y')
plt.plot(t[:len(r)], r)
plt.title('Impulse response')
plt.xlim(0, 0.2)
plt.xticks([])
plt.yticks([])

plt.show()

                                                                                                                                                                                                                                                                                                                                                     fileIO.py                                                                                           0000664 0001750 0001750 00000002301 12603272636 012150  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'
#with open("text.txt", "w") as textfile:
#    textfile.write("Done!")

#with open("text.txt", "w") as my_file:
#    my_file.write("written by my_file ptr")
#if not my_file.closed:
#    my_file.close()
#print my_file.closed

regDict = {}
with open("../../fg_dig_rr.sv", "r") as topfile:
    regDict = {line.split()[1]: line.split()[2].strip(',') for line in topfile if ('input' in line) and ('T' == line.split()[1][-1])}
print regDict
print regDict.items()[0][0]

bigList = []
with open("../../fgRgStructsPkgSMALL.sv", "r") as structfile:
    lines =structfile.readlines()

for n in lines:
    structname = ''
    fieldname = ''
    sizename = ''
    sizeMSB = '0'
    sizeLSB = '0'
    if 'logic' in n:
        if ':' not in n.split()[1]:
            fieldname = n.split()[1].strip(';')
            size = 1
        else:
            fieldname = n.split()[2].strip(';')
            sizename = n.split()[1].strip(']')
            sizeMSB = sizename.split(':')[0]
            sizeLSB = sizename.split(':')[1]
            size = int(str(sizeMSB)) - int(str(sizeLSB)) + 1
        print fieldname, size
    if '}' in n:
        structname = n.split()[1].strip(';')
        print structname










                                                                                                                                                                                                                                                                                                                               file_stats.py                                                                                       0000664 0001750 0001750 00000001126 12605545345 013144  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'
import sys

with open("../../fgRgStructsPkg.sv", mode='rt') as f:
    contents = f.read()
word_count = len(contents.split())
char_count = len(contents)
line_count = 0
for char in contents:
    if char == '\n':
        line_count += 1
print word_count, char_count, line_count

max_line_length = 0
with open("../../fgRgStructsPkg.sv", mode='rt') as f:
    for line in f:
        if len(line) > max_line_length:
            max_line_length = len(line)
print max_line_length
#print contents[-1::-1]

with open("../../reversed.sv", mode='wt') as f:
    f.write(contents[-1::-1])


                                                                                                                                                                                                                                                                                                                                                                                                                                          gcd.py                                                                                              0000664 0001750 0001750 00000000665 12600141373 011537  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'


def vikgcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    :rtype : int
    """
    i = 0
    assert isinstance(b, int)
    print(a, b)
    while b:
        a, b = b, a % b
        print(a, b)
        i += 1
    print("Done")
    return a, i

print(vikgcd(35, 25))
                                                                           hack_plot.py                                                                                        0000664 0001750 0001750 00000001730 12572363265 012756  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 # -*- coding: utf-8 -*-
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

                                        hack_plot.py~                                                                                       0000664 0001750 0001750 00000001252 12534642161 013144  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 # -*- coding: utf-8 -*-
"""
Created on Thu May 21 14:37:50 2015

@author: jblackma
"""

import sys, os, xlrd
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.lines as mlines
import numpy as np
import csv
import pickle
import itertools
import math

plt.close("all")

current = []
voltage = []

f = open('../../log/smplLogs/cITech3Ah.txt','r')
for line in f:
    if line[0] != '#':
        current.append(line.split()[13])
        voltage.append(line.split()[12])

plt.figure(1)
plt.plot(voltage)
plt.title("voltage")

plt.figure(2)
plt.plot(current)
plt.title("current")
                                                                                                                                                                                                                                                                                                                                                      listCompr.py                                                                                        0000664 0001750 0001750 00000002100 12576111232 012743  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'

even_sqaures = [x ** 2 for x in range(1, 12) if x % 2 == 0]
print even_sqaures

cubes_by_four = [n ** 3 for n in range(1, 11) if (n ** 3) % 4 == 0]
print cubes_by_four

sqaures = [x ** 2 for x in range(1, 11)]
print sqaures
special_sq = filter(lambda sq: 30 <= sq <= 70, sqaures)
print special_sq

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
print movies.items()

threes_and_fives = [x for x in range(1, 16) if x%3 == 0 or x%5 == 0]
print threes_and_fives

garbled1 = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled1[::-1]
message = message[::2]
print message

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
garbled = filter(lambda st: st != "X", garbled)
print garbled

four = 0b0100
print bin(1)
print type(bin(1))
print int("11001001", 2)

def flip_bit(number, n):
    print(bin(number))
    theNthBit = number >> n
    print(bin(theNthBit))
    print(bin(theNthBit)[0])

flip_bit(9,2)
flip_bit(9,3)


                                                                                                                                                                                                                                                                                                                                                                                                                                                                logParse.py                                                                                         0000664 0001750 0001750 00000003350 12634374147 012566  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'
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
                                                                                                                                                                                                                                                                                        logParseSoc.py                                                                                      0000664 0001750 0001750 00000002147 12636054253 013231  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'
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
                                                                                                                                                                                                                                                                                                                                                                                                                         moreClass.py                                                                                        0000664 0001750 0001750 00000003234 12577056762 012751  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'
class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides = 3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(170, 9, 1)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG" % (self.color, self.model, str(self.mpg))

    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg = mpg

    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("herald", "white", 75, "molten salt")
print my_car.condition
my_car.drive_car()
print my_car.condition

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print my_point
                                                                                                                                                                                                                                                                                                                                                                    plot1.py                                                                                            0000664 0001750 0001750 00000000134 12572360363 012042  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 import matplotlib.pyplot as plt
plt.plot([0,1,2,3,4])
plt.ylabel('some numbers')
plt.show()
                                                                                                                                                                                                                                                                                                                                                                                                                                    plot1.py~                                                                                           0000664 0001750 0001750 00000000132 12572360323 012232  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
                                                                                                                                                                                                                                                                                                                                                                                                                                      plotWithNp.py                                                                                       0000755 0001750 0001750 00000002004 12605064250 013103  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 # -*- coding: utf-8 -*-
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            plotWithNp.py~                                                                                      0000664 0001750 0001750 00000001730 12572364733 013321  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 # -*- coding: utf-8 -*-
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

                                        pyClass100115.py                                                                                    0000664 0001750 0001750 00000000762 12603322605 013070  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'

from bank_account import BankAccount

account = BankAccount()
account.deposit(40)

print(account)

def exclude(pred_func, full_list):
    exc_list = []
    for n in full_list:
        if not pred_func(n):
            exc_list.append(n)
    return exc_list
print exclude(lambda x: len(x) > 3, ["red", "blue", "green"])
print exclude(bool, [False, True, False])

def call(some_func, *args):
    print args
    return some_func(*args)

print call(int)
print call(len, "hello")

              qcClassListCompr.py                                                                                 0000664 0001750 0001750 00000002713 12603022613 014222  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'


def vowel_names(names):
    return [x for x in names if x[0] in "AEIOU"]


print vowel_names(["Alice", "Bob", "Christy", "Jules"])
names = ["Scott", "Arthur", "Jan", "Elizabeth"]
print vowel_names(names)


def power_list(numbers):
    return [n[1] ** n[0] for n in enumerate(numbers)]


numbers = [3, 2, 5]
for n in enumerate(numbers):
    print n[0], n[1]
print power_list(numbers)
numbers = [3, 2.33, 5.238729437394]
print power_list(numbers)

matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]
print matrix
flatMat = []
for row in enumerate(matrix):
    # print matrix[row[0]]
    for col in enumerate(matrix[row[0]]):
        flatMat.append(matrix[row[0]][col[0]])
print flatMat

# goodFlatMat = [matrix[row[0]][col[0]] for col in enumerate(matrix[row[0]]) for row in enumerate(matrix)]
# print goodFlatMat

bestFlatMat = [matrix[row[0]][col[0]] for row in enumerate(matrix) for col in enumerate(matrix[row[0]])]
print bestFlatMat


def get_factors(number):
    return [n for n in range(1, number + 1) if not number % n]


numSet = {62, 293, 314}
print numSet

def get_all_factors(numSet):
    return {num: get_factors(num) for num in numSet}

print get_all_factors(numSet)
numSet = {23094832, 2587245, 76, 4000}
# print get_all_factors(numSet)

unflipped = {'Python': "2015-09-15", 'Java': "2015-09-14", 'C': "2015-09-13", 'Fortran': "2015-09-13"}
print unflipped.items()
flipped = {v: k for k, v in unflipped.items()}
print flipped
                                                     qcClass.py                                                                                          0000664 0001750 0001750 00000023165 12603611311 012370  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'

words = ["there", "are", "some", "words"]
print " ".join(words)

favFruits = ["banana", "mango", "papaya", "apple", "pineapple"]
print favFruits[len(favFruits) - 3:len(favFruits)]


def vowel_names(names):
    output_names = []
    for name in names:
        if name[0].upper() in ['A', 'E', 'I', 'O', 'U']:
            output_names.append(name)
    return output_names
names = ["Scott", "Arthur", "Jan", "Elizabeth"]
print vowel_names(names)

declInd = '''Action of Second Continental Congress,\nJuly 4, 1776.\nThe unanimous Declaration of the thirteen united States of America,\n\nWHEN in the Course of human Events, it becomes necessary for one People to dissolve the Political Bands which have connected them with another, and to assume among the Powers of the Earth, the separate and equal Station to which the Laws of Nature and of Nature\xe2\x80\x99s God entitle them, a decent Respect to the Opinions of Mankind requires that they should declare the causes which impel them to the Separation.\n\nWE hold these Truths to be self-evident, that all Men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty, and the Pursuit of Happiness\xe2\x80\x94That to secure these Rights, Governments are instituted among Men, deriving their just Powers from the Consent of the Governed, that whenever any form of Government becomes destructive of these Ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its Foundation on such Principles, and organizing its Powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient Causes; and accordingly all Experience hath shewn, that Mankind are more disposed to suffer, while Evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long Train of Abuses and Usurpations, pursuing invariably the same Object, evinces a Design to reduce them under absolute Despotism, it is their Right, it is their Duty, to throw off such Government, and to provide new Guards for their future Security. Such has been the patient Sufferance of these Colonies; and such is now the Necessity which constrains them to alter their former Systems of Government. The History of the present King of Great-Britain is a History of repeated Injuries and Usurpations, all having in direct Object the Establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid World.\n\nHe has refused his Assent to Laws, the most wholesome and necessary for the public Good.\n\nHe has forbidden his Governors to pass Laws of immediate and pressing Importance, unless suspended in their Operation till his Assent should be obtained; and when so suspended, he has utterly neglected to attend to them.\n\nHe has refused to pass other Laws for the Accommodation of large Districts of People, unless those People would relinquish the Right of Representation in the Legislature, a Right inestimable to them, and formidable to Tyrants only.\n\nHe has called together Legislative Bodies at Places unusual, uncomfortable, and distant from the Depository of their public Records, for the sole Purpose of fatiguing them into Compliance with his Measures.\n\nHe has dissolved Representative Houses repeatedly, for opposing with manly Firmness his Invasions on the Rights of the People.\n\nHe has refused for a long Time, after such Dissolutions, to cause others to be elected; whereby the Legislative Powers, incapable of Annihilation, have returned to the People at large for their exercise; the State remaining in the mean time exposed to all the Dangers of Invasion from without, and Convulsions within.\n\nHe has endeavoured to prevent the Population of these States; for that Purpose obstructing the Laws for Naturalization of foreigners; refusing to pass others to encourage their Migrations hither, and raising the Conditions of new Appropriations of Lands.\n\nHe has obstructed the Administration of Justice, by refusing his assent to Laws for establishing Judiciary Powers.\n\nHe has made Judges dependent on his Will alone, for the Tenure of their Offices, and the Amount and Payment of their Salaries.\n\nHe has erected a Multitude of new Offices, and sent hither Swarms of Officers to harrass our People, and eat out their Substance.\n\nHe has kept among us, in Times of Peace, Standing Armies, without the consent of our Legislatures.\n\nHe has affected to render the Military independent of and superior to the Civil Power.\n\nHe has combined with others to subject us to a Jurisdiction foreign to our Constitution, and unacknowledged by our Laws; giving his Assent to their Acts of pretended Legislation:\n\nFor quartering large Bodies of Armed Troops among us:\n\nFor protecting them, by a mock Trial, from Punishment for any Murders which they should commit on the Inhabitants of these States:\n\nFor cutting off our Trade with all Parts of the World:\n\nFor imposing Taxes on us without our Consent:\n\nFor depriving us, in many Cases, of the Benefits of Trial by Jury:\n\nFor transporting us beyond Seas to be tried for pre-tended Offences:\n\nFor abolishing the free System of English Laws in a neighbouring Province, establishing therein an arbitrary Government and enlarging its Boundaries, so as to render it at once an Example and fit Instrument for introducing the same absolute Rule into these Colonies:\n\nFor taking away our Charters, abolishing our most valuable Laws, and altering fundamentally the forms of our Governments:\n\nFor suspending our own Legislatures, and declaring themselves invested with Power to legislate for us in all Cases whatsoever.\n\nHe has abdicated Government here, by declaring us out of his Protection and waging War against us.\n\nHe has plundered our Seas, ravaged our Coasts, burnt our Towns, and destroyed the Lives of our People.\n\nHe is, at this Time, transporting large Armies of foreign Mercenaries to compleat the Works of Death, Desolation, and Tyranny already begun with circumstances of Cruelty and Perfidy, scarcely paralleled in the most barbarous Ages, and totally unworthy of the Head of a civilized Nation.\n\nHe has constrained our fellow Citizens taken Captive on the high Seas to bear Arms against their Country, to become the Executioners of their friends and Brethren, or to fall themselves by their Hands.\n\nHe has excited domestic Insurrections amongst us, and has endeavoured to bring on the Inhabitants of our Frontiers, the merciless Indian Savages, whose known Rule of Warfare, is an undistinguished Destruction, of all Ages, Sexes and Conditions.\n\nIn every stage of these Oppressions we have Petitioned for Redress in the most humble Terms: Our repeated Petitions have been answered only by repeated Injury. A Prince, whose Character is thus marked by every act which may define a Tyrant, is unfit to be the Ruler of a free People.\n\nNor have we been wanting in Attentions to our British Brethren. We have warned them from Time to Time of Attempts by their Legislature to extend an unwarrantable jurisdiction over us. We have reminded them of the Circumstances of our Emigration and Settlement here. We have appealed to their native justice and Magnanimity, and we have conjured them by the Ties of our common Kindred to disavow these Usurpations, which, would inevitably interrupt our Connections and Correspondence. They too have been deaf to the Voice of Justice and of Consanguinity. We must, therefore, acquiesce in the Necessity, which denounces our Separation, and hold them, as we hold the rest of Mankind, Enemies in War, in Peace, Friends.\n\nWe, therefore, the Representatives of the UNITED STATES OF AMERICA, in General Congress, Assembled, appealing to the Supreme Judge of the World for the Rectitude of our Intentions, do, in the Name, and by Authority of the good People of these Colonies, solemnly Publish and Declare, That these United Colonies are, and of Right ought to be, FREE AND INDEPENDENT STATES, that they are absolved from all Allegiance to the British Crown, and that all political Connection between them and the State of Great-Britain, is and ought to be totally dissolved; and that as FREE AND INDEPENDENT STATES, they have full Power to levy War, conclude Peace, contract Alliances, establish Commerce, and to do all other Acts and Things which INDEPENDENT STATES may of right do. And for the support of this Declaration, with a firm Reliance on the Protection of divine Providence, we mutually pledge to each other our Lives, our fortunes, and our sacred Honor.'
'''
for word in declInd.split(" "):
    #if ('x' in word) or ('X' in word):
    if 'x' in word.lower():
        print word.strip(";.'")
capList = []
for x in declInd:
    if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        capList.append(x)
print capList[373:384]

def flip_dict(myDict):
    assert isinstance(myDict, dict)
    print myDict
    newkey = []
    newval = []
    for item in myDict:
        newval.append(item)
        newkey.append(myDict[item])
    print zip(newkey, newval)  # used to create a list of tuples
    return dict(zip(newkey, newval))

myDict = {'one': 1, 'two': 2, 'three': 3}
reversedDict = flip_dict(myDict)
print reversedDict

routes = {101: ("Tumwater, Washington", "Los Angeles, California"),
          66: ("Chicago, Illinois", "Santa Monica, California"),
          95: ("Miami, FL", "Sometown, Maine")}

print routes
start = ""
dest = ""
outStr = ""
for item in routes:
    start, dest = routes[item]
    print "Route %d goes from %s to %s" % (item, start, dest)

numbers = range(1, 10)
print list(enumerate(numbers))  # enumerate makes a list of tuples

                                                                                                                                                                                                                                                                                                                                                                                                           text.txt                                                                                            0000664 0001750 0001750 00000000026 12577076705 012167  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 written by my_file ptr                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          tryNp.py                                                                                            0000664 0001750 0001750 00000001124 12572431154 012114  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
print(x)
# array([1, 2, 3])
y = np.arange(10)  # like Python's range, but returns an array
print(y)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.linspace(0, 2, 4)  # create an array with 4 equally spaced points starting with 0 and ending with 2.
print(b)
plt.figure(1)
plt.plot(b)
plt.ylabel("b")

onemore = np.linspace(-np.pi, np.pi, 50)
print(onemore)

a_sine_thing = np.sin(onemore)

plt.figure(2)
plt.plot(onemore)
plt.ylabel("onemore")

plt.figure(3)
plt.plot(a_sine_thing)
plt.ylabel("a_sine_thing")

plt.show()
                                                                                                                                                                                                                                                                                                                                                                                                                                            tryNp.py~                                                                                           0000664 0001750 0001750 00000000254 12572427712 012322  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 import numpy as np
x = np.array([1, 2, 3])
x
## array([1, 2, 3])
y = np.arange(10)  # like Python's range, but returns an array
y
### array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
                                                                                                                                                                                                                                                                                                                                                    us-state-capitals.csv                                                                               0000664 0001750 0001750 00000001671 12605545713 014521  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 state,capital
Alabama,Montgomery
Alaska,Juneau
Arizona,Phoenix
Arkansas,Little Rock
California,Sacramento
Colorado,Denver
Connecticut,Hartford
Delaware,Dover
Hawaii,Honolulu
Florida,Tallahassee
Georgia,Atlanta
Idaho,Boise
Illinois,Springfield
Indiana,Indianapolis
Iowa,Des Moines
Kansas,Topeka
Kentucky,Frankfort
Louisiana,Baton Rouge
Maine,Augusta
Maryland,Annapolis
Massachusetts,Boston
Michigan,Lansing
Minnesota,St. Paul
Mississippi,Jackson
Missouri,Jefferson City
Montana,Helena
Nebraska,Lincoln
Nevada,Carson City
New Hampshire,Concord
New Jersey,Trenton
New Mexico,Santa Fe
North Carolina,Raleigh
North Dakota,Bismarck
New York,Albany
Ohio,Columbus
Oklahoma,Oklahoma City
Oregon,Salem
Pennsylvania,Harrisburg
Rhode Island,Providence
South Carolina,Columbia
South Dakota,Pierre
Tennessee,Nashville
Texas,Austin
Utah,Salt Lake City
Vermont,Montpelier
Virginia,Richmond
Washington,Olympia
West Virginia,Charleston
Wisconsin,Madison
Wyoming,Cheyenne
                                                                       vikgcd.py                                                                                           0000664 0001750 0001750 00000000540 12574113644 012253  0                                                                                                    ustar   vikram                          vikram                                                                                                                                                                                                                 __author__ = 'vikram'


def vikgcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    :rtype : int
    """
    i = 0
    while b:
        a, b = b, a % b
        i += 1
    return a, i


print(vikgcd(8, 6))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                