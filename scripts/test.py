'#!/usr/bin/env python3
#import os
#import subprocess
import sys

logfile = sys.argv[10]

with open(logfile) as f:
  for line in f:
      print(line.strip())




#result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
#print(result.stdout.decode().split())

