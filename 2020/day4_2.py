import re

BIRTH_YEAR = "byr"
ISSUE_YEAR = "iyr"
EXPIRATION_YEAR = "eyr"
HEIGHT = "hgt"
HAIR_COLOR = "hcl"
EYE_COLOR = "ecl"
PASSPORT_ID = "pid"

required_fields = [
    BIRTH_YEAR,
    ISSUE_YEAR,
    EXPIRATION_YEAR,
    HEIGHT,
    HAIR_COLOR,
    EYE_COLOR,
    PASSPORT_ID
]

valid_eye_colors = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth"
]

def validate_passport(passport):
    # Must have all required fields
    for required_field in required_fields:
        if not any(required_field in field for field in passport):
            return False
    
    # Validate fields
    return validate_fields(passport)


def validate_fields(passport):
    for field in passport:
        field_name, value = field.split(":")
        
        if field_name == BIRTH_YEAR:
            if len(value) != 4 or int(value) < 1920 or int(value) > 2002:
                print(f"Found invalid birth year of {value}")
                return False

        if field_name == ISSUE_YEAR:
            if len(value) != 4 or int(value) < 2010 or int(value) > 2020:
                print(f"Found invalid issue year of {value}")
                return False

        if field_name == EXPIRATION_YEAR:
            if len(value) !=4 or int(value) < 2020 or int(value) > 2030:
                print(f"Found invalid expiration year of {value}")
                return False

        if field_name == HEIGHT:
            if value.endswith("cm"):
                num = int(value[:value.index("c")])
                if num < 150 or num > 193:
                    print(f"Found invalid height of {value}")
                    return False
            elif value.endswith("in"):
                num = int(value[:value.index("i")])
                if num < 59 or num > 76:
                    print(f"Found invalid height of {value}")
                    return False
            else:
                return False

        if field_name == HAIR_COLOR:
            if not re.search(r"^#(?:[0-9a-fA-F]{6})$", value):
                print(f"Found invalid hair color of {value}")
                return False

        if field_name == EYE_COLOR:
            if value not in valid_eye_colors:
                print(f"Found invalid eye color of {value}")
                return False

        if field_name == PASSPORT_ID:
           if not re.search(r"^(?:[0-9]{9})$", value):
                print(f"Found invalid passport id of {value}")
                return False 

    return True


if __name__ == "__main__":
    with open("2020/input/day4.txt") as f:
        lines = f.read().split("\n\n")
        lines = [line.replace("\n", ' ') for line in lines]
        passports = [[field for field in line.split()] for line in lines]
        valid_count = 0
        for passport in passports:
            if validate_passport(passport):
                valid_count += 1

    print(valid_count)