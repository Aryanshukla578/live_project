Text to Speech Python Project
The objective of this project is to convert the text into voice with the click of a button. This project will be developed using Tkinter, gTTs, and playsound library.

In this project, we add a message which we want to convert into voice and click on play button to play the voice of that text message.

Importing the modules
Create the display window
Define functions
So these are the basic steps that we will do in this Python project. Let’s start.

1. Import Libraries
Let’s start by importing the libraries: tkinter, gTTS, and playsound

from tkinter import *
From gtts import gTTS
From playsound import playsound
2. Initializing window
root = Tk()
geometry root.("350x300") 
root.configure(bg='ghost white')
root.title("DataFlair - TEXT TO SPEECH")
Tk() to initialized tkinter which will be used for GUI
geometry() used to set the width and height of the window
configure() used to access window attributes
bg will used to set the color of the background
title() set the title of the window
Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="DataFlair", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)
Label() widget is used to display one or more than one line of text that users can’t able to modify.

root is the name which we refer to our window
text which we display on the label
font in which the text is written
pack organized widget in block
Msg is a string type variable
Entry() used to create an input text field
textvariable used to retrieve the current text to entry widget
place() organizes widgets by placing them in a specific position in the parent widget
3. Function to Convert Text to Speech in Python
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
Message variable will stores the value of entry_field

text is the sentences or text to be read.
lang takes the language to read the text. The default language is English.
slow use to reads text more slowly. The default is False.
As we want the default value of lang, so no need to give that to gTTS.

speech stores the converted voice from the text
speech.save(‘DataFlair.mp3’) will saves the converted file as DataFlair as mp3 file
playsound() used to play the sound
4. Function to Exit
def Exit():
    root.destroy()
root.destroy() will quit the program by stopping the mainloop().

5. Function to Reset
def Reset():
    Msg.set("")
Reset function set Msg variable to empty strings.

6. Define Buttons
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)
Button() widget used to display button on the window

 

root.mainloop()
root.mainloop() is a method that executes when we want to run our program
