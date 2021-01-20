if __name__ == "__main__":
    with open("input/day10.txt") as f:
        adapters = sorted([0] + [int(line) for line in f])
        adapters += [adapters[-1] + 3]
        one_jolt_diffs = 0
        three_jolt_diffs = 0
        for idx,val in enumerate(adapters):
            if idx >= len(adapters)  - 1:
                break
            diff = adapters[idx + 1] - val
            if diff == 1:
                one_jolt_diffs += 1
            elif diff == 3:
                three_jolt_diffs += 1
        print(one_jolt_diffs, three_jolt_diffs)
