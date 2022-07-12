#!/usr/bin/env python3

import json
import os


feedrack = {}

for file in os.getcwd():
    for title, name, date, feedback in file:
        feedback[title] = title
        feedback[name] = name
        feedback[date] = date
   













  # feed = [
    #         {
   # "title": "",
    #"name": "",
    #"date": "", 
    #"feedback": "",
    
    #}]