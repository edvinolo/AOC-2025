from queue import SimpleQueue

def read_input(path):
    adj_list = {}
    with open(path,'r') as f:
        for line in f:
            l = line.split()
            l[0] = l[0][:-1]
            adj_list[l[0]] = l[1:]

    # print(adj_list)

    return adj_list

def search(adj_list):
    state = 'you'
    res = 0

    qu = SimpleQueue()
    qu.put(state)

    # visited = set()
    # visited.add(state)

    while(not qu.empty()):
        state = qu.get()
        if state == 'out':
            res += 1
        else:
            for new_state in adj_list[state]:
                # if not (new_state in visited):
                #     visited.add(new_state)
                qu.put(new_state)

    return res

def update(state,new):
    res = [new,state[1],state[2]]

    if new == 'fft':
        res[2] = True
    elif new == 'dac':
        res[1] = True

    return res

class DFS_2:
    def __init__(self,adj_list):
        self.adj_list = adj_list
        self.cache = {}

    def DFS(self,state):
        # print(state)
        if state[0] == 'out':
            if state[1] and state[2]:
                return 1
            else:
                return 0

        res = 0
        for new in self.adj_list[state[0]]:
            new_state = tuple(update(state,new))
            if not (new_state in self.cache):
                tmp = self.DFS(new_state)
                self.cache[new_state] = tmp
                res += tmp
            else:
                res += self.cache[new_state]

        return res

def part_one(adj_list):
    res = search(adj_list)

    return res

def part_two(adj_list):
    G = DFS_2(adj_list)
    res = G.DFS(tuple(['svr',False,False]))

    return res

path = 'input.txt'
adj_list = read_input(path)
print(f'part one: {part_one(adj_list)}')

path = 'input.txt'
adj_list = read_input(path)
print(f'part two: {part_two(adj_list)}')