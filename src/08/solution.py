import numpy as np

def read_input(path):
    points = []
    with open(path,'r') as f:
        for line in f:
            point = line.split(',')
            point = [int(x) for x in point]
            points.append(point)

    pairs,dists = generate_sorted_pairs(points)

    return points,pairs,dists

def dist2(a,b):
    res = 0
    for i in range(len(a)):
        res += (a[i]-b[i])**2

    return res

def generate_sorted_pairs(points):
    pairs = []
    dists = []

    for i in range(len(points)):
        # pair_i = [x for x in points[i]]
        for j in range(i+1,len(points)):
            dists.append(dist2(points[i],points[j]))
            # pair = pair_i + [x for x in points[j]]
            pairs.append((i,j))

    pairs = np.array(pairs)
    dists = np.array(dists)
    ind = np.argsort(dists)
    dists = dists[ind]
    pairs = pairs[ind]

    return pairs,dists

class Circuit:
    def __init__(self):
        self.nodes = set()

    def add(self,points):
        self.nodes.add(points[0])
        self.nodes.add(points[1])

    def in_circ(self,points):
        a = (points[0] in self.nodes)
        b = (points[1] in self.nodes)
        return a or b

def part_one(pairs,dists,path):
    circuits = [Circuit()]

    if path == 'test.txt':
        limit = 10
    else:
        limit = 1000


    circuits[0].add(pairs[0])
    for i in range(1,limit):
        circ_exist = []
        for j,circ in enumerate(circuits):
            if circ.in_circ(pairs[i]):
                circ_exist.append(j)

        N_exist = len(circ_exist)
        if N_exist == 0:
            circuits.append(Circuit())
            circuits[-1].add(pairs[i])
        elif N_exist == 1:
            circuits[circ_exist[0]].add(pairs[i])
        elif N_exist == 2:
            circuits[circ_exist[0]].nodes = circuits[circ_exist[0]].nodes.union(circuits[circ_exist[1]].nodes)
            circuits.pop(circ_exist[1])


    circuits.sort(key=lambda x: len(x.nodes),reverse=True)

    res = 1
    for i in range(3):
        res *= len(circuits[i].nodes)

    return res

def part_two(points,pairs,dists):
    circuits = [Circuit()]

    N_points = len(points)
    N_pairs = len(pairs)
    res = 0


    circuits[0].add(pairs[0])
    for i in range(1,N_pairs):
        circ_exist = []
        for j,circ in enumerate(circuits):
            if circ.in_circ(pairs[i]):
                circ_exist.append(j)

        N_exist = len(circ_exist)
        if N_exist == 0:
            circuits.append(Circuit())
            circuits[-1].add(pairs[i])
        elif N_exist == 1:
            circuits[circ_exist[0]].add(pairs[i])
        elif N_exist == 2:
            circuits[circ_exist[0]].nodes = circuits[circ_exist[0]].nodes.union(circuits[circ_exist[1]].nodes)
            circuits.pop(circ_exist[1])

        for circ in circuits:
            # print(circ.nodes)
            if len(circ.nodes) == N_points:
                res = points[pairs[i][0]][0]*points[pairs[i][1]][0]
                return res

    return res


path = 'input.txt'

pts,pairs,dists = read_input(path)

print(f'part one: {part_one(pairs,dists,path)}')
print(f'part two: {part_two(pts,pairs,dists)}')