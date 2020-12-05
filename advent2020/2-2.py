f = open("inputs\\day2.txt", "r")
passwords = f.read().splitlines()
validpasswords = 0

for line in passwords:
    charrange, character, password = line.split(' ')
    low, high = charrange.split('-')
    if (password[int(low)-1] == character[0] and password[int(high)-1] != character[0]) or(password[int(high)-1] == character[0] and password[int(low)-1] != character[0]):
        validpasswords += 1

print(validpasswords)
    