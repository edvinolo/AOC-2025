def read_input(path):
    lines = []
    with open(path, 'r') as f:
        for line in f:
            lines.append(line[:-1])

    #print(lines)

    return lines

def part_one(lines):
    res = 0
    N = len(lines[0])
    N_lines = len(lines)
    beams = N*[False]
    beams_tmp = N*[False]
    # print(beams)

    for i,c in enumerate(lines[0]):
        if c == 'S': beams[i] = True
    # print(beams)

    for i in range(1,N_lines-1):
        for j,c in enumerate(lines[i]):
            if beams[j]:
                if c == '^':
                    beams_tmp[j+1] = True
                    beams_tmp[j-1] = True
                    beams_tmp[j] = False
                    res += 1
                else:
                    beams_tmp[j] = True
        beams = beams_tmp

    # print(beams)

    return res

def part_two(lines):
    res = 0
    N = len(lines[0])
    N_lines = len(lines)
    beams = N*[0]
    # print(beams)

    for i,c in enumerate(lines[0]):
        if c == 'S': beams[i] = 1
    # print(beams)

    for i in range(1,N_lines-1):
        for j,c in enumerate(lines[i]):
            if beams[j]:
                if c == '^':
                    beams[j+1] += beams[j]
                    beams[j-1] += beams[j]
                    beams[j] -= beams[j]
                else:
                    beams[j] = beams[j]

    res = sum(beams)

    return res

path = 'input.txt'

lines = read_input(path)
print(f'part one: {part_one(lines)}')
print(f'part two: {part_two(lines)}')