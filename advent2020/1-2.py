import math

f = open("inputs\\day1.txt", "r")
xp = list(map(int, f.read().splitlines()))

for x in xp:
    for y in xp:
        for z in xp:
            if (x + y + z) == 2020:
                print(x, y, z, x*y*z)
                break