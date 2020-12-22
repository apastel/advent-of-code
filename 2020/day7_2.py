import pprint

def traverse(graph, node, outer_bag_count=1, current_bag_count=0):
    global total_bag_count
    if not graph[node]:
        return 0
    for color, quantity in graph[node]:
        current_bag_count += traverse(graph, color, quantity * outer_bag_count, current_bag_count)
        total_bag_count += quantity * outer_bag_count
    return total_bag_count

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
                    inner_bag_list.append((color[:color.index(" bag")], int(bag_count)))
            rules[outer_bag] = inner_bag_list

        # pprint.pprint(rules)
        total_bag_count = 0
        print(traverse(rules, "shiny gold"))