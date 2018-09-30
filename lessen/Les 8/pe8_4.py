studentenCijferlijst = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
    gemiddelde_list = []
    for entry in studentencijfers:
        gemiddelde_list.append(round(sum(entry) / len(entry), 2))
    return gemiddelde_list


def gemiddelde_van_alle_studenten(studentencijfers):
    lengte = 0
    totaal = 0

    for entry in studentencijfers:
        lengte += len(entry)
        totaal += sum(entry)

    return round(totaal / lengte, 2)


print(gemiddelde_per_student(studentenCijferlijst))

print(gemiddelde_van_alle_studenten(studentenCijferlijst))
