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
    def __sub__(self, other):
        return [(pair1[0]>pair2[0]) or (pair1[0]==pair2[0] and pair1[1]>=pair2[1]) for pair1,pair2 in zip(self.breakdown,other.breakdown)]
    def __gt__(self,other):
        return True if all(self-other) else False if not any(self-other) else (self-other).index(True)<(self-other).index(False)
    # def __eq__(self,other):
    #     return all(self-other)
    @property
    def asdict(self):
        return {"cards" : self.cards,
                "bet" : self.bet,
                "summary" : self.breakdown}


with open("./day_7/day_7_1.txt") as f:
    games = f.readlines()
    hands = [Hand(game.split()[0],int(game.split()[1]),card_order) for game in games]

def part1(hands):
    return sum(((idx+1)*x.bet for idx,x in enumerate(sorted(hands))))

if __name__ == "__main__":
    print(f"Part 1: {part1(hands)}")
    