def read_input(path):
    with open(path,'r') as f:
        line = f.readline()

    ranges = line.split(',')

    return ranges

def part_one(ranges):
    result = 0

    for ran in ranges:
        tmp = ran.split('-')
        start = int(tmp[0])
        end = int(tmp[1])

        for i in range(start,end+1):
            str_i = str(i)
            n = len(str_i)
            if n%2 == 0:
                if str_i[:n//2] == str_i[n//2:]:
                    result += i

    return result

def part_two(ranges):
    result = 0

    for ran in ranges:
        tmp  = ran.split('-')
        start = int(tmp[0])
        end = int(tmp[1])

        for i in range(start,end+1):
            str_i = str(i)
            n = len(str_i)
            valid = True
            for j in range(1,n//2+1):
                if n%j == 0:
                    broke = False
                    for k in range(1,n//j):
                        if str_i[:j] != str_i[k*j:(k+1)*j]:
                            broke = True
                            break
                    if k == n//j-1 and not broke:
                        valid = False
                        break
            if not valid:
                #print(str_i)
                result += i
    return result

ranges = read_input('input.txt')
res_1 = part_one(ranges)
res_2 = part_two(ranges)

print(res_1)
print(res_2)