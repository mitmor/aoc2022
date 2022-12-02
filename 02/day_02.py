# !/usr/bin/env python3

#  A == ROCK
#  B == PAPER
#  C == SCISSORS

#  X == ROCK     == 1
#  Y == PAPER    == 2
#  Z == SCISSORS == 3

#  WIN  == 6
#  DRAW == 3
#  LOSE == 0

raw_strat = []
strategy = []
scores = []


class GameRound:
    def __init__(self, p_one, p_two, meth):
        self.p_one = p_one
        self.p_two = p_two
        self.meth = meth
        self.score = 0

    #  Take your choice
    def play(self):
        if self.meth == 1:
            match self.p_two:
                case 'X':  # ROCK
                    self.points(1)
                    self.rock()
                case 'Y':  # PAPER
                    self.points(2)
                    self.paper()
                case 'Z':  # SCISSORS
                    self.points(3)
                    self.scissors()
                case _:
                    print('ERROR!')
            return(self.score)

        if self.meth == 2:
            match self.p_two:
                case 'X':  # LOSE
                    self.points(0)
                    self.lose()
                case 'Y':  # DRAW
                    self.points(3)
                    self.draw()
                case 'Z':  # WIN
                    self.points(6)
                    self.win()
                case _:
                    print('ERROR!')
            return(self.score)

    #  compare your choice to opponent
    def win(self):
        match self.p_one:
            case 'A':  # ROCK
                self.points(2)
            case 'B':  # PAPER
                self.points(3)
            case 'C':  # SCISSORS
                self.points(1)

    def lose(self):
        match self.p_one:
            case 'A':  # ROCK
                self.points(3)
            case 'B':  # PAPER
                self.points(1)
            case 'C':  # SCISSORS
                self.points(2)

    def draw(self):
        match self.p_one:
            case 'A':  # ROCK
                self.points(1)
            case 'B':  # PAPER
                self.points(2)
            case 'C':  # SCISSORS
                self.points(3)

    #  compare your choice to opponent
    def rock(self):
        match self.p_one:
            case 'A':  # ROCK
                self.points(3)
            case 'B':  # PAPER
                self.points(0)
            case 'C':  # SCISSORS
                self.points(6)

    #  compare your choice to opponent
    def paper(self):
        match self.p_one:
            case 'A':  # ROCK
                self.points(6)
            case 'B':  # PAPER
                self.points(3)
            case 'C':  # SCISSORS
                self.points(0)

    #  compare your choice to opponent
    def scissors(self):
        match self.p_one:
            case 'A':  # ROCK
                self.points(0)
            case 'B':  # PAPER
                self.points(6)
            case 'C':  # SCISSORS
                self.points(3)

    #  add points!
    def points(self, score):
        print(score)
        self.score += score


def tabulate(scores):
    final = 0
    for i in scores:
        final += i
    return final


with open('input.txt', 'r') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        raw_strat.append(line)


for r in raw_strat:
    game = GameRound(r[0], r[2], 2)
    scores.append(game.play())

print(tabulate(scores))
