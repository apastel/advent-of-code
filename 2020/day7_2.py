import pprint

if __name__ == "__main__":
    with open("2020/input/day7.txt") as f:
        lines = f.readlines()
        rules = {}
        for line in lines:
            split_line = line.split(" bags contain ")
            outer_bag = split_line[0]
            inner_bags = split_line[1].split(",")
            inner_bag_list = []
            for bag in inner_bags:
                bag_count, color = bag.strip().split(" ", maxsplit=1)
                if bag_count != "no":
                    inner_bag_list.append((bag_count, color[:color.index(" bag")]))
            rules[outer_bag] = inner_bag_list

        pprint.pprint(rules)