if __name__ == "__main__":
    with open("2020/input/day6.txt") as f:
        lines = f.read().split("\n\n")
        lines = [line.replace("\n", ' ') for line in lines]
        answers = [[person for person in line.split()] for line in lines]
        total_sum = 0
        for group in answers:
            group_iter = iter(group)
            group_union = next(group_iter)
            while True:
                try:
                    group_union = set(group_union).union(set(next(group_iter)))
                except StopIteration:
                    break
            total_sum += len(group_union)
        print(total_sum)