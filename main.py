from platform import uname
import pyttsx3 
import shutil
import time
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import *

#importing all our functions from the functions folder
from functions.online_ops import *
from functions.os_ops import *
from pprint import pprint


# BOTNAME = config('ASSISTANTNAME')

"""Initializing an engine that allows us to use sapi5 a Microsoft Speech API"""
engine = pyttsx3.init('sapi5')

"""Setting properties of the speech engine the RATE and VOLUME"""
engine.setProperty('rate', 190) # Rate
engine.setProperty('volume', 1.0) # Volume

""" Getting and Defining the voices that can be used from the engine, here we are using a female voice"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


""" To set the username for the user using the assistant """
class User:
    def username(self, uname):
        speak("What should i call you sir")
        self.uname = take_user_input()
        speak("Welcome Mister")
        speak(uname)
        columns = shutil.get_terminal_size().columns

        print("##############".center(columns))
        print("Welcome Mr.", self.uname.center(columns))
        print("##############".center(columns))
        speak("How can i help you, Sir")
        return uname


    def greet_user(self):
        """Sends greeting message to user according to the time"""

        assname = ("Lucy")
        hour = datetime.now().hour
        minute = datetime.now().minute
        if (hour >= 6) and (hour < 12):
            speak(f"Good Morning {self.uname}. The time is {hour} hours and {minute} minutes ")
        elif (hour >= 12) and (hour <= 16):
            speak(f"Good afternoon {self.uname}. The time is {hour} hours and {minute} minutes ")
        elif (hour >=16) and (hour <=19):
            speak(f"Good evening {self.uname}. The time is {hour} hours and {minute} minutes ")
        speak(f"I am {assname} your personal assistant. How may I assist you?")
        return assname

u = User() # calling the user class to be able to instantiate the functions in it.


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
        speak(choice(opening_text))

        # if not 'exit' in query or 'stop' in query:
        #     speak(choice(opening_text))

        # else:
        #     hour = datetime.now().hour
        #     if hour >= 21 and hour < 6:
        #         speak(f"Good night sir, do take care!. {BOTNAME} is going offline now")
        #     else:
        #         speak('Have a good day sir!')
        #     exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that all over again')
        return 'None'
    return query

def clear_existing():
    clear = lambda: os.system('cls')

"""Here within the main method we initialized the greet function to greet the user
Then we ran a loop that continously takes input from the user using the take_user_input() function"""
if __name__ == '__main__':

    clear_existing()
    u.username(uname)
    # USERNAME =  # Assigns the username in the function Username to a global variable USERNAME
    u.greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad ' in query:
            open_notepad()

        elif 'open calculator' in query:
            open_calculator()

        elif 'open command prompt' in query or 'open cmd ' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open discord' in query:
            open_discord()

        elif 'open excel' in query or 'open microsoft excel' in query:
            open_excel()

        elif 'open word' in query or 'open microsoft word' in query:
            open_microsoft_word()

        elif 'open slack' in query:
            open_slack()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif "send an email" in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")

        elif 'exit' in query:
            speak(f"Thanks I am going offline now")
            exit()

        # To check how the assistant is doing    
        elif 'how are you doing today' in query:
            speak("I guess i'm fine, Thank you")
            speak("How are you, also doing Sir")

        elif 'fine' in query or 'good' in query:
            speak("It's good to know that you're fine")
