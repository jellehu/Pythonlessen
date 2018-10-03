cijfers = {'Jelle': 10.0,
           'Henk': 9.5,
           'Jaap': 7.3,
           'Karin': 5.8,
           'Sam': 8.3,
           'Kees': 8.0,
           'Mo': 3.9,
           'Emma': 9.2,
           'Jan': 9.1,
           'Jet': 1.0}

for naam, cijfer in cijfers.items():
    if float(cijfer) > 9.0:
        print("{} heeft een cijfer hoger dan 9, namelijk een {}".format(naam, cijfer))
