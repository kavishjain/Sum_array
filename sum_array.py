# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 11:58:27 2020

@author: jnk5kor
"""
# Given an array of numbers, write a progem to find a number which has same sum of numbers on it's either side
lis=[]
temp=0
flag=0
len= int(input("enter the length of array"))
for _ in range(len):
    num=int(input("enter the element in array"))
    lis.append(num)
print(lis)
for x in range(0,len):
    temp=temp+lis[x]
    tot=sum(lis[x+2:len])
    if temp == tot:
       # print("number found =",lis[x+1])
        flag=1
        break
if flag==1:
    print("number found =",lis[x+1])
else:
    print("no such combinations")