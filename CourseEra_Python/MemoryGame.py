# Mini Project 5: Memory

import simplegui
import random

#Globals for canvas and card image
CANVAS_W = 800
CANVAS_H = 100
"""Loading of image may take some time for the first Run,
but it would be quicker in subsequent runs"""
CARD_IMG = simplegui.load_image("https://dl.dropboxusercontent.com/u/1935436/card.jpg")

# helper function to initialize globals and restart new game
def new_game():
    global cards, state, exposed, matched, click_index, turns
    cards = range(0,8) + range (0,8)
    random.shuffle(cards)
    exposed = [0]*len(cards)
    matched = []
    click_index = []
    state = 1
    turns = 0
     
# Mouse click handler
def mouseclick(pos):    
    global cards, state, exposed, matched, click_index, turns
    
    """
    If state = 1, check how many cards are clicked previously,
    if 2 unpaired cards are clicked, then flip those cards
    """
    if state == 1:       
        if len(click_index) == 2 and \
        (pos[0]/50 not in click_index) and \
        (pos[0]/50 not in matched):
            exposed[click_index[0]] = exposed[click_index[1]] = 0
            click_index = []
        
        """
        If the card clicked is not exposed, expose that card and 
        update the index of clicked card
        """
        if not(exposed[pos[0]/50]):    
            exposed[pos[0]/50] = not(exposed[pos[0]/50])
            click_index.append(pos[0]/50)
            state = 2
        
    else:  
        """
        if state = 2, exposed the clicked card and turns
        """
        if not(exposed[pos[0]/50]):    
            exposed[pos[0]/50] = not(exposed[pos[0]/50])
            click_index.append(pos[0]/50)
            state = 1
            turns += 1
            
            """
            if two paired cards are exposed in two turns,
            add the indexes of that card in matched list
            """
            if cards[click_index[0]] == cards[click_index[1]]:
               matched.extend(click_index) 
    
    """
    Expose the paired cards, when clicked
    """
    for match in matched:
            exposed[match] = 1       
    
    
# Draw handler to draw the cards and text    
def draw(c):
    global label   
    
    init_pos = 20
    CARD_W = 50    
    for card in cards:
        c.draw_text(str(card), (init_pos, 65), 50, 'white')
        init_pos += 49
    
    for ex in exposed:
        if not ex:
            c.draw_image(CARD_IMG, (100/2, 140/2), (100, 140), (CARD_W/2, CANVAS_H/2) , (50, CANVAS_H))
        CARD_W += 100
    
    label.set_text("Turns = " + str(turns))    
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

