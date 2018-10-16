try:
    kosten = 4356
    personen = eval(input("Hoeveel personen gaan er mee op reis? "))

    if personen < 0:
        raise ValueError

    prijs_pp = kosten / personen
    print(prijs_pp)
except ZeroDivisionError:
    print("Delen door nul kan niet!")
except ValueError:
    print("Negatieve getallen zijn niet toegestaan!")
except NameError:
    print("Gebruik cijfers voor het invoeren van het aantal!")
except:
    print("Onjuiste invoer")
