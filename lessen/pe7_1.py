def convert(tempCelcius):
    tempFahr = tempCelcius * 1.8 + 32
    return tempFahr


def table():
    print("\u00A0 F \t\tC")
    for i in range(-30, 41, 10):
        result = i * 1.8 + 32
        print(result, "\t", float(i))

print(convert(25))
print("\n")
print(table())