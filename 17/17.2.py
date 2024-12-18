import time
import re
import copy

def solution2():
    with open('17/input.txt', 'r') as f:
        data = f.read().rstrip().split("\n\n")

        program = list(map(int, re.findall(r'-?\d+', data[1])))

    values = copy.deepcopy(program)
    results = []
    find_solutions(values, program, 0, results, 1)
    
    if len(results):
        print(sorted(results)[0])

def find_solutions(values, program, a, results, level):
    val = values[-level]
    for i in range(0, 8):
        test = run_program(program, a + i, 0, 0, True)
        if test[0] == val:
            if level == len(values):
                results.append(a + i)
            elif level < len(values):
                find_solutions(values, program, (a + i) * 8, results, level + 1)

def run_program(prog, a, b, c, onetime=False):
    ip = 0
    output = []
    while ip < len(prog):
        opcode = prog[ip]
        operand = prog[ip + 1]
        match opcode:
            case 0:  # adv
                combo = get_combo(a, b, c, operand)
                a = a // (2 ** combo)
            case 1:  # bxl
                b = b ^ operand
            case 2:  # bst
                combo = get_combo(a, b, c, operand)
                b = combo % 8
            case 3:  # jnz
                if a == 0 or onetime:
                    return output
                else:
                    ip = operand
                    continue
            case 4:  # bxc
                b = b ^ c
            case 5:  # out
                output.append(b % 8)
            case 6:  # bdv
                combo = get_combo(a, b, c, operand)
                b = a // (2 ** combo)
            case 7:  # cdv
                combo = get_combo(a, b, c, operand)
                c = a // (2 ** combo)
        ip += 2
    return output

def get_combo(a, b, c, operand):
    if operand <= 3:
        return operand
    if operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        return 7

if __name__ == "__main__":
    solution2()