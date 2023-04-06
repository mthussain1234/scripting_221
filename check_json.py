import os
import sys
import json

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON IS VALID!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("usage: check_json.py <file>")