# Two types of serialization formates
# Agreeing on a 'Wire Format'
# XML = Extensible Markup Language

# purpose is to share structed data
# started as a simpliefied subset of the Standard Generalized Markup Language(SGML) and is designed to be relatively human-legible

# serialize/ De-Serialize - Convert data in one program into a common format that 
# can be stored and/or transmitted between systems in a programming languag-independent manner
''' # triple quoted string
<people> #start tag
    <person>
    <name>Chuck</name>
        #Text Content
    <phone type="intl">+1 734 303 4456</phone>
           #Attribute
    <email hide="yes"/>
    #self Closing Tag
    </person>
</people> # end tag
'''
import  xml.etree.ElementTree as ET 
data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print('Name: ', tree.find('name').text )
print('email: ', tree.find('email').get('hide'))
# XML Schema
# Describing a "contract" as to what is acceptable XML
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brian</name>
        </user>
    </users>
</stuff>'''
stuff = ET.fromstring(input)
lis = stuff.findall('users/user')
print('List of stuff is: ', lis, '\n' 'User count: ', len(lis))
for item in lis:
    print('name: ',item.find('name').text)
    print('id: ', item.find('id').text)
    print('attribute: ', item.get('x'))
# Parsing XML


# JSON
