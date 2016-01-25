__author__ = 'vikram'
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










