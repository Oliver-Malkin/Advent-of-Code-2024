import re

with open("input.txt", "r") as file:
    data = file.read()

matches = re.findall("mul\([1-9]\d*\,[1-9]\d*\)", data)

total = 0

for match in enumerate(matches):
    numbers = match[1].strip("mul()").split(",")
    total += int(numbers[0]) * int(numbers[1])

print(total)
