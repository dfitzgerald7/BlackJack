
from random import randint

class Deck: 

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] 

    
    @staticmethod
    def dealCard():
        return Deck.cards[randint(0, len(Deck.cards) - 1)]


