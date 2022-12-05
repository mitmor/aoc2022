#!/usr/bin/env python3

tasks = []

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    assignments = []

    for line in lines:
        assignments.append(line.split(","))
    for a in assignments:
        tasks.append(
            [
                [int(i) for i in a[0].split("-")],
                [int(i) for i in a[1].split("-")],
            ]
        )


def part_one(task_list):
    dupes = []
    for pair in task_list:
        if min(pair[0]) >= min(pair[1]) and max(pair[0]) <= max(pair[1]):
            dupes.append([pair[0], pair[1]])
        elif min(pair[1]) >= min(pair[0]) and max(pair[1]) <= max(pair[0]):
            dupes.append([pair[0], pair[1]])
    return len(dupes)


def part_two(task_list):
    overlaps = []
    for pair in task_list:
        for i in range(min(pair[0]), max(pair[0]) + 1):
            if i in range(min(pair[1]), max(pair[1]) + 1):
                overlaps.append(pair)
                break
    return len(overlaps)


print(part_one(tasks))
print(part_two(tasks))
