from tkinter import *
import requests
import xmltodict


def clicked():
    i = 0

    station = entry.get()
    auth_details = ('jellevandenbroek@gmail.com', '9rayag9ctbMXu1cEmaFkKed0O4IxVLmNgt84MwWCqBW2kLOs_jtQdA')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(station)
    response = requests.get(api_url, auth=auth_details)
    vertrekXML = xmltodict.parse(response.text)

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        if i == 5:
            break
        else:
            eindbestemming = vertrek['EindBestemming']
            vertrektijd = vertrek['VertrekTijd']
            treinSoort = vertrek['TreinSoort']
            spoorNummer = vertrek['VertrekSpoor']['#text']
            vertrektijd = vertrektijd[11:16]
            label = Label(master=root,
                          text='om {} vertrekt er een {} vanuit {} naar {} op spoor {}.'.format(vertrektijd,
                                                                                                treinSoort,
                                                                                                station,
                                                                                                eindbestemming,
                                                                                                spoorNummer),
                          height=2)
            label.pack()
            i += 1


root = Tk()

label = Label(master=root, text='Voer een stationsnaam in:', height=2)
label.pack()

entry = Entry(master=root)
entry.pack(padx=20, pady=10)

button = Button(master=root, text='Druk hier', command=clicked)
button.pack(padx=20, pady=10)

root.mainloop()
