---
name: "Object Generation from Structured Data"
description: "Generating objects from structured data such as JSON."
category: general
authors: [yuhattor] 
platforms: [copilot, copilot-chat]
level: lv2
---

## Object Generation from Structured Data

[<img src="https://img.shields.io/badge/Lv2-Practically_Viable_Pattern-green">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

Working with structured data is an everyday task for developers. Transforming data from formats like JSON into objects within your programming language allows for more robust and maintainable code. Imagine you have a list of users, and you want to convert this data into user objects within your application. GitHub Copilot can help you in this transformation process, turning a tedious task into a seamless exercise.

#### Example

Here's a Python example of how you might convert the given JSON data into a list of user objects:

```python
import json

json_data = '[{"id": "1", "name": "Yuki Hattori"}, {"id": "2", "name": "George Hattori"}]'
users = json.loads(json_data)

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

user_objects = [User(user['id'], user['name']) for user in users]

for user in user_objects:
    print(user.id, user.name)
```

### Exercise

- **Exercise 1**: Try generating objects from a different JSON structure, e.g., a JSON that includes address information for the users.
- **Exercise 2**: Experiment with handling edge cases, such as missing data within the JSON, and ensure that your code handles them gracefully.

### Checklist for Further Learning

- How would you modify the code to accommodate a more complex data structure?
- What methods could you use to validate the data before transforming it into objects?
- How can this pattern be adapted to different programming languages or frameworks?