import math
lines = open('day1.txt', 'r').readlines()

def calculate_fuel(x):
    fuel = math.floor(x / 3) - 2
    if (fuel <= 0):
        return 0
    else:
        return fuel + calculate_fuel(fuel)

def main():
    sum = 0
    for line in lines:
        sum += calculate_fuel(int(line))
    print(sum)

if __name__ == '__main__':
    main()