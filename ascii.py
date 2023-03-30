import argparse
import numpy as np
from PIL import Image


class convert():
    descStr = "This program converts ASCII art into an image."
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--file', dest='filename', required=True)
    
    args = parser.parse_args()
    filename = args.filename
    
    
    list=".,:;+*?%S#@"
    bright=dict()
    color = 255
    for loop in list:
        bright.update({loop:color})
        color=color-(int(color/len(list)))
    txt = open(filename,"r")
    line = txt.readlines()
    height=0
    for i in line:
        width=0
        for j in i:
            width+=1
        height+=1
    arr=[]
    final=[]
    for i in line:
        for j in i:
            if j!="\n":
                arr.append(bright[j])
        final.append(arr)
        arr=[]
    final = np.array(final)
    pic = Image.fromarray(np.uint8(final), mode='L')
    pic.save("photo.jpg")  


if __name__ == '__main__':

    convert()
    
        
    
        
        
    

    
