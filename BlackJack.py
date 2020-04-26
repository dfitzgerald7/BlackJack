
from User import User 
from Dealer import Dealer
from time import sleep
class BlackJack():
    print("<================================================>")
    print("          Welcome to the Blackjack Table          ")
    print("<================================================>")

    user = User()
    dealer = Dealer()
    runBool=True 

    while runBool: 
        handOver=False
        user.newHand()
        dealer.newHand()
        dealerBool=True
        print("The dealer is showing: ")
        dealer.printCards()

        print("Your cards are: ")
        user.printCards()
        
        while not handOver:
            resp = ""
            while resp not in ["hit", "stay", "exit", "help"]:
               resp = input("Hit or Stay? \n => ").lower()

            if resp == "hit":
                user.hit()

            user.printCards()
            print("Your total : " + str(user.total))

            if resp == "stay":
                handOver= True

            if user.didBust():
                print("Busted")
                handOver=True
                dealerBool=False
            

            if resp == "exit":
                handOver=True
                runBool=False
        if dealerBool:
            print("Dealer's Total :" + str(dealer.total))
            while dealer.shouldHit():
                dealer.hit()
                print("Dealer hit: " + str(dealer.getLast()))
                sleep(2)
            print("The dealer's final total is " + str(dealer.total))
            if dealer.didBust(): 
                print("Dealer Busted")
                print("You Win")
            elif dealer.total < user.total:
                print("You had a higher hand")
                print("You Win")
            else:
                print("You lose")
        
        if input("Play again? \n => ").lower() != "yes":
            runBool=False

    print("Goodbye")
