import random


def monopolyword():
    dubbelcounter = 1

    while dubbelcounter < 3:
        eerste = random.randrange(1, 7)
        tweede = random.randrange(1, 7)
        totaal = eerste + tweede

        if eerste == tweede:
            dubbelcounter += 1
            worp = "{} + {} = {} (dubbel)".format(eerste, tweede, totaal)
            print(worp)
        else:
            worp = "{} + {} = {}".format(eerste, tweede, eerste + tweede)
            print(worp)
            break

        if dubbelcounter == 3:
            worp = "{} + {} = (direct naar gevangenis)".format(eerste, tweede)
            print(worp)
            break


monopolyword()
