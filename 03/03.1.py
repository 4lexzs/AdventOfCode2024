import re
from pathlib import Path

def read_input() -> str:
    # Read the input data
    input_data: str = Path("03/input3.txt").resolve().read_text().strip()

    # Parse the input data
    return input_data.replace("\n", "")

def solution1() -> None:
    data: str = read_input()
    result = 0

    # Find the number of appearances in the text
    pattern = r"mul\((\d+),(\d+)\)"
    matches: list[str] = re.findall(pattern, data)

    for match in matches:
        num1, num2 = map(int, match)
        result += num1 * num2

    print(result)

if __name__ == "__main__":
    solution1()