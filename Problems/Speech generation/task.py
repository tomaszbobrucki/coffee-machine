number = input()

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for i in number:
    j = int(i)
    #  print(type(j))
    print(digits[j])
