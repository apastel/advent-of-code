import itertools

if __name__ == "__main__":
    with open("input/day10.txt") as f:
        adapters = sorted([0] + [int(line) for line in f])
        adapters += [adapters[-1] + 3]
        count = 0
        print(len(adapters))
        for x in range(len(adapters) + 1):
            print(x)
            for combo in itertools.combinations(adapters, x):
                count += 1
        print(count)
        # optional_cnt = 0
        # for idx,val in enumerate(adapters):
        #     if idx >= len(adapters)  - 2:
        #         break
        #     diff = adapters[idx + 1] - val
        #     diff_next = adapters[idx + 2] - val
        #     if diff_next <= 3:
        #         optional_cnt += 1
        # print(f"{optional_cnt} adapters are optional")
        # print(f"total arrangements is 2 ** {optional_cnt} = {2 ** optional_cnt}")
