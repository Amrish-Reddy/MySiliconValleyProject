import requests
import json

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
    "X-RapidAPI-Key": "a88f99c074mshd36b4ade20d923fp177cc8jsn6c9d8ac76f23",
    "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
data = json.loads(response.text)

print(json.dumps(data, indent=4))
