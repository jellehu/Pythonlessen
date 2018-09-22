def kwadraten_som(grondgetallen):
    resultaat = 0
    for number in grondgetallen:
        if number >= 0:
            resultaat = resultaat + number ** 2
    return resultaat

print(kwadraten_som([4, 5, 3, -81]))