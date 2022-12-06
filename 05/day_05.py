#!/usr/bin/env python3

with open("input.txt", "r") as f:
    lines = f.readlines()


def hasNum(string):
    return any(char.isdigit() for char in string)


def con(a, b, c):
    return (int(a), int(b), int(c))


linetrack = 0
stack_id = 0
matrix = []
for line in lines:
    row = []
    if hasNum(line):
        break
    while len(line) > 0:
        stack_id += 1
        crate = line[0:3].strip("[]").replace("   ", "#")
        row.append(crate)
        line = line[4:]
    matrix.append(row)
    linetrack += 1

steps = []
for line in lines[linetrack + 2:]:
    line = line.strip().replace(" ", ",").split(",")
    steps.append(con(line[1], line[3], line[5]))


def find_top(matrix, col):
    col -= 1
    row = 0
    for i in matrix:
        if i[col].isalpha():
            return (i[col], row)
        row += 1


new_matrix = []

# make empty columns
for row in matrix:
    new_matrix.append([])

cols = len(matrix[0])
n = 0

while n <= cols:
    if n < cols:
        for row in list(reversed(matrix)):
            if n == len(new_matrix):
                new_matrix.append([])
            new_matrix[n].append(row[n])
    n += 1
for i in new_matrix:
    while "#" in i:
        i.remove("#")

two_matrix = []
for i in new_matrix:
    two_matrix.append(i.copy())

for s in steps:
    for _ in range(s[0]):
        move = new_matrix[s[1] - 1].pop()
        new_matrix[s[2] - 1].append(move)

final = ""
for i in new_matrix:
    final = final + i.pop()

print(final)

for s in steps:
    pickem = []
    for _ in range(s[0]):
        pickem.append(two_matrix[s[1] - 1].pop())
    for p in list(reversed(pickem)):
        two_matrix[s[2] - 1].append(p)


final_two = ""
for i in two_matrix:
    final_two = final_two + i.pop()

print(final_two)
