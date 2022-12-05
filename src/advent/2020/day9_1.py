import itertools

PREAMBLE_LENGTH = 25

def find_invalid_number(previous_set, number):
    invalid_number = True
    for pair in itertools.combinations(previous_set, 2):
        if pair[0] + pair[1] == number:
            invalid_number = False
            break
    if invalid_number:
        return number
    return False
    


if __name__ == "__main__":
    with open("input/day9.txt") as f:
        numbers = [int(line) for line in f]
        for idx, number in enumerate(numbers):
            if idx < PREAMBLE_LENGTH:
                continue
            previous_set = numbers[idx - PREAMBLE_LENGTH:idx]
            if invalid_number := find_invalid_number(previous_set, number):
                print(invalid_number)
                exit()
