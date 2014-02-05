# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
score = 0
in_play = False
outcome = ""
d_card_pos = [50, 170]
p_card_pos = [50, 370]
x_add = 80
score_str = ["Score: " + str(score) , (450, 50), 30, 'Black']
game_str = ["BlackJack", (150, 50), 40, 'Black']
d_str = ['Dealer', (50, 150), 30, 'Black']
p_str = ['Player', (50, 350), 30, 'Black']
outcome =  ['', (200, 150), 30, 'Black']
h_s_str = ["Hit or Stand?" , (200, 350), 30, 'Black']

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# Card Class definition
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, \
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# Hand Class definition
class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.has_ace = False
        
    def __str__(self):
        hand_str = ""
        for c in self.hand:
            hand_str += (str(c) + " ")
        return "Hand Contains " + hand_str

    def add_card(self, card):
        self.hand.append(card)        
    
    def get_value(self):
        self.value = 0
        for c in self.hand:
            self.value += VALUES.get(c.get_rank())
            if c.get_rank() == 'A': self.has_ace = True 
            
        if self.has_ace:
            if (self.value + 10) <= 21:            
                self.value += 10                   
            else:
                return self.value    
                
        return self.value    
     
    def draw(self, canvas, pos): 
        i = 0
        for c in self.hand:
            c.draw(canvas, [(pos[0] + x_add * i), pos[1]])
            i += 1
        
# Deck class definition, contains list of card objects 
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                new_card = Card(s, r)
                self.deck.append(new_card)

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        deck_cards = ""
        for c in self.deck:
            deck_cards += (str(c) + " ")
        return "Deck Contains " + deck_cards

# Handler for Deal button
def deal():
    global outcome, in_play, game_deck, d_hand, p_hand, h_s_str, score, score_str
    
    if in_play:
        score -= 1
    
    game_deck = Deck()
    game_deck.shuffle()
    
    d_hand = Hand()
    p_hand = Hand()
    
    outcome = ['', (200, 150), 30, 'Black']
    h_s_str = ["Hit or Stand?" , (200, 350), 30, 'Black']   
    
    for n in range(2):
        d_hand.add_card(game_deck.deal_card())
        p_hand.add_card(game_deck.deal_card())
          
    in_play = True
    
# Handler for hit button
def hit():    
    global outcome, in_play, game_deck, d_hand, p_hand, score
    
    if in_play:
        p_hand.add_card(game_deck.deal_card())
        if p_hand.get_value() > 21:        
           in_play = False
        
        if not(in_play): 
            outcome[0] = "Dealer Won!, Player Busted"
            h_s_str[0] = "New Deal?"
            score -= 1
            
    else:
        h_s_str[0] = "Game Over, Hit Deal button!"

#Handler for Stand Button        
def stand():
    global outcome, in_play, game_deck, d_hand, p_hand, score, outcome
    
    if not(in_play):
        h_s_str[0] = "Game Over, Hit Deal button!"
    else:
        while d_hand.get_value() < 17:
            d_hand.add_card(game_deck.deal_card())            
        in_play = False
             
        if d_hand.get_value() > 21:
            outcome[0] = "Player Won, Dealer Busted"
            h_s_str[0] = "New Deal?"
            score += 1            
        elif d_hand.get_value() >= p_hand.get_value():
            outcome[0] = "Dealer Won"
            h_s_str[0] = "New Deal?"
            score -= 1            
        else:
            outcome[0] = "Player Won"
            h_s_str[0] = "New Deal?"
            score += 1

#Draw handler       
def draw(canvas):    
    canvas.draw_text(game_str[0], game_str[1], game_str[2], game_str[3])
    canvas.draw_text(d_str[0], d_str[1], d_str[2], d_str[3])
    canvas.draw_text(p_str[0], p_str[1], p_str[2], p_str[3])
    canvas.draw_text(outcome[0], outcome[1], outcome[2], outcome[3])
    canvas.draw_text("Score: " + str(score), score_str[1], score_str[2], score_str[3])
    canvas.draw_text(h_s_str[0], h_s_str[1], h_s_str[2], h_s_str[3])
    d_hand.draw(canvas, d_card_pos)
    p_hand.draw(canvas, p_card_pos)
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, \
                          [d_card_pos[0] + CARD_BACK_CENTER[0], d_card_pos[1] + CARD_BACK_CENTER[1]], CARD_SIZE)    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
