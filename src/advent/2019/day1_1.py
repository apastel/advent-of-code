import math
lines = open('day1.txt', 'r').readlines()
sum = 0
for line in lines:
    sum += math.floor(int(line) / 3) - 2
print(sum)