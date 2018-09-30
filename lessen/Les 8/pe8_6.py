aantalKluizen = 12
alleKluisnummers = []

for nummer in range(1, 13):
    alleKluisnummers.append(nummer)


def toon_aantal_kluizen_vrij():
    file = open("kluizen.txt")
    lengthFile = len(file.readlines())
    file.close()
    return "Er zijn nog {} kluizen vrij.".format(aantalKluizen - lengthFile)


def nieuwe_kluis():
    file = open("kluizen.txt")
    for line in file.readlines():
        kluisnummer, wachtwoord = line.split(';')
        alleKluisnummers.remove(int(kluisnummer))

    file.close()
    file = open("kluizen.txt", "a")

    if len(alleKluisnummers) > 0:
        nieuwKluisWachtwoord = input("Voer een wachtwoord in: ")
        file.write("\n{};{}".format(alleKluisnummers[0], nieuwKluisWachtwoord))
        file.close()
        return "U kunt nu kluis nummer {} gebruiken".format(alleKluisnummers[0])
    else:
        return "Er zijn helaas geen kluizen meer beschikbaar."


def kluis_openen():
    file = open("kluizen.txt")
    bestaat = False
    nummer = input("Voer uw kluisnummer in: ")
    code = input("Voer uw wachtwoord in: ")
    nummerEnCode = "{};{}".format(nummer, code)

    for line in file.readlines():
        value = line.strip("\n")
        if value == nummerEnCode:
            bestaat = True

    file.close()

    if bestaat == True:
        return "Uw kluis is nu geopend."
    else:
        return "Deze combinatie bestaat niet."


def kluis_teruggeven():
    file = open("kluizen.txt", "r")
    verwijderd = False
    nummer = input("Voer uw kluisnummer in: ")
    code = input("Voer uw wachtwoord in: ")
    nummerEnCode = "{};{}".format(nummer, code)
    readLines = file.readlines()

    file.close()
    file = open("kluizen.txt", "w")

    for line in readLines:
        value = line.strip("\n")
        if value == nummerEnCode:
            verwijderd = True
        else:
            file.write(line)

    file.close()
    file = open("kluizen.txt", "r")
    ereaseBlankLines = file.readlines()

    file.close()

    file = open("kluizen.txt", "w")

    for i, line in enumerate(ereaseBlankLines):
        value = line.strip("\n")
        if i == len(ereaseBlankLines) - 1:
            file.write(value)
        else:
            file.write(line)

    if verwijderd == True:
        return "Uw kluis is verwijderd uit de lijst."
    else:
        return "Deze combinatie bestaat niet."


while (1):
    print()
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")
    print("5: Ik wil stoppen")
    keuze = int(input("Maak een keuze: "))

    if keuze < 1 or keuze > 5:
        print("Voer een geldige waarde in")
    else:
        if keuze == 1:
            print(toon_aantal_kluizen_vrij())
        elif keuze == 2:
            print(nieuwe_kluis())
        elif keuze == 3:
            print(kluis_openen())
        elif keuze == 4:
            print(kluis_teruggeven())
        elif keuze == 5:
            print("Bezig met stoppen...")
            break
