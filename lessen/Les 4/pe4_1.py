cijferICOR = 7
cijferPROG = 8.5
cijferCSN = 7.8

gemiddelde = round((cijferCSN + cijferICOR + cijferPROG) / 3, 1)
beloning = (cijferCSN + cijferICOR + cijferPROG) * 30
overzicht = 'Mijn cijfers (gemiddeld een {}) leveren een beloning van \u20ac{} op!'.format(gemiddelde, beloning)
print(overzicht)

tekst = 'het nummer is {}'.format(gemiddelde)
