import requests
import pyttsx3

# API key for OpenWeatherMap
API_KEY = "04042444e5b215ac5c9c75fc4efc6081"

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

# Initialize the pyttsx3 engine for text-to-speech
engine = pyttsx3.init()

def speak(text):
    """Function to speak the given text."""
    engine.say(text)
    engine.runAndWait()

def get_weather(city):
    """Function to get the weather for the given city."""
    # Make the API call to OpenWeatherMap
    url = BASE_URL.format(city, API_KEY)
    response = requests.get(url)

    print(response.text) # added line to print the response text

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data) # added line to print the JSON data

        # Extract the temperature and description from the response
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        # Speak the weather
        speak(f"The temperature in {city} is {temperature} degrees Celsius with {description}.")

    else:
        speak("Sorry, I couldn't find the weather for that city. Please try again.")

# Prompt the user for a city
city = input("Enter a city name: ")

# Get the weather for the city
get_weather(city)
