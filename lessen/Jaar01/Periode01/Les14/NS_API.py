import requests
import xmltodict

while True:
    station = input("Voer een station in: ")

    try:
        auth_details = ('jellevandenbroek@gmail.com', '9rayag9ctbMXu1cEmaFkKed0O4IxVLmNgt84MwWCqBW2kLOs_jtQdA')
        api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(station)
        response = requests.get(api_url, auth=auth_details)
        vertrekXML = xmltodict.parse(response.text)

        print('Dit zijn de vertrekkende treinen vanaf station {}:'.format(station))

        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
            eindbestemming = vertrek['EindBestemming']
            vertrektijd = vertrek['VertrekTijd']
            treinSoort = vertrek['TreinSoort']
            spoorNummer = vertrek['VertrekSpoor']['#text']
            vertrektijd = vertrektijd[11:16]
            print('om {} vertrekt er een {} vanuit {} naar {} op spoor {}.'.format(vertrektijd, treinSoort, station, eindbestemming, spoorNummer))

        break
    except KeyError:
        print("Dit station bestaat niet, voer een geldig station in.\n")
