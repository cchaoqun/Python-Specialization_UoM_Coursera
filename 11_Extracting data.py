# re.search() returns a True/False depending on whether the string matches the regular expression
# if we want the matching strings to be extracted, we use 
# re.findall()

# [0-9]+ 
# [] means single digit from 0 to 9  
# + means one or more
import re
x = 'My 2 favorite number are A 16 and 42'
y = re.findall('[0-9]+',x)
print(y)
z = re.findall('[AEIOU]',x)
print(z)

# Greedy Matching 
# The repeat character(* and .) push outward in both directions to match the largest possible string
x = 'From: Using the: Character'
y = re.findall('^F.+:',x)
z = re.findall('^F.:',x)
print(y,z)

# Nor greedy matching
# '^F.+?:'  
# ^ means starts with 
# . means any char 
# + one or more char 
# ? donot be greedy prefer the shortest
x = 'From: Using the: Character'
y = re.findall('^F.+?:',x)
print(y)

# \s@+\s+  
# \s means at least one no blanket char 
# + means one or more no blanket char 
import re
a = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
b = re.findall('\S+@\S+',a)
print(b)
c = re.findall('^From (\S+@\S+)',a) #() means the stuff I want to extract
print(c)

d = re.findall('@([^ ]*)',a) 
e = re.findall('^From .*@([^ ]*)',a)
# find a @ 
# want stuff after @ 
# ^ means everything but not a blanket
print(d,e)

# '\' means the original behave of a regular expression prefix it with '\'
A = 'We just received $10.00 for cookies'
B = re.findall('\$[0-9.]+',A)
print(B)