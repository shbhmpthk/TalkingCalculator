# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 23:50:57 2018

@author: shubham pathak
"""
from speechRecog import *
import playText
import operandGenerator
import operatorDetector


# The text that you want to convert to audio
playText.playString('Welcome to the new age of calculator. How may i help you?')
result=0
while(1):    
    a=''
    b=''
    operator=''
    
    mytext = getString()
    if(type(mytext).__name__=='NoneType'):
        playText.playString('Sorry I didn\'t get that. Try again')
        continue
    
    operator = operatorDetector.findOperator(mytext)
    if(operator=='c'):
        playText.playString('Thanks for using me. See ya. Good Bye')
        break
    elif(operator=='gtng'):
        playText.playString('Hello shubhi')
    elif (operator == '-1'):
        playText.playString('I dont think you are using me correctly. Bye bye')
        break
    a,b = operandGenerator.findOperand(mytext,result)
    if(a=='' and b==''):
        playText.playString('Sorry I didn\'t recognised operands. Try again')
        continue
    if(b=='' or a==''):
        playText.playString('Sorry I didn\'t find second operand. Say it again')
        while(a==''):
            mytext = getString()
            if(type(mytext).__name__=='NoneType'):
                playText.playString('Sorry. Please say the second operand again')
                continue
            try:
                a= float(mytext)
            except ValueError :
                a=''
                playText.playString('Sorry. Please say the second operand again')
                continue
    
        while(b==''):
            mytext = getString()
            if(type(mytext).__name__=='NoneType'):
                playText.playString('Sorry. Please say the second operand again')
                continue
            try:
                b= float(mytext)
            except ValueError :
                b=''
                playText.playString('Sorry. Please say the second operand again')
                continue
    if(operator == 'sf'):
        result = float(b)-float(a)
    elif(operator == '-'):
        result = float(a)-float(b)
    elif(operator == '/'):
        result = float(a)/float(b)
    elif(operator == 'dv'):
        result = float(b)/float(a)
    elif(operator=='+'):
        result = float(a) + float(b)
    elif(operator=='*'):
        result = float(a)*float(b)
    playText.playString('Answer is  %0.3f' % (result))
    playText.playString('Do you wanna do more calculation?')
    mytext = getString()
    if(type(mytext).__name__=='NoneType'):
        playText.playString('We are unable to recognise your voice.  Restart the app')
        break
    if 'no' in mytext:
        playText.playString('Thanks for using me. See ya. Good Bye')
        break
    else:
        playText.playString('I am ready again')
        
 

