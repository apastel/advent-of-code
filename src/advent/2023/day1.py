from advent.load import read_input
import re

data = read_input(group=True)[0]

def calibrate(input_str: str) -> int:
    first = input_str[[x.isdigit() for x in input_str].index(True)]
    reverse_input_str = input_str[::-1]
    last = reverse_input_str[[x.isdigit() for x in reverse_input_str].index(True)]
    concat = f"{first}{last}"
    return int(concat)

print(sum([calibrate(line) for line in data]))

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
    match_spelled_num = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine))", input_str)
    
    try:
        first_index_digit = [x.isdigit() for x in input_str].index(True)
    except:
        first_index_digit = None
    if (match_spelled_num): #this is a list now
        first_index_spelled_num = input_str.find(match_spelled_num[0])
        if (first_index_digit == None or first_index_spelled_num < first_index_digit):
            first = mapping.get(match_spelled_num[0])
        else:
            first = input_str[first_index_digit]
    else:
        first = input_str[first_index_digit]

    reverse_input_str = input_str[::-1]
    try:
        last_index_digit = [x.isdigit() for x in reverse_input_str].index(True)
        last_index_digit = abs(last_index_digit - (len(reverse_input_str) - 1))
    except:
        last_index_digit = None
    if (match_spelled_num):
        last_index_spelled_num = input_str.rfind(match_spelled_num[-1])
        if (last_index_digit == None or last_index_spelled_num > last_index_digit):
            last = mapping.get(match_spelled_num[-1])
        else:
            last = input_str[last_index_digit]
    else:
        last = input_str[last_index_digit]

    concat = f"{first}{last}"
    return int(concat)

print(sum([calibrate2(line) for line in data]))