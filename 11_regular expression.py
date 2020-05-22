# re.search () like find()

import re
name = input('Please enter a file name: ')
if len(name) < 1 : name = 'mbox-short.txt'
fhand = open(name)
for line in fhand:
    line = line.rstrip()
# use find()
    #if line.find('From: ') >= 0:
       # print(line)
# use re.search()
    #if re.search('From ',line):
        #print(line)
# re.search() like startswith()
# use startswith()
    #if line.startswith('From: '):
    #print(line)
# use re.search()
    #if re.search('^From: ',line):
         #print(line)

# wild-card character
# ^X.*: 
# ^ means start with  
# . means any char  
# * means 0 or more times
# : means any char
'''
# ^	Matches the beginning of a line
$	Matches the end of the line
.	Matches any character
\s	Matches whitespace
\S	Matches any non-whitespace character
*	Repeats a character zero or more times
*?	Repeats a character zero or more times (non-greedy)
+	Repeats a character one or more times
+?	Repeats a character one or more times (non-greedy)
[aeiou]	Matches a single character in the listed set
[^XYZ]	Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	Indicates where string extraction is to start
)	Indicates where string extraction is to end
'''
