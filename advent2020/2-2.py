f = open("inputs\\day2.txt", "r")
passwords = f.read().splitlines()
validpasswords = 0

for line in passwords:
    charrange, character, password = line.split()
    low, high = map(int, charrange.split('-'))
    validpasswords += ((password[low-1] == character[0]) + (password[high-1] == character[0])) == 1

print(validpasswords)
    