from collections import defaultdict

def main(args):
    name = '24/input.txt'
    if args:
        name = args[0]
    with open(name) as inf:
        lines = inf.readlines()
    lines = [l.strip() for l in lines]

    values, operations = parse(lines)
    print('Part 2:', part2(values, operations))


def part2(values, operations):
    def is_input(operand):
        return operand[0] in 'xy'

    use_map = defaultdict(list)
    for op in operations:
        use_map[op[0]].append(op)
        use_map[op[2]].append(op)

    swapped = set()
    for operation in operations:
        left, op, right, result = operation
        if result == 'z45' or left == 'x00':
            continue

        if op == 'XOR':
            if is_input(left):
                if not is_input(right):
                    swapped.add(result)
                if result[0] == 'z' and result != 'z00':
                    swapped.add(result)
                usage = use_map[result]
                using_ops = [o[1] for o in usage]
                if result != 'z00' and sorted(using_ops) != ['AND', 'XOR']:
                    swapped.add(result)
            else:
                if result[0] != 'z':
                    swapped.add(result)

        elif op == 'AND':
            if is_input(left):
                if not is_input(right):
                    swapped.add(result)
            usage = use_map[result]
            if [o[1] for o in usage] != ['OR']:
                swapped.add(result)

        elif op == 'OR':
            if is_input(left) or is_input(right):
                swapped.add(result)
            usage = use_map[result]
            using_ops = [o[1] for o in usage]
            if sorted(using_ops) != ['AND', 'XOR']:
                swapped.add(result)

        else:
            print(operation, 'unknown op')

    return ','.join(sorted(swapped))


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