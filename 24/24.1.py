def main(args):
    name = '24/input.txt'
    if args:
        name = args[0]
    with open(name) as inf:
        lines = inf.readlines()
    lines = [l.strip() for l in lines]

    values, operations = parse(lines)
    print('Part 1:', part1(values, operations))


def part1(values, operations):
    results = apply_operations(values, operations)
    return sum_zvalues(results)


def apply_operations(values, operations):
    mem = dict(**values)

    while True:
        did_operation = False

        for op in operations:
            if op[3] in mem:
                # already done
                continue
            if op[0] not in mem or op[2] not in mem:
                # dependent values not done yet
                continue

            mem[op[3]] = do_op(mem[op[0]], op[1], mem[op[2]])
            did_operation = True

        if not did_operation:
            break

    return mem


def do_op(left, op, right):
    if op == 'AND':
        return left and right
    if op == 'OR':
        return left or right
    if op == 'XOR':
        return left ^ right
    raise Exception()


def sum_zvalues(results):
    z_keys = sorted([
        k for k in results
        if k.startswith('z')
    ])[::-1]
    result = 0
    for k in z_keys:
        result <<= 1
        result += results[k]
    return result


def parse(lines):
    values = {}
    operations = []
    for line in lines:
        if ':' in line:
            name, rest = line.split(':')
            value = int(rest.strip())
            values[name] = value
        elif '->' in line:
            parts = line.split(' ')
            op = (parts[0], parts[1], parts[2], parts[4])
            operations.append(op)
    return (values, operations)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])