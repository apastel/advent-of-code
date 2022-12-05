import itertools

entries = open("input/day1.txt", "r").readlines()
entries = [int(i) for i in entries]
for pair in itertools.combinations(entries, 2):
    if pair[0] + pair[1] == 2020:
        print(f"{pair[0]} + {pair[1]} = 2020")
        print(f"{pair[0]} * {pair[1]} = {pair[0] * pair[1]}")