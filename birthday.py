import time
import json



birthday = {}

with open('birthday.json') as f:
    data = json.load(f)


# Print to check if JSON loaded alright.
print(data)

# Format to day.month
dm = time.strftime("%d.%m")
print(f"Today is", dm)

# print(type(dm)) to check the type

# Convert to a string
str_dm = str(dm)

# Search the dictionary for 
for name, age in data.items():
    if age == str_dm:
        print(f"Today is {name}'s birthday!")
