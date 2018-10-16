import csv

with open('artikelen.csv') as file:
    reading = csv.DictReader(file, delimiter=';')
    hoogstePrijs = 0
    duursteArtikel = ''
    kleinsteVoorraad = 9999
    kleinsteVoorraadNummer = 0
    aantalProducten = 0

    for row in reading:
        prijs = float(row['Prijs'])
        voorraad = int(row['Voorraad'])

        if prijs > hoogstePrijs:
            hoogstePrijs = prijs
            duursteArtikel = row['Naam']

        if voorraad < kleinsteVoorraad:
            kleinsteVoorraad = voorraad
            kleinsteVoorraadNummer = row['Artikelnummer']

        aantalProducten += voorraad

    print("Het duurste artikel is {} en die kost {} Euro".format(duursteArtikel, hoogstePrijs))
    print("Er zijn slechts {} exemplaren in voorraad van het product met nummer {}".format(kleinsteVoorraad,
                                                                                           kleinsteVoorraadNummer))
    print("In totaal hebben wij {} producten in ons magazijn liggen".format(aantalProducten))
