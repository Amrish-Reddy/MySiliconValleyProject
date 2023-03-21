import requests

# List of zodiac signs
zodiac_signs = ["aries", "taurus", "gemini", "cancer", "leo", "virgo",
                "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]

# Function to get horoscope for a given zodiac sign
def get_horoscope(sign):
    response = requests.post("https://aztro.sameerkumar.website/?sign=" + sign + "&day=today")
    data = response.json()
    return data['description']

# Loop through each zodiac sign and print their horoscope
for sign in zodiac_signs:
    print("Horoscope for " + sign.capitalize() + ":")
    print(get_horoscope(sign))
    print("***********************************")
