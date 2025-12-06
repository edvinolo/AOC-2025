def read_input(path):
    numbers = []
    with open(path,'r') as f:
        for lin in f:
            line = lin.split()
            if line[0] == '+' or line[0] == '*':
                ops = line
            else:
                numbers.append(line)

    # print(line_0)
    # print(ops)

    nums = []
    for j in range(len(numbers[0])):
        num = []
        for i in range(len(numbers)):
            num.append(int(numbers[i][j]))
        nums.append(num)

    return [nums,ops]

def read_input_two(path):
    lines = []
    with open(path,'r') as f:
        for lin in f:
            lin = lin[:-1]
            line = lin[::-1]
            lines.append(line)

    N_num = len(lines)-1

    # for line in lines[:N_num]:
    #     print(line)

    ops = lines[-1].split()

    nums = []
    num_list = []
    empty = N_num*' '
    for j in range(len(lines[0])):
        num = ''
        for i in range(N_num):
            num += lines[i][j]
        if num == empty:
            nums.append(num_list)
            num_list = []
        else:
            num_list.append(int(num))

    nums.append(num_list)

    return [nums,ops]

def do_op(nums,op):
    if (op == '+'):
        res = 0
        for num in nums:
            res += num
    else:
        res = 1
        for num in nums:
            res *= num
    return res

def part_one(inp):
    res = 0

    for nums,op in zip(inp[0],inp[1]):
        res += do_op(nums,op)

    return res

path = 'input.txt'
inp = read_input(path)
print(f'part one: {part_one(inp)}')

inp_2 = read_input_two(path)
print(f'part two: {part_one(inp_2)}')