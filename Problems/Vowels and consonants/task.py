vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "y", "z"]

word = list(input())

for i in word:
    if i in vowels:
        print("vowel")
    elif i in consonants:
        print("consonant")
    else:
        break
