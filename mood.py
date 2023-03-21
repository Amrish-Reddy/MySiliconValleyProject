import speech_recognition as sr
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from playsound import playsound

# initialize the speech recognition and sentiment analysis modules
r = sr.Recognizer()
sia = SentimentIntensityAnalyzer()

# listen for user's voice command
with sr.Microphone() as source:
    print("How are You Feeling today")
    audio = r.listen(source)

# recognize the user's voice command
text = r.recognize_google(audio)

# analyze the user's mood using sentiment analysis
polarity_scores = sia.polarity_scores(text)
if polarity_scores['compound'] > 0:
    mood = "positive"
elif polarity_scores['compound'] < 0:
    mood = "negative"
else:
    mood = "neutral"

# respond to the user based on their mood
if mood == "positive":
    print("Glad to hear that you're feeling positive!")
    
elif mood == "negative":
    response = input("I'm sorry to hear that. Would you like me to play some calming music? (yes/no) ")
    if response.lower() == "yes":
        playsound("Calming.mp3")
        print("I hope the music helps to improve your mood.")
    else:
        print("Alright. Is there anything else I can help you with?")
        
else:
    print("I see. Is there anything I can help you with?")
