import random

infected = 100
carriers=[0,0,0,0]
dayNr = 0

while infected < 1000000:
    total_carriers = 0
    infection_rate = random.uniform(0.8,1.5)
    
    carrier_append = infection_rate*infected
    infected += carrier_append
    
    carriers.append(carrier_append)

    for i in carriers:
        total_carriers+=i
    
    print("Day:", dayNr, "- Number of infected:", str(int(infected)) + "\n".ljust(11) + "Total number of carriers:", str(int(total_carriers)))

    carriers.pop(0)
    dayNr+=1











"""import requests

url = "https://cat-fact.herokuapp.com/facts"

response = requests.get(url)

responsedict = response.json()

print(responsedict)

for cat in responsedict:
    print("source:", cat["source"])




        while True:
        send_request = requests.get(url)
        if send_request ==
        """