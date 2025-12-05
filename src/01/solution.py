def read_input(path):
    dir = []
    dist = []
    with open(path,'r') as f:
        for line in f:
            dir.append(line[0])
            dist.append(int(line[1:]))
            if dir[-1] == 'L':
                dist[-1] = -dist[-1]

    #print(dir)
    #print(dist)
    return dir, dist

def count_part_1(dist,start):
    pos = start
    counter = 0

    for step in dist:
        pos = (pos+step)%100
        if pos == 0:
            counter += 1

    return counter

def count_part_2(dist,start):
    pos = start
    counter = 0

    for step in dist:
        for i in range(abs(step)):
            if (step < 0):
                pos -= 1
            else:
                pos += 1
            pos = pos%100
            if pos == 0:
               counter += 1
        #print(step,pos,counter)
    return counter

start = 50
dir, dist = read_input('input.txt')
counter_1 = count_part_1(dist,start)
counter_2 = count_part_2(dist,start)

print(counter_1)
print(counter_2)