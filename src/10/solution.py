import queue
import numpy as np
import scipy.optimize as so

def read_input(path):
    lights = []
    buttons = []
    joltages = []
    with open(path,'r') as f:
        for line in f:
            lin = line.split()
            # print(lin)

            lights.append(parse_lights(lin[0][1:-1]))
            buttons.append(parse_buttons(lin[1:-1],len(lights[-1])))
            joltages.append(parse_joltages(lin[-1]))

    return lights, buttons, joltages

def parse_lights(light):
    res = len(light)*[False]
    for i,c in enumerate(light):
        if c == '#':
            res[i] = True

    return res

def parse_buttons(button,N_light):
    but = N_light*[False]
    N_but = len(button)

    res = np.zeros((N_but,N_light),dtype = bool)

    for i,buts in enumerate(button):
        for j in buts[1:-1].split(','):
            res[i][int(j)] = True

    # print(res)

    return res

def parse_joltages(joltage):
    res = []

    for jolt in joltage[1:-1].split(','):
        res.append(int(jolt))

    return res

def update(state,button):
    stat = [x for x in state[0]]
    res = [stat,state[1]]

    for i in range(len(state[0])):
        # print(state[0],button,state[0][i]^button[i])
        res[0][i] = state[0][i]^button[i]

    res[1] += 1

    return res

def update_joltage(state,button):
    stat = [x for x in state[0]]
    res = [stat,state[1]]

    for i in range(len(state[0])):
        # print(state[0],button,state[0][i]^button[i])
        res[0][i] += button[i]

    res[1] += 1

    return res

def search(lights,buttons):
    state = [len(lights)*[False],0]

    qu = queue.SimpleQueue()
    qu.put(state)

    visited = set()
    visited.add(tuple(state[0]))

    while(not qu.empty()):
        state = qu.get()
        # print(state,lights)
        if state[0] == lights:
            return state[1]

        for button in buttons:
            new_state = update(state,button)
            # print(button)
            if not (tuple(new_state[0]) in visited):
                visited.add(tuple(new_state[0]))
                qu.put(new_state)

def search_joltage(joltages,buttons):
    N_but = buttons.shape[0]

    b = np.array(joltages)
    A = buttons.T

    eq_constr = so.LinearConstraint(A=A,lb=b,ub=b)

    bounds = so.Bounds(lb=0)

    c = np.ones(N_but,dtype = int)
    integrality = np.ones_like(c)

    res = so.milp(c=c,constraints=eq_constr,integrality=integrality,bounds=bounds)

    return sum([round(i) for i in res.x])



def part_one(lights,buttons):
    res = 0

    for light, butts in zip(lights,buttons):
        res += search(light,butts)

    return res

def part_two(joltages,buttons):
    res = 0

    for jolt, butts in zip(joltages,buttons):
        res += search_joltage(jolt,butts)
        # print(res)

    return res

path = 'input.txt'
lights, buttons, joltages = read_input(path)

print(f'part one: {part_one(lights,buttons)}')
print(f'part one: {part_two(joltages,buttons)}')