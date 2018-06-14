import blackjack as b
import time

while True:
    print ('\n'*100)
    print ("Welcome to Blackjack \n \n")
    time.sleep(3)
    
    # Created deck and chip objects. These will remain constants throughout.
    game_deck = b.Deck()
    player_chips = b.Chips()
    b.playing = True
    

    while b.playing:
        # New hands set up
        player_hand = b.Hand()
        dealer_hand = b.Hand()
        b.hit_stand = True

        # Deals cards and then displays hands
        print ("\n" * 100 + "Dealing cards...")
        time.sleep(3)
        game_deck.shuffle()
        b.start_game_deal(player_hand, dealer_hand, game_deck)
        b.show_some(player_hand, dealer_hand)
        time.sleep(3)

        #Takes bet from the player
        player_bet = b.take_bet(player_chips)
        player_chips.bet = player_bet

        #if hit_stand varibale is set to True in blackjack.py, the player will continue to have the option to hit or stand
        while b.hit_stand:
            print ('\n' * 100) 
            print (" Player, your hands value is {}.".format(player_hand.value))
            time.sleep(3)
            b.hit_or_stand(game_deck,player_hand)
            time.sleep(3)
            b.show_some (player_hand, dealer_hand)
            time.sleep(3)
        
        # Checks value of hand
            if player_hand.value > 21:
                b.player_busts(player_hand, dealer_hand, player_chips)
                time.sleep(5)
        
                b.hit_stand = False 
                b.show_some(player_hand, dealer_hand)
                time.sleep(5)

        print ("Dealer's hand value is currently {}".format(dealer_hand.value))
        time.sleep(5)
            
    
        while dealer_hand.value <= 17:
            b.hit(game_deck, dealer_hand)
            print ("Dealer hit. Dealer deck value is now {}".format(dealer_hand.value))
            time.sleep(5)
        
        if dealer_hand.value > 21:
            print ("Dealer's hand has exceeded 21!")
            time.sleep(3)
            b.dealer_busts(player_hand, dealer_hand, player_chips)
            time.sleep(5)

        elif dealer_hand.value >= player_hand.value:
            print ("Dealer's hand value is greater than your hand! Dealer's hand value = {}, Player's hand value = {}".format(dealer_hand.value, player_hand.value))
            b.dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            print ("Your hand value is greater than the dealer's hand! Player hand value = {}, Dealer hand value = {}".format(player_hand.value, dealer_hand.value))
            b.player_wins (player_hand, dealer_hand, player_chips)

        else: 
            print ("Error")

        if not b.play_again():
            break
        

    break
         
  