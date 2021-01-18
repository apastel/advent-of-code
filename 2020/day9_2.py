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

def find_encryption_weakness(invalid_number, numbers):
    for idx, number in enumerate(numbers):
        for x in range(2, len(numbers) - idx):
            subset = numbers[idx:idx + x]
            if sum(subset) == invalid_number:
                return min(subset) + max(subset)


if __name__ == "__main__":
    with open("input/day9.txt") as f:
        numbers = [int(line) for line in f]
        for idx, number in enumerate(numbers):
            if idx < PREAMBLE_LENGTH:
                continue
            previous_set = numbers[idx - PREAMBLE_LENGTH:idx]
            if invalid_number := find_invalid_number(previous_set, number):
                print(find_encryption_weakness(invalid_number, numbers))
                exit()
                