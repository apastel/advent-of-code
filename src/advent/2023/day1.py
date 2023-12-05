from advent.load import read_input

data = read_input(group=True)[0]

def calibrate(input_str: str) -> int:
    first = input_str[[x.isdigit() for x in input_str].index(True)]
    reverse_input_str = input_str[::-1]
    last = reverse_input_str[[x.isdigit() for x in reverse_input_str].index(True)]
    concat = f"{first}{last}"
    return int(concat)

# print(sum([calibrate(line) for line in data]))

mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def calibrate2(input_str: str) -> int:
    for x in mapping:
        input_str.find(x)
    first = any(x for x in input_str if mapping.get(x))
    last = any(x for x in input_str if mapping.get(x))
    concat = f"{first}{last}"
    print(concat)

for line in data:
    calibrate2(line)