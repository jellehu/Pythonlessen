def inlezen_beginstation(stations):
    while True:
        beginInput = input("Wat is je beginstation? ")

        if beginInput in stations:
            return beginInput


def inlezen_eindstation(stations, beginstation):
    while True:
        eindInput = input("Wat is je eindstation? ")

        if eindInput in stations:
            if stations.index(eindInput) > stations.index(beginstation):
                return eindInput
            else:
                print("{} ligt niet op de route.".format(eindInput))
        else:
            print("Deze trein komt niet in {}.".format(eindInput))


def omroepen_reis(stations, beginstation, eindstation):
    beginstationIndex = stations.index(beginstation) + 1
    eindstationIndex = stations.index(eindstation) + 1
    kaartprijs = (eindstationIndex - beginstationIndex) * 5
    tussenstationsRange = range(beginstationIndex, eindstationIndex - 1)

    print("Het beginstation {} is het {}e station in het traject.".format(beginstation, beginstationIndex))
    print("Het eindstation {} is het {}e station in het traject.".format(eindstation, eindstationIndex))
    print("De afstand bedraagt {} station(s).".format(eindstationIndex - beginstationIndex))
    print("De prijs van het kaartje is {} euro.".format(kaartprijs))
    print()
    print("Jij stapt in de trein in: {}".format(beginstation))

    for i in tussenstationsRange:
        print(" - {}".format(stations[i]))

    print("Jij stapt uit in: {}".format(eindstation))


stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal",
            "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard",
            "Maastricht"]
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
