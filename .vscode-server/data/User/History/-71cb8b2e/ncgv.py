#!/usr/bin/env python3

import json
import os
from turtle import title


feedrack = {}
current_directory = os.getcwd()

for (root, dirs, files) in os.walk('.'):
   for file in files:
    file_name, file_ext = os.path.splitext(file)
    name = current_directory + '/'+file_name+file_ext
    #print(name)
    if name.endswith(".txt"):
     with open(name, 'r', encoding='utf-8') as infile:
       for line  in infile:
        (title, name, date, feedback) = line.split()
         #if infile.endswith(".py"):
        print(title)
        #feedrack[title] = title
        #feedrack[name] = name
        #feedrack[date] = date
        #feedrack[feedback] = feedback 
   













  # feed = [
    #         {
   # "title": "",
    #"name": "",
    #"date": "", 
    #"feedback": "",
    
    #}]
