required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

if __name__ == "__main__":
    with open("2020/input/day4.txt") as f:
        lines = f.read().split("\n\n")
        lines = [line.replace("\n", ' ') for line in lines]
        passports = [[field for field in line.split()] for line in lines]
        invalid_count = 0
        for passport in passports:
            for required_field in required_fields:
                if not any(required_field in field for field in passport):
                    invalid_count += 1
                    break
            for field in passport:
                field_name, value = field.split(":")
        
        print(len(passports) - invalid_count)