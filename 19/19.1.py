file_path = '19/input.txt'

with open(file_path, 'r') as file:
    content = file.read()

patterns_section, designs_section = content.strip().split("\n\n")
patterns = patterns_section.split(", ")
designs = designs_section.split("\n")

def can_form_design(patterns, design):
    dp = [False] * (len(design) + 1)
    dp[0] = True  

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and dp[i - len(pattern)] and design[i - len(pattern):i] == pattern:
                dp[i] = True
                break

    return dp[-1]

solution_1 = sum(can_form_design(patterns, design) for design in designs)

print(solution_1)
