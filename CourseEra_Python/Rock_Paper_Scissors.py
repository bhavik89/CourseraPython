#Mini Project 2:
# Rock-paper-scissors-lizard-Spock program


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# library function random is imported to generate random numbers
import random

# helper functions
# This Function converts a number (0-4) to corresponding name 
def number_to_name(number):
    
        if number == 0:
            name = 'rock'
        elif number == 1:
            name = 'Spock'
        elif number == 2:
            name = 'paper'   
        elif number == 3:
            name = 'lizard'	
        elif number == 4:
            name = 'scissors'
        else:
            name = 'Invalid'
        
        return name 

# This function converts a name to the corresponding number    
def name_to_number(name):
    
        if name == 'rock':
            number = 0
        elif name == 'Spock':
            number = 1
        elif name == 'paper':
            number = 2   
        elif name == 'lizard':
            number = 3	
        elif name == 'scissors':
            number = 4
        else:
            number = 9
        
        return number 

# determines winner
def winner(diff_mod5):
    
    if diff_mod5 == 0:
        print "Player and computer tie! \n"
        
    elif diff_mod5 <= 2:
        print "Player Wins! \n"
    
    else: 
        print "Computer Wins! \n"


    
# Main function: 
# This function takes the player's choice and 
# generates a random guess for computer 
# and computes the winner\Tie between two
def rpsls(name): 
   
    # converts name to player_number using name_to_number
    print "Player chooses %s" %name
    player_number = name_to_number(name)
 
    if player_number > 4:
        print "ERROR: Incorrect user input!! \n"
        return None

    # computes random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    print "Computer chooses %s" % number_to_name(comp_number)
    
    # computes difference of player_number and comp_number modulo five
    diff_mod5 = (player_number - comp_number) % 5
    winner(diff_mod5)
    
# tests for the program
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

