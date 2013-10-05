# -*- coding: utf-8 -*-
import os,os.path  
import shutil,string  
dir = "/Users/a/Desktop/twins"
if os.path.isdir(dir):
	print("Directory is exist") 
else:
	print("Directory is not exist")
	exit()
w=-1		#w=-1因为os.listdir读取时第一项是.DS_Store,要忽略掉
for i in os.listdir(dir):
	w=w+1
	print w
	print i	
	newfile=i.replace(str(i),"newname"+str(w)+".jpg")  
	oldname=dir+'/'+str(i)				
	newname=dir+'/'+str(newfile)		
	shutil.move(oldname,newname)		
print 'Rename finished!'
