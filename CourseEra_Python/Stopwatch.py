# MiniProject: "Stopwatch: The Game"
# Importing GUI module to add GUI to the program for user interaction
import simplegui


# define and initializing global variables
time = tenth_sec = seconds_units = seconds_tenth = minutes = tries = win = 0

# Global variables to display time and win/tries
time_str = str(minutes) + ":" + str(seconds_tenth) + str(seconds_units) + "." + str(tenth_sec)
score_str = str(win) + "/" + str(tries)

# Global Image constants for displaying smiley or blank image
win_smiley = 'https://dl.dropboxusercontent.com/u/1935436/_win.png'
loose_smiley = 'https://dl.dropboxusercontent.com/u/1935436/_loose.png'
no_image = 'https://dl.dropboxusercontent.com/u/1935436/_1reset.png'

# format function to extract the digits from the variable (time)
# and represent it in the correct M:SS.T format to display on canvas
# This function is called every 10th of a second and when Reset button is pressed
def format(t):
    """Including global variables to use"""
    global tenth_sec, seconds_units, seconds_tenth, minutes, time_str
    
    """Extracting the digits and converting it into equivalent time format"""
    tenth_sec = (t % 10)       
    seconds_units = ((t / 10) % 10)        
    seconds_tenth = ((t / 100) % 6)      
    minutes = ((t / 100)/6)
    
    """Representing the manipulated numbers in correct time format as a string"""    
    time_str = str(minutes) + ":" + str(seconds_tenth) + str(seconds_units) + "." + str(tenth_sec)
    
# start_handler function, called when start button is pressed
# This function starts the timer and resets the smiley image
def start_handler():
    global image
    timer.start()
    image = simplegui.load_image(no_image)
    

# Handler when Stop button is pressed
# This fucntion stops the timer (if running), 
# also determines whether the timer is stopped at whole number 
# increments the number of tries and wins depending upon the condition
# Also, sets the image depending upon win or loose
def stop_handler():
    
    """Including global variables to use"""
    global tries, win, tenth_sec, score_str, image
    
    """If the timer is running, increment the number of tries """ 
    """and decide whether player won or lost and set the corresponding smiley image"""
    if timer.is_running():
        timer.stop()
        tries += 1
        if tenth_sec == 0:
            win += 1  
            image = simplegui.load_image(win_smiley)
        else:
            image = simplegui.load_image(loose_smiley)  
     
    """Set the format string to display number of tries and wins"""        
    score_str = str(win) + "/" + str(tries)


# Handler when Reset button is pressed
# Stops the timer and Resets the time, number of tries and wins to zero
# Also resets the smiley image to blank
def reset_handler():
    
    """Including global variables to use"""
    global time, tries, win, score_str, image
    
    """Stop the timer and reset global counters"""
    timer.stop()
    time = tries = win = 0
    
    """Reset the string to display number of tries and wins"""
    score_str = str(win) + "/" + str(tries)
    
    """Reset the image to blank and reset the display time"""
    image = simplegui.load_image(no_image)
    format(time)


# Handler for timer tick events
# Increments global time by one and displays it in the correct format
def timer_handler():
    
    global time
    time += 1
    format(time)

# Handler to draw text and images on canvas    
def draw_handler(canvas): 
    
    global image
    
    canvas.draw_text(time_str, (80, 110), 60, 'White')
    canvas.draw_text(score_str, (230, 30), 30, 'Green')
    
    canvas.draw_image(image, (326 / 2, 374 / 2), (326, 374), (150, 150), (60, 63))
    
    
    
# create frame and set canvas draw handler
frame = simplegui.create_frame('Stopwatch', 300, 200)
frame.set_draw_handler(draw_handler)

# Adds control buttons to frame
frame.add_button('Start', start_handler,100)
frame.add_button('Stop', stop_handler, 100)
frame.add_button('Reset', reset_handler, 100)

# Creates a timer and sets its handler to be called every 100 ticks
timer = simplegui.create_timer(100, timer_handler)

# Loads the image on frame
image = simplegui.load_image(no_image)

# Start the frame
frame.start()

