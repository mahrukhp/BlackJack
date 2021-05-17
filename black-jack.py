suits = ('Clubs', 'Hearts', 'Diamonds', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'King', 'Queen', 
        'Jack', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
          'King':10, 'Queen':10, 'Jack':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
import random
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        
    def __str__(self):
        d = ''
        for card in self.deck:
            d += '\n' + card.__str__()
        return 'The deck is: ' + d
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
        
def hit(hand, deck):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(hand, deck):
    global playing
    while True:
        a = input('Would you like to hit or stand? Enter h or s : ').lower()
        if a[0] == 'h' and hand.value < 21:
            hit(hand, deck)
        elif a[0] == 's':
            print('Player stands. DEALERS TURN!\n')
            playing = False
        else:
            print('Please try again!')
            continue
        break
                
def place_bet(chips):
    while True:
        try:
            chips.bet = int(input('Enter the amount you would like to bet : '))
            if chips.total < chips.bet:
                print(f'Sorry, you cannot exceed {chips.total}')
            elif chips.bet < 10:
                print('Minimum amount that can be placed is 10')
            else:
                break
        except:
            print('Please enter an integer!')
            
def show_some(player, dealer):
    print('DEALERS CARDS:')
    print('<Card Hidden>')
    print(dealer.cards[1])
    print()
    print('PLAYERS CARDS:')
    for i in player.cards:
        print(i)
    print()    

def show_all(player, dealer):
    print('DEALERS CARDS:')
    for i in dealer.cards:
        print(i)
    print('Dealers hand =', dealer.value)
    print()
    print('PLAYERS CARDS:')
    for i in player.cards:
        print(i)
    print('Players hand =', player.value)
    print()
    
def player_wins(player, dealer, chips):
    print('Player Wins!!')
    chips.win_bet()

def player_busts(player, dealer, chips):
    print('Player Busts!')
    chips.lose_bet()
    
def dealer_wins(player, dealer, chips):
    print('Dealer Wins!!')
    chips.lose_bet()
    
def dealer_busts(player, dealer, chips):
    print('Dealer Busts!')
    chips.win_bet()
    
def push(player, dealer):
    print('Its a tie... PUSH!!')
    
chips = Chips()

while True:
    playing = True
    print('Welcome to BlackJack\n')
    
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
    place_bet(chips)
    
    show_some(player, dealer)
    
    while playing:
        hit_or_stand(player, deck)
        show_some(player, dealer)
        if player.value > 21:
            player_busts(player, dealer, chips)
            break
            
    if player.value <= 21:
        
        while dealer.value < 17:
            hit(dealer, deck)
    
        print()
        show_all(player, dealer)
    
        if player.value > 21:
            player_busts(player, dealer, chips)
        elif dealer.value > 21:
            dealer_busts(player, dealer, chips)
        elif player.value > dealer.value:
            player_wins(player, dealer, chips)
        elif dealer.value > player.value:
            dealer_wins(player, dealer, chips)
        else:
            push(player, dealer)

    print(f'Total chips left = {chips.total}')
    
    play_again = input('Would you like to play again? Enter yes or no : ').lower()
    if play_again[0] == 'y':
        continue
    else:
        print('Thank you for playing!!!')
    break
