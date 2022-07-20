#!/usr/bin/env python3
import PIL
import os, sys
from PIL import Image

#TROUBLESHOOTING ONLY
current_directory = os.getcwd()
print(current_directory)
#contents = os.listdir(current_directory)
#im = Image.open("image.jpg")
#im.show()
#print(contents)
#print(im.size,im.format,im.mode)


for (root, dirs, files) in os.walk('.'):
    for file in files:
      file_name, file_ext = os.path.splitext(file)
      name = current_directory + '/'+file_name+file_ext
      print(name)
      
      try:
        Image.open(file).rotate(90).convert("RGB").save(name)

      except IOError:
           print("cannot convert", file)