import xmltodict


def processXML(filename):
    with open(filename) as myXMlFile:
        content = myXMlFile.read()
        xmldict = xmltodict.parse(content)
        return xmldict


stationsdict = processXML("stations.xml")
stations = stationsdict['Stations']['Station']

print("Dit zijn de codes en types van de 4 stations:")
for station in stations:
    print("{} - {}".format(station['Code'], station['Type']))
print()

print("Dit zijn alle stations met één of meer synoniemen:")
for station in stations:
    if station['Synoniemen'] != None:
        print("{} - {}".format(station['Code'], station['Synoniemen']['Synoniem']))
print()

print("Dit is de lange naam van elk station:")
for station in stations:
    print("{} - {}".format(station['Code'], station['Namen']['Lang']))
