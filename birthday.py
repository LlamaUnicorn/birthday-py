import time
import json



birthday = {}

with open('birthday.json') as f:
    data = json.load(f)


print(data)


dm = time.strftime("%d.%m")
print(f"Today is", dm)
# print(type(dm))

str_dm = str(dm)


for name, age in data.items():
    if age == str_dm:
        print(f"Today is", name, "'s birthday")
