entries = open("2020/input/day2.txt", "r").readlines()
num_valid = 0
for entry in entries:
    rule, password = entry.split(":")
    rule_pos, rule_letter = rule.split(" ")
    rule_posA, rule_posB = [int(i) for i in rule_pos.split("-")]
    password = password.strip()
    if (password[rule_posA - 1] == rule_letter) ^ (password[rule_posB - 1] == rule_letter):
        print(entry)
        num_valid += 1
print(num_valid)