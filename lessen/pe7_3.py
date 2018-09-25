file = open("kaartnummers.txt")

print("Deze file telt {} regels".format(len(file.readlines())))

file.seek(0)

numberList = []

for line in file.readlines():
    kaartnummer, naam = line.split(',')
    # print(kaartnummer)
    numberList.append(kaartnummer)


highestNumber = max(numberList)

file.seek(0)

tempLineNumber = 1
lineNumber = 0

for line in file.readlines():
    if highestNumber in line:
        lineNumber = tempLineNumber
    else:
        tempLineNumber += 1

print("Het grootste kaartnummer is: {} en dat staat op regel {}".format(max(numberList), lineNumber))

file.close()
