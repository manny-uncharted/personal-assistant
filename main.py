import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text


USERNAME = config('USER')
BOTNAME = config('ASSISTANTNAME')

"""Initializing an engine that allows us to use sapi5 a Microsoft Speech API"""
engine = pyttsx3.init('sapi5')

"""Setting properties of the speech engine the RATE and VOLUME"""
engine.setProperty('rate', 190) # Rate
engine.setProperty('volume', 1.0) # Volume

""" Getting and Defining the voices that can be used from the engine, here we are using a female voice"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def greet_user():
    """Sends greeting message to user according to the time"""

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}. The time is {hour}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USERNAME}. The time is {hour}")
    elif (hour >=16) and (hour <=19):
        speak(f"Good evening {USERNAME}. The time is {hour}")
    speak(f"I am {BOTNAME} your personal assistant. How may I assist you?")


# Text to speech conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# User input
def take_user_input():
    """Takes user input, recognizes it using the speech recognition module and parses it into text.
    The recognizer class is used to recognize the audio taken through the device microphone as the source.
    A pause threshold was set to 1, so that there won't be a complaint even if there's a one second pause

    language was set to English USA
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-US')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, do take care!. {BOTNAME} is going offline now")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that all over again')
        query = 'None'
    return query
    