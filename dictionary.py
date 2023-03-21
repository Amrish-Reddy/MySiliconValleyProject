import requests
import json
import pyttsx3
import speech_recognition as sr

# initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    for string in text.split('\n'):
        engine.say(string)
        engine.runAndWait()

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = json.loads(response.text)

    try:
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        speak(f"The definition of {word} is: {definition}")
        print(f"The definition of {word} is:", definition)
    except:
        speak(f"Sorry, definition not found for the word {word}")
        print("Sorry, definition not found for the word:", word)

# main loop
r = sr.Recognizer()

while True:
    prompt = "Please say a word, or say 'exit' to quit: "
    speak(prompt)
    print(prompt)

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        word = r.recognize_google(audio)
        print(f"You said: {word}")
        if word == "exit":
            break
        else:
            get_definition(word.lower())
    except sr.UnknownValueError:
        speak("Sorry, I did not understand what you said")
    except sr.RequestError:
        speak("Sorry, my speech service is not available") 

speak("Goodbye!") 
