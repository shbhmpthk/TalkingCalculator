# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 00:19:12 2018

@author: poonam pathak
"""

def findOperator(mytext):
    dict={'add':'+','subtracted from':'sf','subtract':'-','-':'-','+':'+', \
          '/':'/','by':'/','divides':'dv','close':'c','hi':'gtng','into':'*'}
    for key in dict.keys():
        if key in mytext:
            return dict[key]
        
    return '-1';
    