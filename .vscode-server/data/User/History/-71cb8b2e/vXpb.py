#!/usr/bin/env python3

import json
import os

current_directory = os.getcwd()

for (root, dirs, files) in os.walk('.'):
   for file in files:
    file_name, file_ext = os.path.splitext(file)
    name = current_directory + '/'+file_name+file_ext
    if name.endswith(".txt"):
     with open(name, 'r') as information:
       info = information.read().split('\n')
    feedrack = {'title':info[0], 'name':info[1], 'date':info[2], 'feedback':info[3]}    
   print(feedrack['title'])
   print(feedrack['name'])
   print(feedrack['date'])
   print(feedrack['feedback'])

   request = requests.post('http://34.123.192.178/feedback/', data = feedback)

  # feed = [
    #         {
   # "title": "",
    #"name": "",
    #"date": "", 
    #"feedback": "",
    
    #}]
