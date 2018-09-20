leeftijd = int(input("Geef je leeftijd: "))
paspoortNL = input("Nederlands paspoort: ")

if leeftijd >= 18 and paspoortNL == 'Ja':
    print("Gefeliciteerd!")
    print("Met een score van {} ben je geslaagd!".format(leeftijd))
else:
    print("Helaas\nMet een score van {} ben je niet geslaagd.".format(leeftijd))