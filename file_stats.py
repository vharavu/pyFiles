__author__ = 'vikram'
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


