import datetime
import csv

bestand = 'inloggers.csv'

with open(bestand, 'a', newline='') as file:
    while True:
        writing = csv.writer(file, delimiter=';')
        naam = input("Wat is je achternaam? ")
        if naam == "einde":
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        print()
        dateAndTime = datetime.datetime.now().strftime("%a %d %b %Y at %H:%M")

        writing.writerow([dateAndTime, voorl, naam, gbdatum, email])
