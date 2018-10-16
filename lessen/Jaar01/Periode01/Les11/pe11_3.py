import csv

with open('scores.csv') as file:
    reading = csv.reader(file, delimiter=';')
    highestValue = 0

    for row in reading:
        value = int(row[-1])
        if value > highestValue:
            highestValue = value
            highestValuerow = row

    print("De hoogste score is: {} op {} behaald door {}".format(highestValuerow[2], highestValuerow[1], highestValuerow[0]))
