import json
input = '''
[
    { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    { "id" : "009",
    "x" : "7",
    "name" : "Brian"
    }
]'''
info = json.loads(input)
print('user count: ', len(info))

for item in info:
    print('id: ',item['id'])
    print('attribue: ', item['x'])
    print('name: ', item['name'])