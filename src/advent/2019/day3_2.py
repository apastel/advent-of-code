import numpy as np

f = open('input/day3.txt', 'r')
firstWire = f.readline().split(',')
secondWire = f.readline().split(',')

def plot(path):
    points = [(0,0)]
    for move in path:
        hop = (0,0)
        if move[0] == 'R':
            hop = (1,0)
        elif move[0] == 'U':
            hop = (0,1)
        elif move[0] == 'L':
            hop = (-1,0)
        elif move[0] == 'D':
            hop = (0, -1)
        for i in range(int(move[1:])):
            lastPoint = points[-1]
            newPoint = tuple(np.add(lastPoint, hop))
            points.append(newPoint)
    return points

def main():
    firstWirePoints = plot(firstWire)
    secondWirePoints = plot(secondWire)
    intersections = list(set(firstWirePoints) & set(secondWirePoints))
    stepCounts = []
    for point in intersections:
        stepCounts.append(firstWirePoints.index(point) + secondWirePoints.index(point))
    print(min(stepCounts[1:]))
    

if __name__ == '__main__':
    main()