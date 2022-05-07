"""Allows the assistant to interact with several online functions such as:
Find my IP address
Search on Wikipedia
Play videos on YouTube
Search on Google
Send WhatsApp message
Send Email
Get Latest News Headlines
Get Weather Report
Get Trending Movies
Get Random Jokes
Get Random Advice
"""
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
NEWS_API_KEY = config("NEWS_API_KEY")
OPEN_WEATHER_APP_ID = config("OPEN_WEATHER_APP_ID")
# TMDB_API_KEY = config("TMDB_API_KEY")

# To check my ip address
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

# Search information on wikipedia
def search_on_wikipedia(query):
    """Search's the query on wikipedia and summarizes the information into 2 sentences"""
    results = wikipedia.summary(query, sentences = 2)
    return results

# play videos on youtube function
def play_on_youtube(video):
    kit.playonyt(video)

# Search on Google function
def search_on_google(query):
    kit.search(query)

# Send whatsapp message function
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+234{number}", message)

# Send emails function using the smtplib module

def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

#Get latest news headlines
def get_latest_news():
    """Returns the first 5 business news in Nigeria"""
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=ng&apiKey={NEWS_API_KEY}&category=business").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

# Get weather report
def get_weather_report(city):
    res = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_APP_ID}&units=metric").json()    
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

# Get trending movies from the The Movie Database (TMDB)
# def get_trending_movies():
#     trending_movies =[]
#     res = requests.get(
#         f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
#     results = res["results"]
#     for r in results:
#         trending_movies.append(r["original_title"])
#     return trending_movies[:5] # return first 5 trending movies

# We can't leave this out without having the bot get sone great punchline jokes. 
"""Function to get jokes from https://icanhazdadjoke.com"""
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


# An assistant can't be complete if it can't give your some random advice.
"""Function to get a random piece of advice"""
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
