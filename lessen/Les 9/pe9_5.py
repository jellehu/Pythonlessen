def namen():
    namenDict = {}

    while True:
        naam = input("Volgende naam: ")

        if naam == '':
            break
        elif naam in namenDict:
            aantal += 1
        else:
            aantal = 1

        namenDict[naam] = aantal

    for item in namenDict.items():
        if item[1] == 1:
            print("Er is {} student met de naam {}".format(item[1], item[0]))
        else:
            print("Er zijn {} studenten met de naam {}".format(item[1], item[0]))


namen()
