# Python Scripting
import subprocess
# Easy to understand
# Many Libraries
# Large Community
# Language interoperability (Python talks to other languages and software easily)

# Why do we care about scripting?
# Automate repetitive manual tasks using code

# Some examples of things we can write scripts for as DevOps engineers:

# Python to query a database
# Write Python script to execute a shell command
# Python to create a backup
# Python script to fetch I.P's addresses of an autoscaling
# Python script to check the expiry date of an SSL certificate

# Seven inbuilt modules that allow us to do some interesting things:

# sys
# os
# subprocess
# math
# random
# datetime
# json

# sys module
import sys

print(sys.version)

# os module
import os

# print(os.getcwd())
# os.chdir("C:/Users/tahir.LAPTOP-2JTDBK37/Documents/tech_221")
# print(os.getcwd())
#
# os.mkdir("new_dir2")

# subprocess module
import subprocess

# Be careful to not create infinite loops. Automate only after your happy with the manual process.
subprocess.run(["python", "hello_world.py"])

# math module
import math

pi = math.pi
pi_string = str(pi)
print("Value of pi is " + pi_string)

# random module
import random

randnum = random.randrange(1, 10)
print(randnum)

# datetime module
import datetime

whatisthedate = datetime.datetime.now()
print(whatisthedate)

# json module
import json

x = {
    "name": "John",
    "age": 30,
    "city": "London"
}

y = json.dumps(x)

print(x)
print(y)

