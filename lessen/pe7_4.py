import datetime

while 1:
    file = open('hardlopers.txt', 'a')
    vandaag = datetime.datetime.today()
    dateAndTime = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    name = input("Geef de naam van de hardloper op: ")
    file.write("{}, {}\n".format(dateAndTime, name))
    file.close()
