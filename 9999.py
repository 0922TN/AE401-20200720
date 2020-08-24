# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:04:39 2020

@author: User
"""



names=[]
scores=[]
total=0
avg=0


n = input("班上有幾位同學")
n = int(n)


for i in range(n):
    name = input("輸入同學名字")
    names.append(name)
                 
    
    score = input('輸入同學數學成績')
    score = int(score)
    scores.append(score)
    
    
for item in scores:
    total = total+item
    
print("平均分:", (total/n))

highest=0
for i in range(n):
    if scores[i] > highest:
        highest = scores[i]
        highestname = names[i]
        
print(highestname, "最高分:" ,  highest)
       
lowest=100
for i in range(n):
    if scores[i] <  lowest:
        lowest = scores[i]
        lowestname = names[i]
        
print(lowestname, "最低分:" ,  lowest)
       
       
       
       
       
       
       
       