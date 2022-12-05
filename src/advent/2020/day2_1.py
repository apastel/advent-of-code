entries = open("input/day2.txt", "r").readlines()
num_valid = 0
for entry in entries:
    rule, password = entry.split(":")
    rule_count, rule_letter = rule.split(" ")
    rule_min, rule_max = rule_count.split("-")
    if password.count(rule_letter) >= int(rule_min) and password.count(rule_letter) <= int(rule_max):
        num_valid += 1
print(num_valid)