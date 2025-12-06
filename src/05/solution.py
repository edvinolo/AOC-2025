def read_input(path):
    ran_min = []
    ran_max = []
    ids = []
    with open(path,'r') as f:
        for line in f:
            if '-' in line:
                ran = line.split('-')
                ran_min.append(int(ran[0]))
                ran_max.append(int(ran[1]))
            elif line == '\n':
                pass
            else:
                ids.append(int(line))

    return ran_min,ran_max, ids

def union_overlap(first,second):
    fi_0 = ((second[0] <= first[0]) and (first[0] <= second[1]))
    fi_1 =  ((second[0] <= first[1]) and (first[1] <= second[1]))
    se_0 = ((first[0] <= second[0]) and (second[0] <= first[1]))
    se_1 =  ((first[0] <= second[1]) and (second[1] <= first[1]))
    if (fi_0 or fi_1) or (se_0 or se_1):
        return (min(first[0],second[0]),max(first[1],second[1]))
    else:
        return None

def part_one(ran_min,ran_max,ids):
    res = 0
    for id in ids:
        for mi,ma in zip(ran_min,ran_max):
            if (mi <= id) and (id <= ma):
                res += 1
                break

    return res

def part_two(ran_min,ran_max):
    intervals = set([(mi,ma) for mi,ma in zip(ran_min,ran_max)])

    overlap = True

    while(overlap):
        overlap = False
        tmp = set()
        for i,interv_i in enumerate(intervals):
            overlap_i = False
            for j, interv_j in enumerate(intervals):
                if i != j:
                    new_interv = union_overlap(interv_i, interv_j)
                    if new_interv:
                        overlap = True
                        overlap_i = True
                        tmp.add(new_interv)
            if not overlap_i:
                tmp.add(interv_i)
        intervals = tmp

    res = 0
    for interv in intervals:
        res += interv[1]-interv[0] + 1

    return res

ran_min,ran_max, ids = read_input('input.txt')

res = part_one(ran_min,ran_max,ids)
print(f'part one: {res}')

res = part_two(ran_min,ran_max)
print(f'part two: {res}')