f = open("inputs\\day2.txt", "r")
passwords = f.read().splitlines()
validpasswords = 0

for line in passwords:
    charrange, character, password = line.split()
    low, high = map(int, charrange.split('-'))
    validpasswords += password.count(character[0]) >= low and password.count(character[0]) <= high

print(validpasswords)