# personal-assistant
A personal assistant package

This project is one which I decided to create one morning, after reading an article written by a friend of mine. 

Imagine waking up one morning and then being greeted by your personal assistant, which can seamlessly connect across different devices in your home. From you waking up to the sound of good morning “Manuel” and it telling you your schedule for the day and a bunch of other activities for it to assist you with.
The projects’ skeletal structure is written in python, it’s just a simple collection of python script that runs on the local machine as of present
My goal is to create a customizable assistant (package) that can be integrated across different devices and interfaces, from smart watches, homes, cars, mirrors and several others not excluding your laptop and phone while making it customizable for both developers and non-developers (possibly end users).

The goal is to have multiple api endpoints for various devices.

### It's an open source project and open to contributions to make it better.

Currently the program runs efficiently on the local machine. 


## To start the program 
1. clone the program with
''' 
git clone "https://github.com/manny-uncharted/personal-assistant"
'''

2. create a .env file that contains on the required API Keys for the needed api's used. 
"API used are below with their declarative names and the sites to get them"
- EMAIL (Your email address ensure that you've allowed third-party access to send emails using the mail)
- PASSWORD (Your email password)

- NEWS_API_KEY (You have to sign up on https://newsapi.org/ to get your api key)

- OPEN_WEATHER_APP_ID (Same goes here you sign up at https://openweathermap.org/ and get your api key)

- TMDB_API_KEY (This is to get latest movie updates sign up at https://www.themoviedb.org/ and create a free account and create an api key).

There's still a lot to be done on the project to create api endpoints that ensure the program can work across multiple devices seamlessly.

## Features
Currently the assistant can interact with several online and offline functions functions such as:
- Find my IP address
- Search on Wikipedia
- Play videos on YouTube
- Perform search on Google
- Send WhatsApp message (Though works with only whatsapp web for now)
- Send Emails
- Get Latest News Headlines
- Get Weather Report
- Get Trending Movies
- Get Random Jokes
- Get Random advice
- Open discord (if available on the system)
- Open notepad
- Open slack (if installed)
- Open Microsoft word and excel
- Opens calculator
- Opens Visual Studio Code