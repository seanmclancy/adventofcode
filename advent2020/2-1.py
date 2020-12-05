f = open("inputs\\day2.txt", "r")
passwords = f.read().splitlines()
validpasswords = 0

for line in passwords:
    charrange, character, password = line.split(' ')
    low, high = charrange.split('-')
    if password.count(character[0]) >= int(low) and password.count(character[0]) <= int(high):
        validpasswords += 1

print(validpasswords)
    