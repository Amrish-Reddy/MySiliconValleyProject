import requests
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """Function to speak the given text."""
    engine.say(text)
    engine.runAndWait()


API_KEY = "8f430f1640124ab3925cdde8d6bc9c59"
BASE_URL = "https://newsapi.org/v2/top-headlines"

parameters = {
    "apiKey": API_KEY,
    "pageSize": 24,
    "country": "in",
}

response = requests.get(BASE_URL, params=parameters)

if response.status_code == 200:
    data = response.json()
    articles = data["articles"]
    speak("4 minutes 24 headlines by Amrish Reddy")
    for article in articles:
        print(article["title"])
        speak(article["title"])
else:
    print("Failed to retrieve articles")
