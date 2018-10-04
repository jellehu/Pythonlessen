def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.extend(['d', 'e', 'f'])


lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)

# 1. Omdat de lijst al bestaat als ['a', 'b', 'c'].
# 2. Nee, want een string is immutable.
# 3. De opdracht laat zien dat de list te wijzigen is en de string niet.