'''_____    _                       _                  ____                       _
/       \ /  |                    /  |               /     |                    /  |
$$$$$$$  |$$ |   _____     ______ $$ |    _          $$$$$ |  ______    _______ $$ |    _
$$ |__$$ |$$ | /      \  /       |$$ |  /  |            $$ | /      \  /       |$$ |  /  |
$$    $$< $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/        __   $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/
$$$$$$$  |$$ | /    $$ |$$ |      $$   $$<        /  |  $$ | /    $$ |$$ |      $$   $$<
$$ |__$$ |$$ |/$$$$$$$ |$$ \_____ $$$$$$  \       $$ \__$$ |/$$$$$$$ |$$ \_____ $$$$$$  \
$$    $$/ $$ |$$    $$ |$$       |$$ | $$  |      $$    $$/ $$    $$ |$$       |$$ | $$  |
$$$$$$$/  $$/  $$$$$$$/  $$$$$$$/ $$/   $$/        $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $'''


# # # # # #
# GLOBAL  #
# # # # # #

import os
os.system("mode con cols=100 lines=40")
import random
import time
card_suits = ('Spades','Diamonds','Clubs','Hearts')
card_values = {'Ace':11,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}
card_ranks = ('Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
player_name = 'Player'

# # # # # #
# CLASSES #
# # # # # #

class Card():
    '''each card has a SUIT and a RANK'''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return '{} of {}'.format(self.rank,self.suit)

class Deck():
    '''deck has 52 cards. Each SUIT has one of each RANK'''
    def __init__(self):
        repeater = 0
        self.deck = []
        self.y = number_of_decks()
        while repeater < self.y:
            for suit in card_suits:
                for rank in card_ranks:
                    self.deck.append(Card(suit,rank))
            repeater += 1

    def __str__(self):
        deck_print = ''
        for card in self.deck:
            deck_print += '\n- '+card.__str__()
        return 'The deck consists of the following {} cards:\n{}'.format(len(self.deck),deck_print)

    def card_count(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deck_topcard = self.deck.pop(0)
        return deck_topcard

    def thin_deck(self):
        '''checks if the shoe is near empty and refills with discard pile'''
        while len(self.deck) < 20:
            x = 0
            self.deck = []
            while x < self.y:
                for suit in card_suits:
                    for rank in card_ranks:
                        self.deck.append(Card(suit, rank))
                x += 1

class Hand():
    '''Player/dealer hand and values'''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.card2value = 0
        self.aces = 0
        self.BJace = 0

    def add_card2(self,card):
        self.cards.append(card)
        self.value += card_values[card.rank]
        self.card2value += card_values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
            self.BJace += 1

    def add_card(self,card):
        self.cards.append(card)
        self.value += card_values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.aces -= 1
            self.value -= 10

    def check_BJ_dealer(self):
        if self.value == 21 and self.BJace == 1:
            return True

    def check_BJ(self):
        if self.value == 21 and self.aces == 1:
            return True

class Chips():
    '''Betting'''
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        #Standard payout = 1:1
        self.total += self.bet
        print('You Won {} chips !! You have {} chips left.\n'.format(self.bet*2, self.total))

    def win_bet_BJ(self):
        #BlackJack payout = 3:2
        self.total += ((self.bet * 3) // 2)
        print('BlackJack payout is 3:2. You Won {} chips !! You have {} chips left.\n'.format(self.bet+((self.bet*3)//2), self.total))

    def lose_bet(self):
        self.total -= self.bet
        print('You Lost {} chips :( ...You have {} chips left.\n'.format(self.bet,self.total))

    def push(self):
        print('No chips won or lost. You have {} chips left.\n'.format(self.total))

# # # # # # #
# FUNCTIONS #
# # # # # # #

def username():
    global player_name
    player_name = input('Please state your name: ').title()

def intro():
    print('  _____     _                       _                  ____                       _')
    print('/       \ /  |                    /  |               /     |                    /  |')
    print('$$$$$$$  |$$ |   _____     ______ $$ |    _          $$$$$ |  ______    _______ $$ |    _')
    print('$$ |__$$ |$$ | /      \  /       |$$ |  /  |            $$ | /      \  /       |$$ |  /  |')
    print('$$    $$< $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/        __   $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/')
    print('$$$$$$$  |$$ | /    $$ |$$ |      $$   $$<        /  |  $$ | /    $$ |$$ |      $$   $$<')
    print('$$ |__$$ |$$ |/$$$$$$$ |$$ \_____ $$$$$$  \       $$ \__$$ |/$$$$$$$ |$$ \_____ $$$$$$  \ ')
    print('$$    $$/ $$ |$$    $$ |$$       |$$ | $$  |      $$    $$/ $$    $$ |$$       |$$ | $$  |')
    print('$$$$$$$/  $$/  $$$$$$$/  $$$$$$$/ $$/   $$/        $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$_|')
    print('\n'*2)
    print('Welcome to BlackJack!!')
    username()
    print(f'\nThank you for playing {player_name}!!\n\nHow to play BlackJack:\n')
    print(' - Aces may be counted as 1 or 11 points')
    print(' - 2 to 9 according to pip value')
    print(' - 10 and face cards count as ten points\n')
    print('The value of a hand is the sum of the point values of the individual cards. Except, a "blackjack" is the highest hand, consisting of an ace and any 10-point card, and it outranks all other 21-point hands.\n')
    print('After you place your bet, the dealer will deal two cards to you and two cards to self. One of the dealer cards is dealt face-down, all others face-up.\n')
    print('The following moves are available to the player: ')
    print(' - Stand: Player stands pat with his cards')
    print(' - Hit: Player draws another card (and more if he wishes)\n')
    print('If the player exceeds 21 (known as "breaking" or "busting") then he loses.')
    print('After the player has had his/her turn, the dealer will turn over the hole card.')
    print('If the dealer has 16 or less, it\'s mandatory to draw another card.')
    print('If the dealer goes over 21 points, then the player wins.')
    print('If the dealer does not bust, then the higher point total between the player and dealer will win.')
    print('Winning wagers pay even money (1:1), except a winning player blackjack pays 3:2.')
    print('The minimum bet is 10 chips. There is no maximum.\n')
    print('\nLet\'s go!\n')

def number_of_decks():
    while True:
        try:
            decknumber = int(input('Please select how many decks the shoe contains (1 - 8): '))
            if decknumber > 8 or decknumber < 1:
                print('Invalid input. Please try again...\n')
            elif decknumber == 1:
                print('\nYou have selected only 1 deck (52 cards) in the shoe.\n')
                return decknumber
            else:
                print('\nYou have selected {} decks ({} cards) in the shoe.\n'.format(decknumber,decknumber*52))
                return decknumber
        except:
            print('Invalid input, please try again...\n')

def take_bet(Chips):
    while True:
        try:
            print('You have {} chips'.format(Chips.total))
            while True:
                Chips.bet = int(input('Please place your Bet (10 - {}): '.format(Chips.total)))
                if Chips.bet < 10:
                    print('You placed a bet under the minimum of 10 chips. Please try again...')
                else:
                    break
        except ValueError:
            print('Incorrect input, bet must be a number, please try again...\n')
        else:
            if Chips.total < Chips.bet:
                print('Sorry, you have exceeded your available amount of chips. Please try again...\n')
            else:
                current_bet.append(Chips.total - Chips.bet)
                current_bet.append(Chips.bet)
                break

def dealer_hit(deck, hand):
    while True:
        if dealer_hand.value <= 16:
            dealer_hand.add_card(game_deck.deal())
            dealer_hand.adjust_for_ace()
        else:
            show_all(dealer_hand, player_hand)
            break

def hit(deck, hand):
    player_hand.add_card(game_deck.deal())
    player_hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global player_playing
    while True:
        try:
            user_input = input('Hit or Stand?: ')
            if user_input[0].lower() == 'h':
                hit(deck, hand)
                show_some(dealer_hand, player_hand)
                break
            elif user_input[0].lower() == 's':
                player_playing = False
                break
            else:
                print('Invalid input, please try again...')
        except IndexError:
            print('Invalid input, please try again...')

def show_some(dealer, player):
    hidden_card = dealer.cards[1]
    print('\n'*50)
    print('Available Chips: {}    Current Bet: {}\n~~~~~'.format(current_bet[0],current_bet[1]))
    print('\n   Dealer:\n')
    print('    - {}'.format('<Hidden>'))
    print('    - {}'.format(dealer.cards[1]))
    print('                     ({})\n'.format(dealer_hand.card2value))
    print('\n   {}:\n'.format(player_name))
    for card in player.cards:
        print('    - {}'.format(card))
    print('                     ({})\n'.format(player_hand.value))

def show_all(dealer, player):
    print('\n' * 50)
    print('Available Chips: {}    Current Bet: {}\n~~~~~'.format(current_bet[0],current_bet[1]))
    print('\n   Dealer:\n')
    for card in dealer.cards:
        print('    - {}'.format(card))
    print('                     ({})'.format(dealer_hand.value))
    print('\n   {}:\n'.format(player_name))
    for card in player.cards:
        print('    - {}'.format(card))
    print('                     ({})\n'.format(player_hand.value))

def player_busts(chips):
    print("{} BUSTS ... Dealer WINS!\n".format(player_name))
    chips.lose_bet()

def dealer_busts(chips):
    print("Dealer BUSTS ... {} WINS!\n".format(player_name))
    chips.win_bet()

def player_wins(chips):
    print("{} OUTRANKS dealer ... {} WINS!!!\n".format(player_name,player_name))
    chips.win_bet()

def dealer_wins(chips):
    print("Dealer OUTRANKS {} ... Dealer WINS!\n".format(player_name))
    chips.lose_bet()

def push(chips):
    print("Game is DRAW!!\n")
    chips.push()

def player_wins_BJ(chips):
    print("{} WINS with BlackJack!!!\n".format(player_name))
    chips.win_bet_BJ()

def dealer_wins_BJ(chips):
    print("Dealer WINS with BlackJack!\n")
    chips.lose_bet()

def push_BJ(chips):
    print("BlackJacks everywhere. Game is DRAW!!\n")
    chips.push()

def replay():
    if player_chips.total >= 10:
        while True:
            try:
                user_input = input('Would you like to continue betting? Yes/No: ')
                if user_input[0].lower() == 'y':
                    return True
                elif user_input[0].lower() == 'n':
                    return False
                else:
                    print('Invalid input. Please try again...')
            except IndexError:
                print('Invalid input. Please try again...')
    elif player_chips.total == 0:
        print('\nSorry, but you spent all your chips.\n\nGAME OVER')
        return False
    else:
        print('\nSorry, but you only have {} chips left. The minimum bet is 10.\n\nGAME OVER'.format(player_chips.total))
        return False

# # # # # # #
# MAIN CODE #
# # # # # # #

intro()                                         # game introduction/explanation
player_chips = Chips()                          # 100 chips assigned to player
game_deck = Deck()                              # deck created (user decides how many cards)
game_deck.shuffle()                             # deck shuffles
available_chips = True

while available_chips:                          # game ends if player loses all chips
    game_on = True
    while game_on:
        # TABLE SETUP, CARDS IN THE SHOE, INITIAL CARD DEALING:
        player_playing = True
        dealer_playing = True
        current_bet = []
        dealer_hand = Hand()                    # dealer hand assignment
        player_hand = Hand()                    # player hand assignment
        dealer_hand.add_card(game_deck.deal())  # dealer dealt hidden card
        dealer_hand.add_card2(game_deck.deal()) # dealer dealt open card
        dealer_hand.adjust_for_ace()            # adjusts hand less than 22 in case of two aces
        player_hand.add_card(game_deck.deal())  # player dealt 1st card
        player_hand.add_card(game_deck.deal())  # player dealt 2nd card
        player_hand.adjust_for_ace()            # adjusts hand less than 22 in case of two aces
        take_bet(player_chips)                  # bet placed
        show_some(dealer_hand, player_hand)     # shows table with hidden card
        # CHECK FOR BJ IF DEALER HAS OPEN ACE:
        while dealer_hand.check_BJ_dealer():
            print('Dealer has a BlackJack')
            time.sleep(2.5)
            show_all(dealer_hand, player_hand)
            if player_hand.check_BJ():          # draw if player also has BJ
                push_BJ(player_chips)
                player_playing = False
                dealer_playing = False
                break
            else:                               # dealer wins
                dealer_wins_BJ(player_chips)
                player_playing = False
                dealer_playing = False
                break
        # IN CASE PLAYER HAS BJ:
        while player_hand.check_BJ():
            print('You have a BlackJack\n')
            time.sleep(2.5)
            show_all(dealer_hand, player_hand)
            if dealer_hand.check_BJ():          # draw if dealer also has BJ
                print('Dealer has a BlackJack too\n')
                push_BJ(player_chips)
                player_playing = False
                dealer_playing = False
                break
            else:                               # player wins
                player_wins_BJ(player_chips)
                player_playing = False
                dealer_playing = False
                break
        # PLAYER ACTIONS:
        while player_playing:
            hit_or_stand(game_deck, player_hand)
            if player_hand.value > 21:          # player busts, dealer wins
                player_busts(player_chips)
                dealer_playing = False
                break
            elif player_hand.value == 21:       # player stands on 21
                print('You reached 21, it would be wise to Stand...\n...Please wait for Dealer\'s turn\n')
                time.sleep(3.5)
                break
        # DEALER ACTIONS:
        while dealer_playing:
            dealer_hand.adjust_for_ace()        # adjusts hand less than 22, when ace busts
            dealer_hit(game_deck, dealer_hand)
            if dealer_hand.value > 21:          # dealer busts, player wins
                dealer_busts(player_chips)
                break
            elif player_hand.value > dealer_hand.value:   # player outranks and wins
                player_wins(player_chips)
                break
            elif player_hand.value == dealer_hand.value:  # even values. Draw game
                push(player_chips)
                break
            elif player_hand.value < dealer_hand.value:   # dealer outranks and wins
                dealer_wins(player_chips)
                break
        # REPLAY:
        if replay():                            # continue betting
            print("\nLet's continue!!\n")
            game_deck.thin_deck()
            game_on = True
            player_playing = False
            dealer_playing = False
        else:                                   # exit game
            print("\nGoodbye {} and thank you for choosing 'Koutelis Casinos' !!\n".format(player_name))
            input("\nPress 'Enter' to exit game...")
            game_on = False
            available_chips = False
            player_playing = False
            dealer_playing = False
