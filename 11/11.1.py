def parse_input() -> list[int]:
    INPUT = "11/input.txt"
    with open(INPUT) as file:
        stones: list[int] = []
        for line in file.read().splitlines():
            stones.extend([int(s) for s in line.split(" ")])
        return stones

def blink(stones) -> list[int]:
    new_stones: list[int] = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue

        stone_str = str(stone)
        stone_len = len(stone_str)
        if stone_len % 2 == 0:
            left = int(stone_str[: stone_len // 2])
            right = int(stone_str[stone_len // 2 :])
            new_stones.append(left)
            new_stones.append(right)
            continue

        new_stones.append(stone * 2024)
    return new_stones

def solution1():
    stones: list[int] = parse_input()
    for _ in range(25):
        stones = blink(stones)
    print(len(stones))

if __name__ == "__main__":
    solution1()