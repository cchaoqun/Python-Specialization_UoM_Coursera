import re
name = input('Please enter a file name: ')
if len(name) < 1 : name = 'mbox-short.txt'
fhand = open(name)
numlis = list()
for line in fhand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlis.append(num)

print('list of number is:',numlis,'\n''Maximum: ', max(numlis))