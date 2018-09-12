import json
jsonData = '{"name":"Frankfurt","age":67}'
jsonToPython = json.loads(jsonData)
print(jsonToPython)