import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "4bd096cb2bmsh3ef08159dc94b99p1b899cjsnfcb4dec5eb4e"  # Replace with your RapidAPI key
    }
response = requests.get(url, headers=headers)
print(response.json())
  
