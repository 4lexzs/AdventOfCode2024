import re
from pathlib import Path

def read_input() -> str:
    # Read the input data
    input_data: str = Path("03/input3.txt").resolve().read_text().strip()

    # Parse the input data
    return input_data.replace("\n", "")

def solution2() -> None:
    data: str = read_input()
    result = 0
    enabled: bool = True  # Initially, `mul` instructions are enabled

    # Regex to match relevant instructions: mul(X,Y), do(), don't()
    mul_pattern = r"mul\((\d+),(\d+)\)"
    control_pattern = r"(do\(\)|don't\(\))"

    # Find all control and mul instructions
    instructions: list[str, str, str] = re.findall(
        f"{control_pattern}|{mul_pattern}", data
    )

    for control, num1, num2 in instructions:
        if control:
            # Handle `do()` and `don't()` instructions
            enabled = control == "do()"
        elif enabled:
            # Process `mul(X,Y)` instructions if enabled
            result += int(num1) * int(num2)

    print(result)

if __name__ == "__main__":
    solution2()