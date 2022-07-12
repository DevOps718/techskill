#!/usr/bin/env python3

import json
import os


feedrack = {}

for file in os.getcwd():
    for title, name, date, feedback in file:
        feedrack[title] = title
        feedrack[name] = name
        feedrack[date] = date
        feedrack[feedback] = feedback 
   
print(feedrack[feedback])












  # feed = [
    #         {
   # "title": "",
    #"name": "",
    #"date": "", 
    #"feedback": "",
    
    #}]