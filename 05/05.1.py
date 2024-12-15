from collections import defaultdict, deque
from pathlib import Path

def read_input() -> tuple[list[tuple[int, int]], list[list[int]]]:
    # Read the input data
    input_data: str = Path("05/input5.txt").resolve().read_text().strip()

    # Parse the input data
    rules, updates = input_data.split("\n\n")
    rules: list[tuple[int, int]] = [
        (int(num1), int(num2))
        for rule in rules.split("\n")
        for num1, num2 in [rule.split("|")]
    ]
    updates: list[list[int]] = [
        list(map(int, update.split(","))) for update in updates.split("\n")
    ]

    return rules, updates

def update_is_valid(update: list[int], rules: list[tuple[int, int]]) -> bool:
    """Check if the update is valid according to the rules."""
    # Convert rules to a set for fast lookups
    rules_set = set(rules)

    seen = set()

    # Iterate through the update list
    for num in update:
        # Check for conflicts with previously seen elements
        for prev_num in seen:
            if (num, prev_num) in rules_set:
                return False

        # Add the current number to the set of seen elements
        seen.add(num)

    return True

def solution1() -> None:
    rules, updates = read_input()
    result = 0

    for update in updates:
        if update_is_valid(update, rules):
            result += update[len(update) // 2]

    print(result)

if __name__ == "__main__":
    solution1()
