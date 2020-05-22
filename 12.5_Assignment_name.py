'''Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to 
http://www.py4e.com/code3/urllink2.py. 
The program will use urllib to read the HTML from the data files below, and parse the data,
extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the 
other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_391150.html (Sum ends with 84)
You do not need to save these files to your folder since your program will read the data directly from the URL.
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format
The file is a table of names and comment counts. You can ignore most of the data in the file except for lines 
like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags. '''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


url = input('Enter url - ')
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = int(input('Enter count -'))
position = int(input('Enter position -'))
for i in range(count):
    html = urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")

    tags = soup('a')
    link = list()
    name = list()
    for tag in tags:
        x = tag.get('href',None)
        y = tag.text
        link.append(x)
        name.append(y)

    print(link[position-1])
    print(name[position-1])
    url = link[position-1]
