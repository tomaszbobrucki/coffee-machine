word = input()

#  print(type(word))
new_word = ""

for letter in word:
    if letter.isupper():
        new_word += ("_" + letter.lower())
    else:
        new_word += letter

print(new_word)
