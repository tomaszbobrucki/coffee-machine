word = list(input())

for i in range(int(len(word) / 2)):
    if word[i] != word[len(word) - i - 1]:
        print("Not palindrome")
        break
else:
    print("Palindrome")
