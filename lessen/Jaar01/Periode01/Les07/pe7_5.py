def gemiddelde():
    randomSentence = input("Voer een willekeurige zin in: ")

    wordList = randomSentence.split()
    average = 0

    for word in wordList:
        average += len(word) / len(wordList)

    print(round(average, 2))


gemiddelde()
