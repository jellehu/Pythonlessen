def seizoen(maand):
    if maand >= 3 and maand <= 5:
        print("Lente")
    elif maand >= 6 and maand <= 8:
        print("Zomer")
    elif maand >= 9 and maand <= 11:
        print("Herfst")
    elif maand == 12 or maand <= 2 and maand > 0:
        print("Winter")
    else:
        print("Geen geldige waarde")


seizoen(1)
seizoen(3)
seizoen(5)
seizoen(7)
seizoen(9)
seizoen(11)
seizoen(13)
