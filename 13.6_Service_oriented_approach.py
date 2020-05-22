# API
# application program interface
# ways to use web protocol to access data on systems, using well-defined and structured approaches
# google geocoding API
import urllib.request, urllib.parse, urllib.error
import json
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : address = 'Ann Arbor, MI'

    url = serviceurl + urllib.parse.urlencode({'address':address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)
        continue
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',lng)
    location = js['results'][0]['formatted_address']
    print(location)