from pathlib import Path

def read_input() -> tuple[list[int], list[int]]:
    # Read the input data
    input_data = Path("01/input1.txt").resolve().read_text().strip()
    left_list: list[int] = []
    right_list: list[int] = []

    # Parse the input data
    for line in input_data.split("\n"):
        num1, num2 = line.split("   ")
        left_list.append(int(num1))
        right_list.append(int(num2))

    return left_list, right_list

def solution1() -> None:
    left_list, right_list = read_input()

    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Calculate the total distance
    distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

    print(distance)

if __name__ == "__main__":
    solution1()
