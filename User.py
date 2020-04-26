from Player import Player
from Deck import Deck
class User(Player):

    def __init__(self):
        self.chips = 100 
        super().__init__()

    def newHand(self):
        super().newHand()
        self.hit()
        self.hit()

    def printCards(self):
        print("Your Cards are : ")
        super().printCards()
        print("===================")
