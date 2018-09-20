leeftijd = int(input("Geef je leeftijd: "))
paspoortNL = input("Nederlands paspoort: ")

if leeftijd >= 18 and paspoortNL == 'ja':
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Helaas, je mag niet stemmen")