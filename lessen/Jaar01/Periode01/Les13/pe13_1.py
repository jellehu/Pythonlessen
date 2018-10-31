import xmltodict


def processXML(filename):
    with open(filename) as myXMlFile:
        content = myXMlFile.read()
        xmldict = xmltodict.parse(content)
        return xmldict


artikelendict = processXML("artikelen.xml")
artikelen = artikelendict['artikelen']['artikel']

for artikel in artikelen:
    print(artikel['naam'])
