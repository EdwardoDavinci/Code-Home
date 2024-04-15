import string
from wordle_words import words


alphabet = list(string.ascii_lowercase)
letterCount = {}

for letter in alphabet:
    letterCount[letter] = 0

letterFrequency = {}
for letter in alphabet:
    letterFrequency[letter] = 0

for word in words:
    for char in word:
        letterCount[char] += 1

#  Sorting and ordering letters by Frequency
for letter in letterFrequency:
    letterFrequency[letter] = "{:.2f}".format(letterCount[letter] / len(words))

# print(letterFrequency)
orderedFrequency = sorted(letterFrequency.items(), key=lambda x: x[1], reverse=True)
# print(orderedFrequency)
for letter, frequency in orderedFrequency:
    print(f"{letter}: {frequency}")


def wordscore(word, letterFrequency):
    score = 0
    duplicateletter = {}
    for letter in alphabet:
        duplicateletter[letter] = False
    for letter in word:
        if duplicateletter[letter] == False:
            score += letterFrequency[letter]
            duplicateletter[letter] = True
    return score


for letter in letterFrequency:
    letterFrequency[letter] = float(letterFrequency[letter])

wordscores = {}
for word in words:
    wordscores[word] = 0
    wordscores[word] = wordscore(word, letterFrequency)

orderedWords = sorted(wordscores.items(), key=lambda x: x[1], reverse=True)
# print(wordscores)
# print(orderedWords)
num = 1
for word, score in orderedWords[0:10]:
    print(f"{num}:{word}:{score}")
    num += 1
