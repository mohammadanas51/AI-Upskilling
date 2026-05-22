import json

json_string = '''
{
  "firstName": "John",
  "lastName": "Doe",
  "age": 30,
  "isEmployed": true,
  "skills": ["JavaScript", "Python", "React"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "country": "USA"
  }
}
'''

data = json.loads(json_string)

newData = json.dumps(json_string, indent=2)
print(type(data))  # Type dictionary
print(type(newData)) # type string 