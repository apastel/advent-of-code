from anytree import Node, RenderTree, Walker
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
    # for pre, fill, node in RenderTree(nodes.get('COM')):
    #     print("%s%s" % (pre, node.name))
    w = Walker()
    path = w.walk(nodes.get('YOU'), nodes.get('SAN'))
    upwards = path[0]
    common = path[1]
    downwards = path[2]
    totalSteps = len(upwards) + 1 + len(downwards) - 3
    print(totalSteps)
if __name__ == '__main__':
    main()