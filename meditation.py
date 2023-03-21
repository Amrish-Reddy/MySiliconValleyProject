import time
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def meditation_exercise():
    print("Find a comfortable position and close your eyes.")
    speak("Find a comfortable position and close your eyes.")
    time.sleep(5)
    print("Focus on your breath.")
    speak("Focus on your breath.")
    time.sleep(5)
    print("Inhale deeply through your nose, counting to four.")
    speak("Inhale deeply through your nose, counting to four.")
    time.sleep(4)
    print("Hold your breath for a count of four.")
    speak("Hold your breath for a count of four.")
    time.sleep(4)
    print("Exhale slowly through your mouth for a count of six.")
    speak("Exhale slowly through your mouth for a count of six.")
    time.sleep(6)
    print("Repeat for several breaths.")
    speak("Repeat for several breaths.")
    time.sleep(10)
    print("Slowly open your eyes and take a deep breath.")
    speak("Slowly open your eyes and take a deep breath.")
    
    
meditation_exercise()