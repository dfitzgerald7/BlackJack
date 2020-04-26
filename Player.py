##########
# A generic player class that will 
#########

from Deck import Deck

class Player:

    def __init__(self):
        self.cards = [] 
        self.total = 0

    def newHand(self):
        self.cards = [] 
        self.total = 0

    def getCards(self):
        return self.cards

    def addCard(self, card):
        self.cards.append(card)

    def printCards(self):
        for i in range(len(self.cards)):
            print(" " + str(self.cards[i]))

    def hit(self):
        card = Deck.dealCard()
        self.addCard(card)
        total = self.total
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        else:
            total += card

        if total > 21 and "A" in self.cards: 
            total -= 10
        
        self.total = total

    def didBust(self):
        return self.total > 21

    def getLast(self):
        return self.cards[len(self.cards) - 1]
