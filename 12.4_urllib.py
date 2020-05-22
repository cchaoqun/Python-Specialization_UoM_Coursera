# urllib 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
'''
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhand:
    words = line.decode().split()
    for w in words:
        count[w] = count.get(w,0) + 1
print(count)

'''
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())