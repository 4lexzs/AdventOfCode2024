file_path = '19/input.txt'

with open(file_path, 'r') as file:
    content = file.read()

patterns_section, designs_section = content.strip().split("\n\n")
patterns = patterns_section.split(", ")
designs = designs_section.split("\n")

def count_ways_with_dp(patterns, design):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[-1]

solution_2 = sum(count_ways_with_dp(patterns, design) for design in designs)

print(solution_2)