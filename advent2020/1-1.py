import math

f = open("inputs\\day1.txt", "r")
xp = list(map(int, f.read().splitlines()))

for x in xp:
    for y in xp:
        if (x + y) == 2020:
            print(x, y, x*y)
            break
