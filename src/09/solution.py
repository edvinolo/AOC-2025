import numpy as np
import matplotlib.pyplot as plt

def read_input(path):
    points = []
    with open(path,'r') as f:
        for line in f:
            point = line.split(',')
            point = (int(point[0]),int(point[1]))
            points.append(point)

    points = np.array(points)

    return points

def area(a,b):
    return (np.abs(a[0]-b[0])+1)*(1+np.abs(a[1]-b[1]))

def corners(a,b):
    return [a,(b[0],a[1]),b,(a[0],b[1])]

class Edge:
    def __init__(self,a,b):

        self.vert = (a[0] == b[0])

        self.set_c_d(a,b)

        if self.vert:
            self.intersect = self. intersect_vert
            self.on_edge = self.on_vert
        else:
            self.intersect = self.intersect_hor
            self.on_edge = self.on_hor

    def set_c_d(self,a,b):
        if self.vert:
            if (a[1] < b[1]):
                self.c = a
                self.d = b
            else:
                self.c = b
                self.d = a
        else:
            if (a[0] < b[0]):
                self.c = a
                self.d = b
            else:
                self.c = b
                self.d = a

    def intersect_vert(self,point):
        return (point[0] < self.c[0]) and ((self.c[1] <= point[1]) and (point[1] < self.d[1]))

    def intersect_hor(self,point):
        return False

    def on_vert(self,point):
        return (point[0] == self.c[0]) and ((self.c[1] <= point[1]) and (point[1] <= self.d[1]))

    def on_hor(self,point):
        return (point[1] == self.c[1]) and ((self.c[0] <= point[0]) and (point[0] <= self.d[0]))

class F_Edge:
    def __init__(self,edge,center):
        self.vert = edge.vert

        self.c = [float(edge.c[0]),float(edge.c[1])]
        self.d = [float(edge.d[0]),float(edge.d[1])]

        if self.vert:
            self.c[1] += 0.1
            self.d[1] -= 0.1

            if center[0] < self.c[0]:
                self.c[0] -= 0.1
                self.d[0] -= 0.1
            else:
                self.c[0] += 0.1
                self.d[0] += 0.1

        else:
            self.c[0] += 0.1
            self.d[0] -= 0.1

            if center[1] < self.c[1]:
                self.c[1] -= 0.1
                self.d[1] -= 0.1
            else:
                self.c[1] += 0.1
                self.d[1] += 0.1



def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def edge_intersect(a,b):
    #if a == b:
    #    return False

    #if a.vert == b.vert:
    #   return False

    return intersect(a.c,a.d,b.c,b.d)

def share_vertex(a,b):
    return np.all(a.c==b.c) or np.all(a.c==b.d) or np.all(a.d==b.c) or np.all(a.d == b.d)

class Polygon:
    def __init__(self,points):
        self.edges = []
        self.construct(points)

    def construct(self,points):
        for i in range(points.shape[0]-1):
            self.edges.append(Edge(points[i],points[i+1]))
            #print(self.edges[i].vert)

        self.edges.append(Edge(points[-1],points[0]))

        self.points = points

    def inside(self,point):
        count_intersect = 0

        for edge in self.edges:
            if edge.on_edge(point):
                return True
            else:
                count_intersect += edge.intersect(point)

        # print(point,count_intersect)

        return count_intersect%2 == 1

    def edge_not_inside(self,edge):
        dx = (edge.d[0] - edge.c[0])
        dy = (edge.d[1] - edge.c[1])

        for i in range(1,21):
            x = edge.c[0] + i/21*dx
            y = edge.c[1] + i/21*dy
            point = (x,y)

            if not self.inside(point):
                return True

        return False

def valid(corn,shape):
    for corner in corn[1::2]:
        # print(corner,shape.inside(corner))
        if not shape.inside(corner):
            return False

    rect = Polygon(np.array(corn))

    center = [0.0,0.0]

    center[0] = (corn[0][0] + corn[2][0])/2
    center[1] = (corn[0][1] + corn[2][1])/2

    for i,re_edge in enumerate(rect.edges):
        re = F_Edge(re_edge,center)
        # print(i,re.c,re.d)
        if not (shape.inside(re.c) and shape.inside(re.d)):
           return False
        #if shape.edge_not_inside(re_edge):
        #    return False
        for edge in shape.edges:
            # print(edge_intersect(re_edge,edge),re_edge.c,re_edge.d,edge.c,edge.d)
            if edge_intersect(re,edge):
                # print(i,re.c,re.d,edge.c,edge.d)
                return False
                if share_vertex(re_edge,edge):
                    # print(':',shape.edge_not_inside(re_edge),re_edge.c,re_edge.d)
                    if shape.edge_not_inside(re_edge):
                        return False
                else:
                    return False
                #count += 1
                #if count > 2: return False

    for point in shape.points:
        if rect.inside(point):
            on_edge = False
            for re_edge in rect.edges:
                if re_edge.on_edge(point):
                    on_edge = True

            return on_edge



    return True

def plot_points(points):

    x = []
    y = []

    for point in points:
        x.append(point[0])
        y.append(-point[1])

    x.append(points[0][0])
    y.append(-points[0][1])

    fig, ax = plt.subplots()

    ax.plot(x,y)
    plt.show()
    return

def plot_rect(points,corner):

    x = []
    y = []

    for point in points:
        x.append(point[0])
        y.append(-point[1])

    x.append(points[0][0])
    y.append(-points[0][1])

    fig, ax = plt.subplots()

    ax.plot(x,y)

    x = []
    y = []

    for corn in corner:
        x.append(corn[0])
        y.append(-corn[1])

    x.append(corner[0][0])
    y.append(-corner[0][1])
    ax.plot(x,y)

    plt.show()
    return

def part_one(points):
    res = 0

    N_points = points.shape[0]

    for i in range(N_points):
        for j in range(i+1,N_points):
            ar = area(points[i],points[j])

            # print(ar,points[i],points[j])

            if ar > res: res = ar

    return res

def part_two(points):
    res = 0

    N_points = points.shape[0]

    shape = Polygon(points)

    for i in range(N_points):
        for j in range(i+1,N_points):
            ar = area(points[i],points[j])
            if ar > res:
                corn = corners(points[i],points[j])
                #print(corn)
                #print(ar,points[i],points[j],valid(corn,shape))
                # print(valid(corn,shape))
                # plot_rect(shape.points,corn)
                if valid(corn,shape):
                    res = ar


    return res

def print_test(points,outpath):
    N_points = points.shape[0]

    shape = Polygon(points)

    min_i = 10**8
    min_j = 10**8
    max_j = 0
    max_i = 0

    for point in points:
        if point[0] < min_i: min_i = point[0]
        if point[0] > max_i: max_i = point[0]
        if point[1] < min_j: min_j = point[1]
        if point[1] > max_j: max_j = point[1]

    with open(outpath,'w') as f:
        for j in range(min_j,max_j+1):
            string = ''
            for i in range(min_i,max_i+1):
                if shape.inside((i,j)):
                    string += 'x'
                else:
                    string += '.'
            #print(string)
            f.write(string+'\n')

    return


path = 'input.txt'
points = read_input(path)

plot_points(points)

if path == 'test_3.txt':
    print_path = 'print.txt'
    print_test(points,print_path)

print(f'part one: {part_one(points)}')
print(f'part two: {part_two(points)}')