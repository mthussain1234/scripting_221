# Python Libraries and Modules

# Extensive libraries in Python
# external package that you can install, once installed
# can use functions in the library to accelerate development

# Python comes with some integrated libraries

from random import *

print(randint(1, 199))

import math

num_float = 23.21

print(math.floor(num_float))
print(math.ceil(num_float))
print(math.pi)

# Modules
import os
import datetime, sys

working_dir = os.getcwd()
print(working_dir)

print(datetime.date.today())

print(sys.path)

def operating_system_information():
    print(os.cpu_count())

operating_system_information()

# pip - pythons package manager
import requests

requests_bbc = requests.get("https://www.bbc.co.uk")

print(requests_bbc.status_code)
# print(requests_bbc.content)









