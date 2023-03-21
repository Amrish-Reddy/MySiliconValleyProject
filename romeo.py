import pyttsx3
import speech_recognition as sr
import wikipedia
import math
import datetime
import webbrowser
import sympy
from playsound import playsound
import random
import os
import re
import requests
import time
from pytube import YouTube
import json
import urllib.parse
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Romeo. How can I assist you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except:
        print("I didn't catch that. Could you please repeat?")
        return "None"
    return query

def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def arithmetic_operations():
                speak("What is the first number?")
                num1 = int(input("Enter first number: "))
                speak("What is the second number?")
                num2 = int(input("Enter second number: "))
                speak("What operation would you like to perform?")

                operation = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    operation.pause_threshold = 1
                    audio = operation.listen(source)

                    try:
                        query = operation.recognize_google(audio, language='en-in')
                        print(query)

                        if 'add' in query:
                            result = num1 + num2
                            speak(f"The sum of {num1} and {num2} is {result}")
                        elif 'subtract' in query:
                            result = num1 - num2
                            speak(f"The difference between {num1} and {num2} is {result}")
                        elif 'multiply' in query:
                            result = num1 * num2
                            speak(f"The product of {num1} and {num2} is {result}")
                        elif 'divide' in query:
                            result = num1 / num2
                            speak(f"The quotient of {num1} and {num2} is {result}")
                        else:
                            speak("Sorry, I didn't understand the operation.")
                    except:
                        speak("Sorry, I didn't catch that. Could you please repeat the operation?")

def joke():
    jokes = [
    "Why don't scientists trust atoms? Because they make up everything.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why did the chicken cross the playground? To get to the other slide.",
    "Why don't eggs tell jokes? Because they'd crack each other up.",
    "What do you get when you cross a snowman and a shark? Frostbite.",
    "Why do cows wear bells? Because their horns don't work.",
    "What do you call fake spaghetti? An impasta.",
    "Why can't you hear a pterodactyl in the bathroom? Because it has a silent pee.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why did the math book look so sad? Because it had so many problems!"
    ]
    speak(random.choice(jokes))

def ask_trivia():
    trivia = {
        "What is the capital of Spain?": "Madrid",
        "What is the smallest country in the world?": "Vatican City",
        "What is the largest mammal in the world?": "Blue Whale",
        "What is the highest mountain in Africa?": "Mount Kilimanjaro",
        "What is the national animal of Canada?": "Beaver",
        "Who wrote the novel 'Pride and Prejudice'?": "Jane Austen",
        "What is the largest organ in the human body?": "Skin",
        "What is the most abundant gas in the Earth's atmosphere?": "Nitrogen",
        "What is the largest planet in our solar system?": "Jupiter",
        "What is the world's biggest island?": "Greenland",
        "Who is known as the King of Cricket?": "Virat Kohli"
    }
    question = random.choice(list(trivia.keys()))
    speak(question)
    answer = input("Enter your answer: ")
    if answer.lower() == trivia[question].lower():
        print("Correct!")
    else:
        print("Incorrect. The answer is", trivia[question])
    
def translate(query, source, target):
    api_key = '47160e8b8bd7c1e52cb5'
    url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(query)}&langpair={source}|{target}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        return result['responseData']['translatedText']
    else:
        return 'Unable to translate the query.'

    
