import re

with open("input.txt", "r") as file:
    data = file.read()

matches = re.findall(r"don't\(\)|do\(\)|mul\([1-9]\d*\,[1-9]\d*\)", data)
total = 0

enabled = True

for match in enumerate(matches):
    test_case = match[1]
    if test_case == "do()":
        enabled = True
    elif test_case == "don't()":
        enabled = False
    else:
        if enabled:
            numbers = test_case.strip("mul()").split(",")
            total += int(numbers[0]) * int(numbers[1])

print(total)
