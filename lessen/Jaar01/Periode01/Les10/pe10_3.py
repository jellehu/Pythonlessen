def code(invoerstring):
    for char in invoerstring:
        value = ord(char) + 3
        print(chr(value), end="")


code("RutteAlkmaarDen Helder")
