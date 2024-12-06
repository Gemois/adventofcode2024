import argparse
import re

def main(file):
    total_multiplication_result = 0
    enabled_instruction_multiplication_result = 0

    file = open(file, "r")       
    memory = file.read()
    file.close()

    for instruction in extract_instructions(memory):
        total_multiplication_result += executeInstruction(instruction)

    for instruction in ignore_disabled_memory(memory):
        enabled_instruction_multiplication_result += executeInstruction(instruction)

    print("Total multiplication result:", total_multiplication_result)
    print("Enabled instruction multiplication result:", enabled_instruction_multiplication_result)

def extract_instructions(memory):
    return re.findall(r"mul\(\d+,\d+\)", memory)

def ignore_disabled_memory(memory):
    enabled = True
    enabled_memory = []
    
    tokens = re.split(r"(do\(\)|don't\(\))", memory)
    
    for token in tokens:
        if "do()" in token:
            enabled = True
        elif "don't()" in token:
            enabled = False
        elif "mul(" in token and enabled:
            enabled_memory.extend(re.findall(r"mul\(\d+,\d+\)", token))

    return enabled_memory

def executeInstruction(instruction):
    numbers = instruction.replace("mul(", "").replace(")", "").split(",")
    return int(numbers[0]) * int(numbers[1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    main(args.file)
