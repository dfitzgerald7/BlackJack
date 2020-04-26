from Player import Player 
from Deck import Deck

class Dealer(Player):

    def shouldHit(self):
        return self.total < 17

    def newHand(self):
        super().newHand()
        self.hit()


    def printCards(self):
        print("Dealer's cards are")
        super().printCards()

    

