file = open("kaartnummers.txt")

for line in file.readlines():
    kaartInfo = line.strip('\n')
    kaartnummer, naam = kaartInfo.split(',')
    print(naam + " heeft kaartnummer: " + kaartnummer)

file.close()