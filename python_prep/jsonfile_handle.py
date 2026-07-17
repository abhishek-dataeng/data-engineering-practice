import json

with open('/home/abhishek/projects/python_prep/data/jsonfile.json') as f:
    data = json.load(f)

print(data)
data1 = json.loads('{"name":"john","age":25,"city":"delhi"}')

with open('/home/abhishek/projects/python_prep/data/jsonfile.json', 'w') as f:
    json.dump(data1,f)

json_string = json.dumps(data1)
print(json_string)