#!/usr/bin/env python3

import json
import os



feedrack = {}
current_directory = os.getcwd()

for (root, dirs, files) in os.walk('.'):
   for file in files:
    file_name, file_ext = os.path.splitext(file)
    name = current_directory + '/'+file_name+file_ext
    #print(name)
    if name.endswith(".txt"):
     with open(name, 'r', encoding='utf-8') as information:
       info = information.read().split('\n')
         #if infile.endswith(".py"):
    print(info[0])
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
