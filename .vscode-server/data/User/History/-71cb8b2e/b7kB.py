#!/usr/bin/env python3

import json
import os


feedrack = {}
current_directory = os.getcwd()

for (root, dirs, files) in os.walk('.'):
   for file in files:
    file_name, file_ext = os.path.splitext(file)
    name = current_directory + '/'+file_name+file_ext
    print(name)

    with open(name.endswith(".py"), 'r', encoding='utf-8') as infile:
       for title  in infile:
         #if infile.endswith(".py"):
          print(title)
        #feedrack[title] = title
        #feedrack[name] = name
        #feedrack[date] = date
        #feedrack[feedback] = feedback 
   
print(title)












  # feed = [
    #         {
   # "title": "",
    #"name": "",
    #"date": "", 
    #"feedback": "",
    
    #}]
