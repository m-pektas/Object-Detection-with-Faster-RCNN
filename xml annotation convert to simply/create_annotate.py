
import os
import re


def write(filepath,x1,y1,x2,y2,classname):
    f = open("annotate.txt","a+")
    f.write(filepath+","+x1+","+y1+","+x2+","+y2+","+classname+"\n")
    

root_dir = "./train_labels_xmls/"
xmls = os.listdir(root_dir)
objects = []
for i in xmls:
    path = root_dir+i
    file = open(path,"r")
    s = ""
    for j in file:
        s = s + j
        
    path = re.search('<path>(.*)</path>', s).group(1)
    objects = s.split("<object>")
    
    for k in range(1,len(objects)):
        xmin = re.search('<xmin>(.*)</xmin>', objects[k]).group(1)
        ymin = re.search('<ymin>(.*)</ymin>', objects[k]).group(1)
        xmax = re.search('<xmax>(.*)</xmax>', objects[k]).group(1)
        ymax = re.search('<ymax>(.*)</ymax>', objects[k]).group(1)
        name = re.search('<name>(.*)</name>', objects[k]).group(1)
        print (name,xmin,ymin,xmax,ymax)
        write(path,xmin,ymin,xmax,ymax,name)
        
        
    







