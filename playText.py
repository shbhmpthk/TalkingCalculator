# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 00:28:22 2018

@author: poonam pathak
"""
# Import the required module for text 
# to speech conversion
from gtts import gTTS
from pygame import mixer
import os
def playString(str):

    # Language in which you want to convert
    language = 'en'
     
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=str, lang=language, slow=False)
     
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("result.mp3")
    
    # Playing the converted file
    file = 'result.mp3'
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while (mixer.music.get_busy()):
        1
    mixer.music.load('welcome.mp3')
    #file = 'welcome.mp3'
    #if os.path.isfile(file):
     #   os.unlink(file)
    #else:    ## Show an error ##
    #    print("Error: %s file not found" % file)
