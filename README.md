# TalkingCalculator
The news age of calculator, which is capable to take voice input and also speak the result
# System Requirements
1)	Python 3.x preferably anaconda
2)	Following modules must be installed in python

•	Speech recognition module,
•	pyaudio module,
•	Gtts,
•	Pygame,
•	pyttsx module

We can use pip install command to install above mentioned module.
3)	System should be microphone enabled. It should be capable of recording voice.
4)	System should have speakers connected to it.

# Working Model

1)	First of all we set sampling rate approximate to the human voice i.e. 48000 and chunk size of 1024 kb.
2)	After checking all the available microphones on the system, we verified and took permission to use specified microphone.
3)	The microphone will then record the audio from the microphone source set in step 2.
4)	This audio file is passed to Google speech recognition Api which convert speech to text using pre trained recurrent neural network.
5)	A Neural Network that has a memory that influences future predictions. That’s because each letter it predicts should affect the likelihood of the next letter it will predict too.
6)	The string received from Google API is then fed to tokenizer. That will convert the string into a number of tokens.
7)	Operand Identifier: This is a classifier which will identify the operands among the token generated from step 6.
8)	If the number of operand identified in step 7 is less than two, the talking calculator will notify the user about the concerned error.
9)	Operator Classifier: A class for each operator is created that contain all the abbreviation of that operator. This classifier will classify any abbreviation of operator to its literal meaning.
10)	After the identification of operator and operands, we perform asked calculation.
11)	The answer is then given to gTTS which use sophisticated linguistic analysis and syntactical analysis to convert answer to speech.
12)	The system is capable to remind the result of last operation and thus can be used to calculate a chain of arithmetic calculations.

