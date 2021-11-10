
##################TASK1

def roomArea(width, length):
    print(width*length, "m^2")

roomArea(float(input("Width: ")),float(input("Length: ")))


###################TASK2
import random

infected = 100
carriers=[0,0,0,0]
dayNr = 0

while infected < 1000000:
    total_carriers = 0
    infection_rate = random.uniform(0.8,1.5)
    
    carrier_append = infection_rate*infected
    
    carriers.append(carrier_append)

    for i in carriers:
        total_carriers+=i
    
    infected += total_carriers

    print("Day:", dayNr, "- Number of infected:", str(int(infected)) + "\n".ljust(11) + "Total number of carriers:", str(int(total_carriers)))

    carriers.pop(0)
    dayNr+=1

    ###################TASK3

firewall_model = {"FPR-1010":650, "FPR-1120":1500, "FPR-1140":2200, "FPR-1150":3000}

locations = {1:100, 2:500, 3:1000, 4:2000}

for location in locations:
    for model in firewall_model:
        if locations[location]<firewall_model[model]:
            print("Location", location,"can use", model, "with", str(firewall_model[model]) + "Mbps")
            break

###################Bonus TASK

d1 = {
    1:{'name': 'Cambridge Business English Dictionary', 'color':'purple','pages':'947'},
    2:{'name': 'Oxford Dictionary of English', 'color':'blue','pages':'2112'},
    3:{'name': 'The Merriam-Webster Dictionary', 'color':'red','pages':'960'}}

pageQ = 0
dictnr = 0
dictName = ""

for dictionary in d1:
    dictPageQ = int(d1[dictionary]['pages'])
    if dictPageQ > pageQ:
        pageQ = dictPageQ
        dictnr = int(dictionary)
        dictName = d1[dictionary]['name']
    
print("Dictionary nr:", dictnr, "named: '" + dictName + "'", "has the highest quantity of pages at:", pageQ)