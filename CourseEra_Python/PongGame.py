# Mini Project 4: Pong game

# Import libraries
import simplegui
import random

#Global variables
# Canvas globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# Direction globals 
LEFT = False
RIGHT = True
DIRECTION = LEFT
bounce_counter = 0

# Scoring globals
score_r = 0
score_l = 0

# Paddle movement globals
paddle1_pos = [PAD_WIDTH/2, HEIGHT/2]
paddle2_pos = [(WIDTH - PAD_WIDTH/2), HEIGHT/2]
paddle1_vel = 0
paddle2_vel = 0
PADDLE_MOVE = 8

ball_pos = [WIDTH / 2, HEIGHT/2]
ball_vel = [(random.randrange(120, 240))/60.0,\
            (random.randrange(60, 180))/60.0]

# Global Image constants for displaying smiley or blank image
win_smiley = 'https://dl.dropboxusercontent.com/u/1935436/_win.png'
loose_smiley = 'https://dl.dropboxusercontent.com/u/1935436/_loose.png'
no_image = 'https://dl.dropboxusercontent.com/u/1935436/_1reset.png'

# Function to change the direction of ball once it strikes one of the paddles
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global bounce_counter, image_l, image_r   
    
    if direction:
        ball_vel[0] = random.randrange(120, 240)
        ball_vel[0] = -ball_vel[0]/60.0
        ball_vel[0] += ((bounce_counter/100.0)*ball_vel[0])
        bounce_counter += 15
    else:
        ball_vel[0] = random.randrange(120, 240)
        ball_vel[0] = ball_vel[0]/60.0
        ball_vel[0] += ((bounce_counter/100.0)*ball_vel[0])
        bounce_counter += 15
 
# Function to update ball position every tick event    
def update_ball():
    
    global ball_pos, ball_vel 
    global score_r, score_l, DIRECTION, bounce_counter, image_l, image_r
    
    # collide and reflect if ball hits paddles   
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and \
        ((paddle1_pos[1] - PAD_HEIGHT/2) <= ball_pos[1] <= \
         (paddle1_pos[1] + PAD_HEIGHT/2)):   
            
        DIRECTION = RIGHT
        image_l = simplegui.load_image(no_image)
        image_r = simplegui.load_image(no_image)
        spawn_ball(DIRECTION)
        
    elif (ball_pos[0] >= WIDTH - (BALL_RADIUS + PAD_WIDTH)) and \
        ((paddle2_pos[1] - PAD_HEIGHT/2) <= ball_pos[1] <= \
         (paddle2_pos[1] + PAD_HEIGHT/2)):
            
        DIRECTION = LEFT
        image_l = simplegui.load_image(no_image)
        image_r = simplegui.load_image(no_image)
        spawn_ball(DIRECTION)
    
    # collide and reflect if ball hits horizontal wall 
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = random.randrange(60, 180)
        ball_vel[1] = -ball_vel[1]/60.0
        
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = random.randrange(60, 180)
        ball_vel[1] = ball_vel[1]/60.0
    
    # if ball hits the gutter w/o paddle behind it, 
    # start a new game and update scores     
    elif (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH): 
        score_r += 1
        DIRECTION = RIGHT
        image_r = simplegui.load_image(win_smiley)
        image_l = simplegui.load_image(loose_smiley)
        new_game()  
   
    elif (ball_pos[0] >= WIDTH - (BALL_RADIUS + PAD_WIDTH)):
        score_l += 1  
        image_l = simplegui.load_image(win_smiley)
        image_r = simplegui.load_image(loose_smiley)
        DIRECTION = LEFT
        new_game()
        
    ball_pos[0] -= ball_vel[0]
    ball_pos[1] -= ball_vel[1]

# Function to start new game
def new_game():
    global ball_pos, ball_vel  
    global bounce_counter

    ball_pos = [WIDTH / 2, HEIGHT/2]
    ball_vel[1] =  (random.randrange(60, 180))/60.0
    bounce_counter = 0                  
    spawn_ball(DIRECTION)

