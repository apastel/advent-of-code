from advent.load import read_input

nested_list = [line.split("   ") for line in read_input()]
left_list = sorted([int(sublist[0]) for sublist in nested_list])
right_list = sorted([int(sublist[1]) for sublist in nested_list])

distance = 0
for i, _ in enumerate(left_list):
    distance += abs(left_list[i] - right_list[i])

print(distance)

similarity_score = 0
for i, _ in enumerate(left_list):
    similarity_score += left_list[i] * right_list.count(left_list[i])

print(similarity_score)