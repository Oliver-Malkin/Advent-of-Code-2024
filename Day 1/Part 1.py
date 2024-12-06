import csv

a = []
b = []

with open('input.txt', newline='') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        a.append(int(row[0]))
        b.append(int(row[3]))

a.sort() # Now they are in order
b.sort()
dist = 0

for i in range(len(a)):
    dist += abs(a[i] - b[i])

print(dist)