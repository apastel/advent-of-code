from anytree import Node, RenderTree
import pprint
import copy


nodes = {
    'COM': Node("COM")
}

def countNodes(orbits):
    i = 0
    for orbit in orbits:
        orbits[i] = orbit.split(')')   
        i += 1
    return len(set([item for sublist in orbits for item in sublist]))

def process(orbits, count):
    while len(nodes) < count:
        for orbit in orbits:
            objects = orbit.split(')')
            if (objects[0] not in nodes):
                continue
            if (objects[1] not in nodes):
                node = Node(objects[1], parent=nodes.get(objects[0]))
                nodes[objects[1]] = node

def main():
    orbits = []
    with open('input/day6.txt') as temp_file:
        orbits = [line.rstrip('\n') for line in temp_file]
    count = countNodes(copy.deepcopy(orbits))
    process(orbits, count)
    # pprint.pprint(nodes)
    sum = 0
    for node in nodes.values():
        slashCount = str(node).count('/')
        if slashCount > 1:
            sum += str(node).count('/') - 1
    print(sum)
    # for pre, fill, node in RenderTree(nodes.get('COM')):
    #     print("%s%s" % (pre, node.name))
if __name__ == '__main__':
    main()