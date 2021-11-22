import requests

while(True):
    # This while loop locks user into loop until they give an acceptable answer (1, 7, 30).
    hvilke_periode = input("Over hvilket tidsperiode (1, 7, 30 (dager)) ønsker du å se på Bitcoin endringene?: ")
    if hvilke_periode == "1":
        # ?timePeriod(number)((h)our or (d)ay) specifies the lenght of time
        time_period = "?timePeriod=24h"
        break
    elif hvilke_periode not in ["7", "30"]:
        print("Ikke gyldig tidsperiode")
        
    else:
        time_period = "?timePeriod=" + hvilke_periode + "d"
        break

# This URL is required to acces the correct coin API, Qwsogvtv82FCd is the id for Bitcoin.
url = "https://api.coinranking.com/v2/coin/Qwsogvtv82FCd"+time_period

# security token that allows access to API, is personal, taken from account on coinrank website.
token = {"x-access-token" : 
    "coinranking3daf47a74f483dca95aa0df799ae3bc794a561cdde594d70"}

# response is the pure response to the GET request sent from the program
response = requests.request("GET", url, headers = token)

# response is formated into jSON which is the same as a python dictionary, hence _dict
response_dict = response.json()

# statement prints out the change in the bitcoin value over the chosen periode hvilke_periode
print("Endringer i Bitcoin over den siste dagen:\n" if hvilke_periode == "1" else "Endringer i Bitcoin over de siste " + hvilke_periode + " dagene:\n" , str(response_dict["data"]["coin"]["change"]))