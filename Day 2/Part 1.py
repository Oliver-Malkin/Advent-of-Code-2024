with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\n")

total = len(data) # Number of reports

def check_safe(report: list):
    dec = 0 # Flags
    inc = 0
    report = list(map(int, report.split()))

    for j in range(len(report)-1):
        result = report[j]-report[j+1]

        if -3 <= result <= -1: # Safe
            inc = 1
        elif 1 <= result <= 3: # Safe
            dec = 1
        else:
            return False
        
        if inc == 1 and dec == 1: # Not safe
            return False
        
    return True

for i in enumerate(data):
    if not check_safe(i[1]):
        total -= 1

print(total)