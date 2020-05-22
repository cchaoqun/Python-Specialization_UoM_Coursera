import urllib.request, urllib.parse, urllib.error
import beautifulsoup
url = input('Enter -')
html = urllib.request().urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag,get('href', None))
