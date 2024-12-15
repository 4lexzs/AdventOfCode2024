from functools import lru_cache
from pathlib import Path
from typing import Callable

def read_input() -> list[tuple[int, list[int]]]:
    input_data: str = Path("07/input7.txt").resolve().read_text().strip()
    data: list[tuple[int, int, int]] = []
    for line in input_data.split("\n"):
        num1, line = line.split(":")
        num1 = int(num1)
        nums = list(map(int, line.strip().split(" ")))
        data.append((num1, nums))
    return data

def passes_test(
    test_result: int, nums: list[int], operators: list[Callable[[int, int], int]]
) -> bool:
    n: int = len(nums)
    @lru_cache(None)
    def dfs(index: int, current_result: int) -> bool:
        if index == n:
            return current_result == test_result
        if current_result > test_result and all(num > 0 for num in nums):
            return False
        next_num: int = nums[index]
        if any(
            dfs(index + 1, operator(current_result, next_num)) for operator in operators
        ):
            return True
        return False
    return dfs(1, nums[0])

def concatenate(left: int, right: int) -> int:
    return int(f"{left}{right}")

def solution2() -> None:
    input_data: list[tuple[int, list[int]]] = read_input()
    operators: list[Callable[[int, int], int]] = [
        lambda x, y: x + y,
        lambda x, y: x * y,
        concatenate,
    ]
    result: int = sum(
        test_result
        for test_result, nums in input_data
        if passes_test(test_result, nums, operators)
    )
    print(result)

if __name__ == "__main__":
    solution2()
