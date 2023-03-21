import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

movies = {
    "Avatar The Way of Water": ["Drama", "Crime"],
    "RRR": ["Drama", "Crime"],
    "Pushpa The Rise": ["Drama", "Crime"],
    "Dangal": ["Indian", "Drama"],
    "KGF" : ["Action","Drama"],
    "Bajrangi Bhaijaan": ["Indian", "Drama"],
    "Baahubali: The Beginning": ["Indian","Action","Fantasy"],
    "Baahubali 2: The Conclusion": ["Indian","Action","Drama","Fantasy"],
    "Titanic" : ["Romantic","Drama"]
}

tv_shows = {
    "Breaking Bad": ["Drama", "Crime"],
    "Game of Thrones": ["Fantasy", "Drama"],
    "Friends": ["Comedy"],
    "The Office": ["Comedy"],
    "Stranger Things": ["Sci-Fi", "Horror"],
    "The Crown": ["Drama", "History"],
    "Black Mirror": ["Sci-Fi", "Thriller"],
    "Narcos": ["Drama", "Crime"],
    "The Sopranos": ["Drama", "Crime"],
    "The Wire": ["Drama", "Crime"],
    "Sacred Games": ["Indian", "Thriller"]
}

def recommend_movie(genre):
    genre_movies = []
    for movie, genres in movies.items():
        if genre in genres:
            genre_movies.append(movie)
    if len(genre_movies) == 0:
        return "Sorry, we couldn't find any movies in that genre."
    else:
        return random.choice(genre_movies)

def recommend_tv_show(genre):
    genre_tv_shows = []
    for tv_show, genres in tv_shows.items():
        if genre in genres:
            genre_tv_shows.append(tv_show)
    if len(genre_tv_shows) == 0:
        return "Sorry, we couldn't find any TV shows in that genre."
    else:
        return random.choice(genre_tv_shows)

print("Welcome to the movie and TV show recommendation system!")
speak("Welcome to the movie and TV show recommendation system!")
print("What genre are you interested in? (Action, Comedy, Drama, Crime, Thriller, Indian, Fantasy, Romantic)")
speak("What genre are you interested in? (Action, Comedy, Drama, Crime, Thriller, Indian, Fantasy, Romantic)")
genre = input("Enter a genre: ")

movie_recommendation = recommend_movie(genre)
print("You should watch:", movie_recommendation)
speak("You should watch:"+movie_recommendation)

tv_show_recommendation = recommend_tv_show(genre)
print("You should watch:", tv_show_recommendation)
