totaal = 0
aantal = 0

while True:
    getal = input("Geef een getal: ")
    if getal == '0':
        break
    else:
        totaal += int(getal)
        aantal += 1

print("Er zijn {} getallen ingevoerd, de som is: {}".format(aantal, totaal))
