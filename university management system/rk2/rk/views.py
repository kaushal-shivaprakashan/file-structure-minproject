from asyncore import write
import os
from random import sample
import sys
import csv
import re

def add(i):
     with open('data.csv','a+',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(i)



def view():
    data=[]
    with open('data.csv') as file:
        reader=csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data


 
def remove(i):
    def save(j):
        with open('data.csv','w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(j)
    new_list=[]
    proj_id=i

    with open('data.csv') as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element==proj_id:
                    new_list.remove(row)
        save(new_list)

def update(i):
    def update_newlist(j):
        with open('data.csv','w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(j)
    
    new_list=[]
    proj_id=i[0]
    

    with open('data.csv','r')as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element==proj_id:
                    name1=i[1]
                    name2=i[2]
                    email=i[3]
                    proj_id=i[4]

                    data=[name1,name2,email,proj_id]
                    index=new_list.index(row)
                    new_list[index]=data
    update_newlist(new_list)

def search(i):
    data=[]
    proj_id=i   

    with open('data.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            for element in row:
                if element==proj_id:
                    data.append(row)
                    break#my added
    print(data)
    return data

def key_sort(USN):
	t=list()
	fin=open(USN,'r')
	for line in fin:
		line=line.rstrip('\n')
		words=line.split('|')
		t.append((words[0],words[1]))
	fin.close()
	t.sort()
	with open("data.csv",'w') as fout:
		for pkey,addr in t:
			pack=pkey+"|"+addr+"|#"
			fout.write(pack+'\n')
	os.remove(USN)
	os.rename("data.csv",USN)

def binary_search(list, n):  
    low = 0  
    high = len(list) - 1  
    mid = 0  
  
    while low <= high:  
        mid = (high + low) // 2  
        if list[mid] < n:  
            low = mid + 1        
        elif list[mid] > n:  
            high = mid - 1         
        else:  
            return mid           
    return -1     


            


