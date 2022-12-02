#!/usr/bin/env python3

# A == ROCK
# B == PAPER
# C == SCISSORS

# X == ROCK     == 1
# Y == PAPER    == 2
# Z == SCISSORS == 3

# WIN  == 6
# DRAW == 3
# LOSE == 0

raw_strat = []
strategy = []

class GameRound:
    def __init__(self, p_one, p_two):
        self.p_one = p_one
        self.p_two = p_two

    def play(self):
        match self.p_one():
            case self.p_one == "A":
                print("ROCK")
            case _:
                print(self.p_one)

with open('input.txt','r') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        raw_strat.append(line)

for r in raw_strat:
    game = GameRound(r[0],r[2])
    game.play()
