def ticker(filename):
    file = open(filename)
    fileRead = file.readlines()
    file.close()

    tickers = {}

    for line in fileRead:
        bedrijf, afkorting = line.split(':')
        tickers[bedrijf] = afkorting.strip('\n')

    return tickers

# Versie 2
inputvalue = input("Enter a company name or a ticker symbol: ")

for item in ticker("ticker_symbols.txt").items():
    if inputvalue == item[0]:
        print("Ticker name: {}".format(item[1]))
    elif inputvalue == item[1]:
        print("Company name: {}".format(item[0]))




# Versie 1
# companyinput = input("Enter Company Name: ")
#
# for item in ticker("ticker_symbols.txt").items():
#     if companyinput in item:
#         print("Ticker symbol: {}\n".format(item[1]))
#
# tickerinput = input("Enter Ticker Symbol: ")
#
# for item in ticker("ticker_symbols.txt").items():
#     if tickerinput in item:
#         print("Company name: {}".format(item[0]))


