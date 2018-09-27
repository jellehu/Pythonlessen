def standaardprijs(afstandKM):
    kosten = 0
    if afstandKM > 0 and afstandKM <= 50:
        kosten = kosten + afstandKM * 0.80
    elif afstandKM > 50:
        kosten = kosten + 15
        kosten = kosten + afstandKM * 0.60
    else:
        kosten = 0
    return round(kosten, 2)

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)

    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == 1:
            prijs = prijs * 0.65
        else:
            prijs = prijs * 0.70
    else:
        if weekendrit == 1:
            prijs = prijs * 0.60
    return round(prijs, 2)

print(ritprijs(11, 0, 15))

