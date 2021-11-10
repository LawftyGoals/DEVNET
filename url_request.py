import requests

url = "https://cat-fact.herokuapp.com/facts"

response = requests.get(url)

responsedict = response.json()

print(responsedict)

for cat in responsedict:
    print("source:", cat["source"])




