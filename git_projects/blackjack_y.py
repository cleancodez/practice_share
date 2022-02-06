import random

#BLACKJACK or 21 
#THE PLANNING PHASE
#Dealer cards
dealer_cards = []

#Player cards
player_cards = []

#Deal the cards
#Dealer cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has |X|,", dealer_cards[1])
        

#Player_cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("Player cards:", player_cards)
      
     
#Sum of the Player card
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to Stay or Hit? ")).lower()
    if action_taken == 'hit':
        player_cards.append(random.randint(1,11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards " , player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + "with ", player_cards)

        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You Win!")
            break
if sum(player_cards) > 21:
    print("You BUSTED! Dealer wins.")
elif sum(player_cards) == 21:
    print("You have BLACKJACK! |21| You win!!")


#Display the cards
#Sum of the Dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has Black Jack! Dealer wins Pot!")
elif sum(dealer_cards) > 21:
    print("Dealer has BUSTED!")
elif sum(dealer_cards) < 16:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 3:
        print("Dealer has", dealer_cards)
        if dealer_cards > 21:
            print("Dealer Busted! You Win")
        elif sum(dealer_cards) < 16:
            dealer_cards.append(random.randiint(1,11))
            if len(dealer_cards) == 4:
                pass
                



#Player bets from bankroll before turn
#Dealer matches bet
#Player and Dealer Start with 1000
#At the end of each round winner takes money
#If Push can bet again


if len(player_cards) != 2:
        player_bet = int(input("How much would you like to bet? "))
        
class Bankroll():
    def __init__(self, balance):

        self.balance = balance

    def bet(self, player_bet):
        self.balance +=  self.player_bet
        print("You won {}.". format(player_bet))

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print("You bet {}".format(self.balance))
        else:
            print("You do not have enough money.")