# Reset button handler, resets the score, ball and paddle positions    
def reset():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos  
    global score_r, score_l, image_l, image_r
    
    score_r = score_l = 0 
    ball_pos = [WIDTH / 2, HEIGHT/2]
    bounce_counter = 0
    
    paddle1_pos = [PAD_WIDTH/2, HEIGHT/2]
    paddle2_pos = [(WIDTH - PAD_WIDTH/2), HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    
    ball_vel[1] =  (random.randrange(60, 180))/60.0
    
    image_l = simplegui.load_image(no_image)
    image_r = simplegui.load_image(no_image)
    
# update the position of left paddle if one of the 'w' or 's' keys is pressed
def update_paddle1_pos():
    global paddle1_pos
    
    if (paddle1_pos[1] + paddle1_vel) <= (PAD_HEIGHT/2):
        paddle1_pos[1] = (PAD_HEIGHT/2)
        
    elif (paddle1_pos[1] + paddle1_vel) >= (HEIGHT - (PAD_HEIGHT/2)):         
        paddle1_pos[1] = (HEIGHT - (PAD_HEIGHT/2))
        
    else:
        paddle1_pos[1] += paddle1_vel
        
# update the position of left paddle if one of the 'up' or 'down' keys is pressed        
def update_paddle2_pos():
    global paddle2_pos
    
    if (paddle2_pos[1] + paddle2_vel) <= (PAD_HEIGHT/2):
        paddle2_pos[1] = (PAD_HEIGHT/2)
        
    elif (paddle2_pos[1] + paddle2_vel) >= (HEIGHT - (PAD_HEIGHT/2)):
         paddle2_pos[1] = (HEIGHT - (PAD_HEIGHT/2))
            
    else:        
        paddle2_pos[1] += paddle2_vel

# Draw handler to draw on canvas        
def draw(c):
    global score_r, score_l, paddle1_pos, paddle2_pos, \
        ball_pos, ball_vel, paddle1_vel, paddle2_vel
    
    update_ball()
        
    # draw mid line and gutters
    # Draw field
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
            
    # draw smiley
    c.draw_image(image_l, (326 / 2, 374 / 2), (326, 374), (110, 50), (50, 53))
    c.draw_image(image_r, (326 / 2, 374 / 2), (326, 374), (490, 50), (50, 53))
    
    # Draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "yellow", "yellow")
    
    # update paddle's vertical position, keep paddle on the screen
    update_paddle1_pos()
    update_paddle2_pos()    
 
    # draw paddles
    c.draw_polygon([(0, (paddle1_pos[1] - PAD_HEIGHT/2)), 
                    (PAD_WIDTH, (paddle1_pos[1] - PAD_HEIGHT/2)), 
                    (PAD_WIDTH, (paddle1_pos[1] + PAD_HEIGHT/2)), 
                    (0, (paddle1_pos[1] + PAD_HEIGHT/2))], 
                   2, 'white','red')
    
    c.draw_polygon([(WIDTH, (paddle2_pos[1] - PAD_HEIGHT/2)), 
                    ((WIDTH - PAD_WIDTH), (paddle2_pos[1] - PAD_HEIGHT/2)), 
                    ((WIDTH - PAD_WIDTH), (paddle2_pos[1] + PAD_HEIGHT/2)), 
                    (WIDTH, (paddle2_pos[1] + PAD_HEIGHT/2))], 
                   2, 'white','red')
    
    
    # draw scores
    c.draw_text(str(score_l), [180, 50], 40, 'white')
    c.draw_text(str(score_r), [400, 50], 40, 'white')
    
    
# change the paddle velocities, 
# when a key corresponding to the paddle is pressed    
def keydown(key):
    global paddle1_vel, paddle2_vel
        
    if key==simplegui.KEY_MAP["W"]:
        paddle1_vel = -PADDLE_MOVE
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = PADDLE_MOVE
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -PADDLE_MOVE 
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = PADDLE_MOVE    

# reset the velocities of the corresponding paddle, 
# when a key related to it is released
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP["W"] or key==simplegui.KEY_MAP["s"]:
            paddle1_vel = 0
    
    elif key==simplegui.KEY_MAP["up"] or key==simplegui.KEY_MAP["down"]:
            paddle2_vel = 0  
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT,)
frame.set_canvas_background('green')

# set canvas draw handler
frame.set_draw_handler(draw)

# set keyboard event handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# reset button handler
frame.add_button('Reset', reset, 100)

# Loads the image on frame
image_l = simplegui.load_image(no_image)
image_r = simplegui.load_image(no_image)

# start frame and new game
frame.start()
new_game()
