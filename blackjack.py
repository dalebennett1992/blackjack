import random
import time

# Global variables

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
hit_stand = True

#Classes

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):

        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def adjust_for_ace(self):        
        adjust = ''
        while adjust.upper() != 'Y' and adjust.upper() != 'N':
            adjust = input("The value of an Ace can be 1 or 11. Would you like to change the value of your ace? (Y/N) \n Ace Current Value: {}".format(values['Ace']))

        if adjust.upper() == 'Y':
            if values['Ace'] == 11:
                values['Ace'] = 1
            else:
                values['Ace'] = 11
        else:
            pass

    def add_card(self,card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.adjust_for_ace()
        else:
            pass
        self.value += values[card.rank]

    def first_deal_add (self,card):
        self.cards.append(card)
        self.value += values[card.rank]

class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Functions that are not restricted to a class

def take_bet(chips):

    player_bet = None
    player_bet_valid = False

    while player_bet_valid == False:
        try:
            player_bet = int(input('\n' * 100 + 'Please place your bet. \n'))
        except ValueError:
            print (" \n Invalid input, please input an integer value. \n")
            time.sleep(3)
        else:
            if player_bet > chips.total:
                print (" \n You have insufficient chips to place this bet. You have {} chips remaining. \n".format(chips.total))
                player_bet = None
            else:
                print ("\n Thank you. Your bet is {} \n".format(player_bet))
                player_bet_valid = True
    return player_bet

def start_game_deal(player, dealer, deck):
    player.first_deal_add(deck.deal())
    dealer.first_deal_add(deck.deal())
    player.first_deal_add(deck.deal())
    dealer.first_deal_add(deck.deal())
    

def hit(deck,hand):

    hand.add_card(deck.deal())


def hit_or_stand(deck,hand):

    global hit_stand

    hit_stand_decision = None

    while hit_stand_decision != 1 and hit_stand_decision != 2:

        try:
            print ('\n' * 100)
            hit_stand_decision = int(input("Would you like to hit or stand? Choose from the options below. \n 1: Hit \n 2: Stand"))

        except ValueError:
            print ("Please input the integer 1 or 2 only.")

        else:
            if hit_stand_decision == 1:
                print ("Chose to hit")
                hit(deck,hand)
            elif hit_stand_decision == 2:
                print ("Chose to stand")
                hit_stand = False
                break
            else: 
                hit_stand_decision = None
                print ('\n' * 100)
                print ("You have entered an invalid number. Please choose 1 (Hit) or 2 (Stand)")
                time.sleep(5)


def show_some(player, dealer):
    
    player_hand_string = ''
    dealer_hand_string = '????'
        
    for card in player.cards:
        player_hand_string += '\n' + card.__str__() 
        
    for card in dealer.cards[1:]:
        dealer_hand_string += '\n' + card.__str__() 

    print ('\n' * 100 + "Player's hand is: \n {} \n \nThe dealers hand is: \n{} \n \n".format(player_hand_string,dealer_hand_string))



def show_all():

    player_hand_string = ''
    dealer_hand_string = ''
        
    for card in player.cards:
        player_hand_string += card.__str__() + ', '
        
    for item in dealer.cards:
        dealer_hand_string += card.__str__() + ' ,'

    print ("Dealer's hand is: \n {} \n Players hand is: \n {}".format(player_hand_string, dealer_hand_string))

#Game outcomes

def player_busts(player, dealer, chips):

        print ("BUST, you lost {}".format(chips.bet))
        dealer_wins(player, dealer, chips)
        playing = False

def player_wins(player, dealer, chips):
    
    chips.win_bet()
    print ("You won. {} has been added to your chips. You now have {} chips.".format(chips.bet, chips.total))
    time.sleep(5)
        
        
def dealer_busts(player, dealer, chips):
    if dealer.value > 21:
        print ('\n' * 100 + 'Dealer BUST')
        player_wins(player, dealer, chips)


def dealer_wins(player, dealer, chips):
    chips.lose_bet()
    print ("You lose! {} has been deducted from your chips. You now have {} chips".format(chips.bet, chips.total))

def play_again():
    
    global playing 
    play_again = ''

    while play_again.upper() != 'Y' and play_again.upper() != 'N':

        play_again = input("Would you like to play again? (Y/N): ")
    
    if play_again.upper() == 'Y':
        print ("Chose to play again")
        return True
    elif play_again.upper() == 'N':
        print ("Chose to exit game")
        playing = False
        return False
    else:
        print ("Error")
    
       

            
    



 

        