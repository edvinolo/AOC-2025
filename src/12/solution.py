def read_input(path):
    rects = []
    nums = []
    with open(path,'r') as f:
        for lin in f:
            line = lin.split()
            rects.append([int(line[0][:2]),int(line[0][3:-1])])
            tmp = [int(x) for x in line[1:]]
            nums.append(tmp)

    return rects,nums

def part_one(rects,nums):
    res = 0

    for rect,num in zip(rects,nums):
        if rect[0]*rect[1] >= 9*sum(num):
            res += 1

    return res

path = 's_input.txt'

rects,nums = read_input(path)

print(f'part one: {part_one(rects,nums)}')