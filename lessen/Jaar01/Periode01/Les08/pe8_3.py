invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

result = invoer.split('-')
result.sort()

print("Gesorteerde list van ints: {}".format(result))
print("Grootste getal: {} en Kleinste getal: {}".format(max(result), min(result)))
print("Aantal getallen: {} en Som van de getallen: {}".format(len(result), sum(map(int, result))))
print("Gemiddelde: {}".format(sum(map(int, result)) / (len(result))))
