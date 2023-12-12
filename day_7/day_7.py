"""Day 7
Let's play some poker
"""
from collections import Counter
# from operator import __ge__,__le__,__gt__,__lt__,__eq__
# from itertools import product

all_cards = "AKQJT98765432"
card_order = dict((card,rank) for card,rank in zip(all_cards[::-1],range(1,len(all_cards)+1)))

class Hand():
    def __init__(self,cards,bet,card_order):
        self.cards = cards
        self.bet = bet
        self.card_vals = [card_order[i] for i in cards]
        self.breakdown = sorted([(times,card_rank) for (card_rank,times) in Counter(self.card_vals).most_common()],reverse=True)
        # Score hand per category
        self.sumrank = [0]*5
        for (times,card_rank) in self.breakdown:
            self.sumrank[5-times] += (14**times)*card_rank
    def __sub__(self, other):
        return [(i>j) for i,j in zip(self.sumrank,other.sumrank) if not(i==j==0)]
    #     # return [(pair1[0]>pair2[0]) or (pair1[0]==pair2[0] and pair1[1]>=pair2[1]) for pair1,pair2 in zip(self.breakdown,other.breakdown)]
    def __gt__(self,other):
        return True if not any(self-other) else False if all(self-other) else (self-other).index(True)<(self-other).index(False)
        return (self-other).index(True)<(self-other).index(False) or not any(self-other)
    #     # return True if all(self-other) else False if not any(self-other) else (self-other).index(True)<(self-other).index(False)
    def __eq__(self,other):
        return not sum(self-other)
    @property
    def asdict(self):
        return {"cards" : self.cards,
                "bet" : self.bet,
                "summary" : self.breakdown,
                "score" : self.sumrank}


with open("./day_7/day_7_1.txt") as f:
    games = f.readlines()
    hands = [Hand(game.split()[0],int(game.split()[1]),card_order) for game in games]

with open("./day_7/test_7_1.txt") as f:
    games = f.readlines()
    testhands = [Hand(game.split()[0],int(game.split()[1]),card_order) for game in games]


def part1(hands):
    return sum(((idx+1)*x.bet for idx,x in enumerate(sorted(hands))))

if __name__ == "__main__":
    print(f"Test 1: {part1(testhands)}")
    # for hand in testhands:
    #     print(hand.asdict)
    # print(testhands[1]-testhands[4])
    # print(f"Part 1: {part1(hands)}")
    