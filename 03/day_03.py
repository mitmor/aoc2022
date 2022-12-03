#!/usr/bin/env python3

# Lowercase have priorities 1-26
# Uppercase have priorities 27-52

# score offsets!
LO = 96
HI = 38

with open("input.txt", "r") as f:
    sacks = f.read().splitlines()


# PART ONE
# Split the stacks to get compartments
def sack_split(sacks):
    split = []
    total = 0
    for s in sacks:
        items = len(s) // 2
        split.append([s[0:items], s[items:]])

    for c in split:
        total += calculate(list(set(c[0]) & set(c[1]))[0])

    return total


# PART TWO
# Split the sacks into groups of 3 and find total priority
def group_split(sacks):
    groups = []
    total = 0
    while len(sacks) > 0:
        groups.append(sacks[0:3])
        del sacks[:3]

    for g in groups:
        total += calculate(list((set(g[0]) & set(g[1]) & set(g[2])))[0])
    return total


def calculate(item):
    if item.islower():
        return ord(item) - LO
    elif item.isupper():
        return ord(item) - HI


# Part One
print(sack_split(sacks))

# Part Two
print(group_split(sacks))
