list = eval(input("Geef een lijst met minimaal 10 strings: "))

shortList = []

for entry in list:
    if len(entry) <= 4:
        shortList.append(entry)


print(shortList)


# ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]