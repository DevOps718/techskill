#!/usr/bin/env python3
import PIL
import os, sys
from PIL import Image

#TROUBLESHOOTING ONLY
current_directory = os.getcwd()
#print(current_directory)
#contents = os.listdir(current_directory)
#im = Image.open("image.jpg")
#im.show()
#print(contents)
#print(im.size,im.format,im.mode)


#path = r'C:\Users\IMRRO\OneDrive\Desktop\images'

for (root, dirs, files) in os.walk('.'):
    for file in files:
        if file.endswith(".jpg"):
            name = os.getcwd() + '\\'+file
            im = Image.open(name)
            #print(im)
            #with open(name) as im:
                #im.show()            
      
        #file[0].split('.jpg')
        #img = Image.open()
        #file_name, file_ext = os.path.splitext(file)
    
        #img.save('{}.png'.format(file_name))
        

    #out = im.rotate(45)
    #print(out)
    