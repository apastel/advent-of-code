def invert_dict(dic):
    new_dic = {}
    for key, value in dic.items():
        new_dic.setdefault(key, [])
        for element in value:
            new_dic.setdefault(element, []).append(key)
    return new_dic

def all_ancestors(graph, child, ancestors=[]):
    if not graph[child]:
        return []
    ancestors += graph[child]
    for parent in graph[child]:
        all_ancestors(graph, parent, ancestors)
    return set(ancestors)

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
                    inner_bag_list.append(color[:color.index(" bag")])
            rules[outer_bag] = inner_bag_list

        rules = invert_dict(rules)
        ancestor_colors = all_ancestors(rules, "shiny gold")
        print(ancestor_colors)
        print(len(ancestor_colors))