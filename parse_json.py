import json
import os


# json = json.loads(open("C:/Users/tahir.LAPTOP-2JTDBK37/Documents/tech_221/scripting/example.json").read())
# value = json["country"]
# print(value)

# script to create absolute path variable
script_dir = os.path.dirname(__file__)
print("The script is located at:" + script_dir)
script_absolute_path = os.path.join(script_dir, 'example.json')
print("Script path is: " + script_absolute_path)

# script parse
json = json.loads(open(script_absolute_path).read())
value = json["website"]
print(value)

# Loop through json keys and values, print them out

# for keys, values in json.items():
#     print(keys, ":", values)

for key in json:
    value = json[key]
    print("Key and value are {} = {}".format(key, value))

# What is YAML
# YAML is designed to be simple and easy to read,
# often used for configuration files and data exchange between applications
# What does it stand for - yet another markup language
# How is it used - creating configuration files, defining build pipelines,and managing IAC.
# Difference between YAML and markdown?
