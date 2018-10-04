uurloon = input('Wat verdien je per uur: ')
aantal_uur = input('Hoeveel uur heb je gewerkt: ')

loon = eval(uurloon) * eval(aantal_uur)

print('{} uur werken levert {} Euro op'.format(aantal_uur, loon))
