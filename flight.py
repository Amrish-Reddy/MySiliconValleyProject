import requests
import pyttsx3

# Set up text-to-speech engine
engine = pyttsx3.init()

# Define a function to get flight information and speak it out loud
def speak_flight_info():
    # Set up the API endpoint and parameters
    endpoint = "https://opensky-network.org/api/states/all"
    params = {"lamin": 30.0, "lomin": -125.0, "lamax": 50.0, "lomax": -65.0}

    # Send a GET request to the API endpoint
    response = requests.get(endpoint, params=params)

    # Get the JSON data from the response
    data = response.json()

    # Get the first flight from the data and extract the relevant information
    first_flight = data["states"][0]
    icao24 = first_flight[0]
    callsign = first_flight[1]
    origin_country = first_flight[2]
    longitude = first_flight[5]
    latitude = first_flight[6]
    altitude = first_flight[7]
    velocity = first_flight[9]

    # Speak the flight information out loud
    engine.say(f"Flight {callsign} with ICAO 24-bit address {icao24} is currently flying over {origin_country} at {altitude} meters above sea level, with a velocity of {velocity} meters per second, at longitude {longitude} and latitude {latitude}.")
    engine.runAndWait()

# Call the function to retrieve and speak flight information
speak_flight_info()
