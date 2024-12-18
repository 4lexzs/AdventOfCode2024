# Program constants for opcodes
ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

# Initialize the registers with given values
registers = {"A": 22817223, "B": 0, "C": 0}

# Program (example input)
program = [2, 4, 1, 2, 7, 5, 4, 5, 0, 3, 1, 7, 5, 5, 3, 0]

# Instruction pointer starts at 0
instruction_pointer = 0

# List to collect output values
output_values = []

# Function to determine the value of combo operands
def combo_value(operand):
    if operand in range(0, 4):
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    else:
        raise ValueError("Invalid combo operand")

# Simulation loop to process the program
while instruction_pointer < len(program):
    opcode = program[instruction_pointer]
    operand = program[instruction_pointer + 1]
    
    # Execute instruction based on the opcode
    if opcode == ADV:  # adv: divide A by 2^combo_operand
        registers["A"] = registers["A"] // (2 ** combo_value(operand))
    elif opcode == BXL:  # bxl: bitwise XOR B with literal operand
        registers["B"] ^= operand
    elif opcode == BST:  # bst: store combo operand % 8 into B
        registers["B"] = combo_value(operand) % 8
    elif opcode == JNZ:  # jnz: jump if A is not zero
        if registers["A"] != 0:
            instruction_pointer = operand
            continue
    elif opcode == BXC:  # bxc: bitwise XOR B with C
        registers["B"] ^= registers["C"]
    elif opcode == OUT:  # out: output combo operand % 8
        output_values.append(combo_value(operand) % 8)
    elif opcode == BDV:  # bdv: divide A by 2^combo_operand and store in B
        registers["B"] = registers["A"] // (2 ** combo_value(operand))
    elif opcode == CDV:  # cdv: divide A by 2^combo_operand and store in C
        registers["C"] = registers["A"] // (2 ** combo_value(operand))
    else:
        raise ValueError(f"Invalid opcode: {opcode}")
    
    # Move to the next instruction (opcode and operand together)
    instruction_pointer += 2

# Join the collected output values into a string
output_string = ",".join(map(str, output_values))

# Print the solution
print("Solution 1:", output_string)