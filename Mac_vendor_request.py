import requests
import urllib
import time
from sys import exit
from os.path import exists

class Mac_vendor_request:
    def __init__(self):

        # Create 2 variables, vendor dictionary is a dictionary of vendors and macadressess 
        # associated. mac_file_len will be used to count down remaining mac adresses.
        self.mac_file_len = 0
        self.vendor_dictionary = {}

        print("startup")
        # Reads the mac list text file and counts number of lines. with simplifies IO streams if no
        # MAC_list.txt then exit program.
        if exists('MAC_list.txt'):
            print("reading lines")
            with open('MAC_list.txt', 'r') as mf:
                self.mac_file_len = len(mf.readlines())
            print("finished reading lines")
        else:
            print("MAC_list.txt is missing.")
            exit()


        # Find self.mac_file document
        self.mac_file = open("MAC_list.txt", "r")

        # Create Vendor list document if one does not exist and open for writing.
        self.write_file = open("Vendor_list.txt", "w")

        # For loop that runs through each line of the MAC_list and creates a url and send request.
        for i in self.mac_file:
            self.url = "https://api.macvendors.com/" + urllib.parse.quote_plus(i)
            # takes the vendor bytes of the mac address from MAC_list and stores it as a string.
            self.vendor_mac = str(i[0:6])

            while True:

                # checks if vendor mac is already in vendor dictionary
                if self.vendor_mac in self.vendor_dictionary:
                    self.write_from_dictionary(i)
                    break
                # since it is not will query macvendors.
                else:
                    # sends get request to url.
                    self.send_request = requests.get(self.url)
                    # if 200 response, writes from get to both dictionary and write file.
                    if "200" in str(self.send_request):
                        self.write_from_get(i)
                        break
                    
                    # if 404 response, writes 404 to file.
                    elif "404" in str(self.send_request):
                        self.write_404(i)
                        break

                    # if website responds with any other request the program 
                    elif "429" in str(self.send_request):
                        print(str(self.send_request))
                        time.sleep(5)
                    
                    else:
                        response_choice = input("The following response was recieved:" + str(self.send_request) + "\nWould you like to " +
                            "(r)etry, (p)ass over or (e)xit program?")
                        if(response_choice == "r"):
                            print("retrying...")
                        elif(response_choice == "p"):
                            self.write_404(i)
                            break
                        elif(response_choice == "e"):
                            exit()
                        else:
                            "invalid input, retrying..."                        
                            
                                    
        # closes files for best practice
        self.mac_file.close()
        self.write_file.close()              

    def write_from_dictionary(self, i):
        # takes the mac address passsed through i if this address is already in list it will use 
        # the dictionary entry to write to Vendor_list file.
        print("writing from dictionary to list.")
        self.write_file.write(self.vendor_dictionary[self.vendor_mac] + ":" + i)
        print("written from dictionary to list.")
        self.mac_file_len -= 1
        print("Remaining:", self.mac_file_len)

    def write_from_get(self, i):
        # takes the mac address passed through i and pushes the vendor mac and vendor name into dictonary
        # as well as it writes the entry into the Vendor_list file.
        self.vendor_dictionary.update({self.vendor_mac:self.send_request.text})
        self.write_file.write(self.send_request.text + ":" + i)
        self.mac_file_len -= 1
        print(self.send_request.text)
        print(self.mac_file_len)
        time.sleep(1)

    def write_404(self,i):
        # takes mac address passed through i and writes 404 response to Vendor_list meaning that the
        # vendor mac is not recongized (no longer in use, fake, specifically made?).
        self.write_file.write(str(self.send_request)+":"+ i)
        self.mac_file_len -= 1
        print(str(self.send_request))
        print(self.mac_file_len)
        time.sleep(1)


Mac_vendor_request()