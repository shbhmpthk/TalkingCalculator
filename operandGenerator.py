# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 23:46:17 2018

@author: poonam pathak
"""
def findOperand(mytext,result):
    i=0;
    while (i<len(mytext) and not mytext[i].isdigit()):
        i+=1
    start=i;
    while (i<len(mytext) and (mytext[i].isdigit())):
        i+=1
    operand1 = mytext[start:i]
    while (i<len(mytext)and not mytext[i].isdigit() ):
        i+=1
    start=i;
    while (i<len(mytext) and (mytext[i].isdigit())):
        i+=1
    operand2 = mytext[start:i]
    if('result' in mytext):
        operand2 = result
    mylist =[operand1,operand2]
    return mylist