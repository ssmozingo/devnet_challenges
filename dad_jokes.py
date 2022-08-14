import requests
import json
import random

print("Let's hear a Dad joke!\n")
choice = input("Would you like to use a search term?\nPlease type it now or hit the Enter button.\n")
if choice == "":
  url = "https://icanhazdadjoke.com/" 
  head = {"Accept":"application/json"}
  r = requests.get(url, headers=head)
  data = r.json()['joke']
  print(data)
else:
  url = "https://icanhazdadjoke.com/search?term=" + choice 
  head = {"Accept":"application/json"}
  r = requests.get(url, headers=head)
  max_jokes = r.json()['total_jokes']
  num = random.randrange(0,max_jokes)
  data = r.json()['results'][num]['joke']
  print(max_jokes)
  print(data)