if __name__ == "__main__":
    greet()
    while True:
        query = take_command().lower()
        if 'youtube' in query:
            speak("Opening Youtube...")
            webbrowser.open("https://www.youtube.com/")
            speak("What should i search sir")
            query = take_command().lower()
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
        elif 'search' in query or 'information' in query:
            speak('What do you want me to search for?')
            search_query = take_command().lower()
            try:
                results = wikipedia.summary(search_query, sentences=10)
                speak("According to wikipedia")
                speak(results)
            except:
                speak('I am unable to find any information about that on wikipedia.')
        elif 'facebook' in query:
            speak("Opening Facebook...")
            webbrowser.open("https://www.facebook.com/")
        elif 'instagram' in query:
            speak("Opening Instagram...")
            webbrowser.open("https://www.instagram.com/")
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'quit' in query:
            speak("Goodbye!")
            quit()
        elif 'whitehat' in query:
            speak("Opening WhiteHat Junior.")
            webbrowser.open("https://code.whitehatjr.com/")
        elif "byju's" in query:
            speak("Opening Byju's.")
            webbrowser.open("https://learn.byjus.com/")
        elif 'prime' in query:
            speak("Opening Prime Video.")
            webbrowser.open("https://www.primevideo.com/")
        elif 'hotstar' in query:
            speak("Opening Disney plus Hotstar")
            webbrowser.open("https://www.hotstar.com/in")
        elif 'practice maths' in query:
            speak("Let's Practice Mathematics")
            webbrowser.open("https://byjus.com/learn/adaptive-questions/practice/22219")    
        elif 'buy' in query:
            speak("What Type of Item")
            query = take_command().lower()
            webbrowser.open("https://www.google.com/search?tbm=shop&hl=en&psb=1&ved=0CAAQvOkFahcKEwjYiJCIj-L9AhUAAAAAHQAAAAAQCg&q="+query)
        elif 'space' in query:
            speak("Research on Which Planet?")
            query = take_command().lower()
            webbrowser.open("https://solarsystem.nasa.gov/planets/"+query+"/overview/")
            if 'jupiter' in query:
                speak("Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, and slightly less than one one-thousandth the mass of the Sun. Jupiter is the third brightest natural object in the Earth's night sky after the Moon and Venus, and it has been observed since prehistoric times. It was named after Jupiter, the chief deity of ancient Roman religion.Jupiter is primarily composed of hydrogen, followed by helium, which constitutes a quarter of its mass and a tenth of its volume")
            if 'saturn' in query:
                speak("Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth.It has only one-eighth the average density of Earth, but is over 95 times more massive.Saturn's interior is most likely composed of a rocky core, surrounded by a deep layer of metallic hydrogen, an intermediate layer of liquid hydrogen and liquid helium, and finally, a gaseous outer layer. Saturn has a pale yellow hue due to ammonia crystals in its upper atmosphere")
            if 'uranus' in query:
                speak("Uranus is the seventh planet from the Sun. It is named after Greek sky deity Uranus (Caelus), who in Greek mythology is the father of Cronus (Saturn), a grandfather of Zeus (Jupiter) and great-grandfather of Ares (Mars). Uranus has the third-largest planetary radius and fourth-largest planetary mass in the Solar System. The planet is similar in composition to Neptune, and both have bulk chemical compositions which differ from those of the other two giant planets, Jupiter and Saturn (the gas giants). For this reason, scientists often distinguish Uranus and Neptune as ice giants.")
            if 'neptune' in query:
                speak("Neptune is the eighth planet from the Sun and the farthest known planet in the Solar System. It is the fourth-largest planet in the Solar System by diameter, the third-most-massive planet, and the densest giant planet. It is 17 times the mass of Earth, and slightly more massive than its near-twin Uranus. Neptune is denser and physically smaller than Uranus because its greater mass causes more gravitational compression of its atmosphere. Being composed primarily of gases and liquids, it has no well-defined solid surface. The planet orbits the Sun once every 164.8 years at an average distance of 30.1 astronomical units (4.5 billion kilometres; 2.8 billion miles). It is named after the Roman god of the sea and has the astronomical symbol ♆, representing Neptune's trident.")
            if 'earth' in query:
                speak("Earth is the third planet from the Sun and the only place known in the universe where life has originated and found habitability. While Earth may not contain the largest volumes of water in the Solar System, only Earth sustains liquid surface water, extending over 70.8% of the Earth with its ocean, making Earth an ocean world. Earth's polar regions currently retain most of all other water with large sheets of ice covering ocean and land, dwarfing Earth's groundwater, lakes, rivers and atmospheric water. Land, consisting of continents and islands, extends over 29.2% of the Earth and is widely covered by vegetation. Below Earth's surface material lies Earth's crust consisting of several slowly moving tectonic plates, which interact to produce mountain ranges, volcanoes, and earthquakes. Earth's liquid outer core generates the magnetic field that shapes the magnetosphere of Earth, largely deflecting destructive solar winds and cosmic radiation.Earth has an atmosphere, which shields Earth's surface from most meteoroids and UV-light, and has a composition of primarily nitrogen and oxygen")
            if 'mars' in query:
                speak("Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, larger only than Mercury. In the English language, Mars is named for the Roman god of war. Mars is a terrestrial planet with a thin atmosphere and has a crust primarily composed of elements similar to Earth's crust, as well as a core made of iron and nickel. Mars has surface features such as impact craters, valleys, dunes, and polar ice caps. Mars has two small, irregularly shaped moons, Phobos and Deimos.Some of the most notable surface features on Mars include Olympus Mons, the largest volcano and highest-known mountain in the Solar System, and Valles Marineris, one of the largest canyons in the Solar System.")
            if 'venus' in query:
                speak("")
            if 'mercury' in query:
                speak("")
            if 'pluto' in query:
                speak("")
        elif 'sunrisers hyderabad' in query:
            speak("Opening Sunrisers..")
            webbrowser.open("https://www.sunrisershyderabad.in/")
        elif 'rajasthan royals' in query:
            speak("Opening Rajasthan Royals..")
            webbrowser.open("https://www.rajasthanroyals.com/")
        elif 'BookMyShow' in query:
            speak("Book Your Show")
            webbrowser.open("https://in.bookmyshow.com")
        elif 'spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("https://open.spotify.com/")
        elif 'thunkable' in query:
            speak("Opening Thunkable...")
            webbrowser.open("https://thunkable.com/")
        elif 'firebase' in query:
            speak("Opening Google Firebase...")
            webbrowser.open("https://firebase.google.com/")
        elif 'codepen' in query:
            speak("Opening CodePen...")
            webbrowser.open("https://codepen.io/")
        elif 'adobe' in query:
            speak("Opening Adobe...")
            webbrowser.open("https://www.adobe.com/")
        elif 'amazon' in query:
            speak("Opening Amazon...")
            webbrowser.open("https://www.amazon.in/")
        elif 'flipkart' in query:
            speak("Opening Flipkart...")
            webbrowser.open("https://www.flipkart.com/")
        elif 'myntra' in query:
            speak("Opening Myntra...")
            webbrowser.open("https://www.myntra.com/")
        elif 'meesho' in query:
            speak("Opening Meesho...")
            webbrowser.open("https://meesho.com/")
        elif 'mood' in query:
            import mood
        elif 'job' in query:
            import job
        elif 'apple' in query:
            speak("Opening Apple...")
            webbrowser.open("https://www.apple.com/")
        elif 'google photos' in query:
            speak("Opening Google Photos...")
            webbrowser.open("https://photos.google.com/")
        elif 'google play' in query:
            speak("Opening Google Play Store...")
            webbrowser.open("https://play.google.com/store")
        elif 'google maps' in query:
            speak("Opening Google Maps...")
            webbrowser.open("https://maps.google.com/")
        elif 'google drive' in query:
            speak("Opening Google Drive...")
            webbrowser.open("https://drive.google.com/")
        elif 'google docs' in query:
            speak("Opening Google Docs...")
            webbrowser.open("https://docs.google.com/")
        elif 'google sheets' in query:
            speak("Opening Google Sheets...")
            webbrowser.open("https://sheets.google.com/")
        elif 'google slides' in query:
            speak("Opening Google Slides...")
            webbrowser.open("https://slides.google.com/")
        elif 'google meet' in query:
            speak("Opening Google Meet...")
            webbrowser.open("https://meet.google.com/")
        elif 'google calendar' in query:
            speak("Opening Google Calendar...")
            webbrowser.open("https://calendar.google.com/")
        elif 'google' in query:
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/")
        elif 'briefly about' in query:
            speak("Introducing Romeo, your very own AI-powered personal assistant. With just a few words, Romeo can help you with a wide range of tasks, making your life easier and more efficient.Need to know the weather forecast? Just ask Romeo and get real-time updates instantly. Want to stay up-to-date with the latest news? Romeo has got you covered with live news updates from around the world. And if you're curious about your horoscope or astrology information, Romeo can provide that too.But that's not all - Romeo can also recommend movies that are tailored to your taste, tell you interesting trivia, and even share some funny jokes to make you smile. And when it comes to cooking, Romeo can provide you with detailed recipe instructions so you can whip up a delicious meal in no time.With Romeo, you'll never forget an important event or task again. Romeo can set reminders and alarms to keep you on track throughout the day. And if you need to buy something online, Romeo can do that too with simple voice commands.Whether you need to perform arithmetic operations, convert currencies, or search Wikipedia, Romeo is always there to help. And with the ability to detect your mood and provide personalized recommendations, Romeo is more than just an assistant - it's a friend.So why wait? Give Romeo a try today and experience the future of personal assistance. With Romeo, you'll have a powerful ally that's always at your service. Say hello to the ultimate personal assistant with Romeo!")
        elif 'perfect square' in query:
            number = int(input("Enter a number: "))
            result = number * number
            print("The square of", number, "is", result)
        elif 'square root' in query:
            speak("What number do you want to find the square root of?")
            num_query = take_command().lower()
            try:
                    num = int(num_query)
                    result = math.sqrt(num)
                    speak(f"The square root of {num} is {result}")
            except:
                    speak("Sorry, I am unable to find the square root of that number")
        elif 'quote' in query:
            quotes = [
          "Believe you can and you're halfway there. -Theodore Roosevelt",
          "You miss 100% of the shots you don't take. -Wayne Gretzky",
          "Success is not final, failure is not fatal: it is the courage to continue that counts. -Winston Churchill",
          "It does not matter how slowly you go as long as you do not stop. -Confucius",
          "The only way to do great work is to love what you do. -Steve Jobs",
          "You are never too old to set another goal or to dream a new dream. -C.S. Lewis",
          "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. -Christian D. Larson",
          "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. -Albert Schweitzer",
          "Strive not to be a success, but rather to be of value. -Albert Einstein",
          "I have not failed. I've just found 10,000 ways that won't work. -Thomas Edison",
          "The only limit to our realization of tomorrow will be our doubts of today. -Franklin D. Roosevelt",
          "The future belongs to those who believe in the beauty of their dreams. -Eleanor Roosevelt",
          "If you want to lift yourself up, lift up someone else. -Booker T. Washington",
          "Happiness is not something ready made. It comes from your own actions. -Dalai Lama",
          "A journey of a thousand miles begins with a single step. -Lao Tzu",
          "Believe in yourself, take on your challenges, dig deep within yourself to conquer fears. Never let anyone bring you down. You got this. -Chantal Sutherland",
          "Be yourself; everyone else is already taken. -Oscar Wilde",
          "If you don't stand for something you will fall for anything. -Malcolm X",
          "The only true wisdom is in knowing you know nothing. -Socrates",
          "We are what we repeatedly do. Excellence, then, is not an act, but a habit. -Aristotle",
          "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. -Jimmy Dean",
          "The best way to predict the future is to invent it. -Alan Kay",
          "Do not go where the path may lead, go instead where there is no path and leave a trail. -Ralph Waldo Emerson",
          "You must be the change you wish to see in the world. -Mahatma Gandhi",
          "Let us sacrifice our today so that our children can have a better tomorrow. -A. P. J. Abdul Kalam",
          "We are what our thoughts have made us; so take care about what you think. Words are secondary. Thoughts live; they travel far. -Swami Vivekananda",
          "Persistence is very important. You should not give up unless you are forced to give up. -Elon Musk",
          "Success is not a good teacher, failure makes you humble. -Shah Rukh Khan",
          "The best way to find yourself is to lose yourself in the service of others. -Mahatma Gandhi",
          "The difference between ordinary and extraordinary is that little extra. -Jimmy Johnson"
          "Dream, dream, dream. Dreams transform into thoughts and thoughts result in action. -A. P. J. Abdul Kalam",
          "You have to dream before your dreams can come true. -A. P. J. Abdul Kalam",
          "In a gentle way, you can shake the world. -Mahatma Gandhi",
          "I am not afraid of storms, for I am learning how to sail my ship. -Louisa May Alcott",
          "Chase your dreams but always know the road that will lead you home again. -Tim McGraw",
          "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela",
          "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
            "If you're going through hell, keep going. -Winston Churchill",
            "If you want to make your dreams come true, the first thing you have to do is wake up. -J.M. Power",
            "The best revenge is massive success. -Frank Sinatra",
            "Success is not how high you have climbed, but how you make a positive difference to the world. -Roy T. Bennett",
            "Believe in yourself and you can change a whole world. -Vishwas Chavan",
            "Strength does not come from physical capacity. It comes from an indomitable will. -Mahatma Gandhi",
            "Success is not about how much money you make. It's about the difference you make in people's lives. -Michelle Obama",
            "The only person you are destined to become is the person you decide to be. -Ralph Waldo Emerson",
            "It's not the years in your life that count. It's the life in your years. -Abraham Lincoln",
            "The two most important days in your life are the day you are born and the day you find out why. -Mark Twain",
            "You can never cross the ocean until you have the courage to lose sight of the shore. -Christopher Columbus",
            "A winner is a dreamer who never gives up. -Nelson Mandela",
            "Be the change you wish to see in the world. -Mahatma Gandhi",
            "I would rather die of passion than of boredom. -Vincent Van Gogh",
            "The true test of leadership is how well you function in a crisis. -Brian Tracy",
            "Don't let yesterday take up too much of today. -Will Rogers",
            "Happiness is not the absence of problems, it's the ability to deal with them. -Steve Maraboli",
            "Do what you can, with what you have, where you are. -Theodore Roosevelt",
            "The future depends on what you do today. -Mahatma Gandhi",
            "Believe in your infinite potential. Your only limitations are those you set upon yourself. -Roy T. Bennett",
            "You never know how strong you are, until being strong is your only choice. -Bob Marley",
            "You can't build a reputation on what you are going to do. -Henry Ford",
            "A true entrepreneur is a doer, not a dreamer. -Nolan Bushnell",
            "The secret of success is to do the common thing uncommonly well. -John D. Rockefeller Jr.",
            "The successful warrior is the average man, with laser-like focus. -Bruce Lee",
            "I failed my way to success. -Thomas Edison",
            "If you don't like something, change it. If you can't change it, change your attitude. - Maya Angelou",
            "You can't use up creativity. The more you use, the more you have. - Maya Angelou",
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
            "Believe you can and you're halfway there. - Theodore Roosevelt"
            "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer"
            "If opportunity doesn't knock, build a door. - Milton Berle"
            "The best way to predict your future is to create it. - Abraham Lincoln"
            "Be the change you want to see in the world. - Mahatma Gandhi"
            "Do one thing every day that scares you. - Eleanor Roosevelt"
            "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela"
            "I am not a product of my circumstances. I am a product of my decisions. - Stephen Covey"
            "The only limit to our realization of tomorrow will be our doubts of today  - Franklin D. Roosevelt"
            "The best way to find yourself is to lose yourself in the service of others. - Mahatma Gandhi"
            "We must be the change we wish to see in the world. - Mahatma Gandhi"]
            quote = random.choice(quotes)
            print("Here's a inspirational quote for you:")
            print(quote)
        elif 'close tab' in query:
            pyautogui.hotkey("ctrl", "w")
        elif 'copy' in query:
            pyautogui.hotkey("ctrl", "c")
        elif 'paste' in query:
            pyautogui.hotkey("ctrl", "v")
        elif 'new tab' in query:
            pyautogui.hotkey("ctrl", "t")
        elif 'new window' in query:
            pyautogui.hotkey("ctrl", "n")
        elif 'horoscope' in query:
            import horoscope
        elif 'recipes' in query:
            import recipes
        elif 'movie' in query:
            import movie
        elif 'fitness' in query:
            import fitness
        elif 'reminder' in query:
            import reminder
        elif '√' in query:
            query.replace("square root")
        elif 'translate' in query:
            speak('What do you want me to translate?')
            translate_query = take_command().lower()
            speak('What is the source language?')
            source = take_command().lower()
            speak('What is the target language?')
            target = take_command().lower()
            translated_text = translate(translate_query, source, target)
            speak(f'The translated text is: {translated_text}')
            print(f'The translated text is: {translated_text}')
        elif 'location' in query:
            speak("Which location is it ?")
            query = take_command().lower()
            webbrowser.open("https://www.google.com/maps/search/"+query)
        elif 'type' in query:
            speak("Ok Sir")
            type_query = take_command().lower()
            pyautogui.write(type_query)
        elif 'flight' in query:
            import flight
        elif 'pythagorean theorem' in query:
            speak("In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.")
        elif 'pythagorean theorem' in query:
            speak("In a right-angled triangle, the square of the hypotenuse is equal to the sum of the squares of the other two sides.")
        elif "newton's law" in query:
            speak("First Law: An object at rest tends to stay at rest and an object in motion tends to stay in motion with the same speed and in the same direction unless acted upon by an external force. Second Law: The acceleration of an object is directly proportional to the force applied on it and inversely proportional to its mass. Third Law: For every action, there is an equal and opposite reaction.")
        elif 'einstein theory of relativity' in query:
            speak("Time dilation: Time passes more slowly in a moving reference frame than in a stationary one.Length contraction: Objects appear shorter in the direction of motion.Mass-energy equivalence: E = mc^2, where E is energy, m is mass, and c is the speed of light.")
        elif 'ramanujan formula' in query:
            speak("One of Ramanujan's most famous results is his formula for computing the number of partitions of an integer. This formula involves an infinite series and has been widely studied by mathematicians.Another important theorem attributed to Ramanujan is the Ramanujan–Nagell equation, which is an equation of the form x^2 + 7 = 2^n, where x, n are integers. This equation has been studied extensively in number theory and has connections to other areas of mathematics, including elliptic curves and modular forms.")
        elif 'cv raman formula' in query:
            speak("C.V. Raman's formula is a mathematical expression that describes the Raman Effect. It can be written as: λ' = λ + A(1-cosθ)where λ' is the scattered wavelength, λ is the incident wavelength, A is a constant related to the molecular properties, and θ is the angle between the incident and scattered beams.")
        elif 'trivia' in query:
            speak("Here you go to Trivia")
            speak("Welcome to Trivia Game")
            ask_trivia()
        elif 'dictionary' in query:
            import dictionary
        elif 'meditation' in query:
            import meditation
            webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DXcj8Mdu8qUVH")
        elif 'nattu nattu' in query:
            webbrowser.open("https://www.youtube.com/watch?v=OsU0CGZoV8E")
        elif 'natu natu' in query:
            webbrowser.open("https://www.youtube.com/watch?v=OsU0CGZoV8E")
        elif 'currency' in query:
            import currency
        elif 'weather' in query:
            import weather
        elif 'news' in query:
            import news_api
        elif 'cricket' in query:
            import cricket
        elif 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'joke' in query:
            joke()
            speak()
        elif 'calculate' in query:
            arithmetic_operations()
        elif 'say happy birthday' in query:
            speak("To Whom ?")
            query = take_command().lower()
            speak("Happy Birthday"+query)
        elif 'say hi' in query:
            speak("To Whom ?")
            query = take_command().lower()
            speak("Hi"+query)
        elif 'stop' in query or 'exit' in query or 'bye' in query:
            speak("Goodbye!")
            break
