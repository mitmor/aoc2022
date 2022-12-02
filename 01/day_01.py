#!/usr/bin/env python3

inventory = []


def get_totals(inv):
    summed = []
    for li in inv:
        total = 0
        for i in li:
            total = total + int(i)
        summed.append(total)
    return(summed)


def get_biggest(totals):
    top = []
    all_items = totals
    sums = 0
    while len(top) < 3:
        highest = 0
        for i in all_items:
            if i > highest:
                highest = i
        top.append(highest)
        all_items.remove(highest)
    for i in top:
        sums = sums + i
    return sums


with open('input.txt', 'r') as f:
    c = []
    for i in f.readlines():
        if i == '\n':
            inventory.append(c)
            c = []
        else:
            c.append(i.strip())

print(get_biggest(get_totals(inventory)))
