# =============================================================================
# Project 10: Developing the Montana Solitaire Game in Python using an ASCII
# based interface
# Date: 04/13/2020
# Author: Ghaleb Basher
# =============================================================================

#DO NOT DELETE THESE LINES
import cards, random
import copy
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)


def initialize():
    
    """ This function initializes the game by dealing all the 48 cards 
        needed to play the game """
    
    #We first make a Deck OBJECT and shuffle it
    game_deck = cards.Deck()
    game_deck.shuffle()
    
    tableau = []                             #tableau will be a list of 4 lists
    
    for i in range(4):
        row_of_cards = []                    #A row of cards
        for j in range(13):
            row_of_cards.append( game_deck.deal() )
        
        tableau.append( row_of_cards )       #Each row is then added to the tab
    
    return tableau
    
       
def display(tableau):
    '''
        This function displays the current state of the game.
        It display four rows of 13 cards with row and column labels.
        Ace is displayed with a blank.
        
        parameters: 
            tableau: data structure representing the tableau 
        
        Returns: None
    '''

    print("{:3s} ".format(' '), end = '')
    for col in range(1,14):
        print("{:3d} ".format(col), end = '')
    print()
        
    for r,row_list in enumerate(tableau):
        print("{:3d}:".format(r+1), end = '')
        for c in row_list:
            if c.rank() == 1:
                print("  {}{}".format(' ',' '), end = '')
            else:
                print("{:>4s}".format(str(c)),end = '')
        print()

def validate_move(tableau,source_row,source_col,dest_row,dest_col):
    """ This function returns a boolean to indicate whether the move being 
        specified is valid or not """
    
    #Create bool variables representing different states
    source_car = tableau[source_row][source_col]
    empty_dest = tableau[dest_row][dest_col].rank() == 1
    leftmost_c = dest_col == 0
    source_ran = source_car.rank() == 2
    
    if empty_dest:
        
        if leftmost_c and source_ran:           #First option
            return True
        
        if not leftmost_c:
            left_card = tableau[dest_row][dest_col - 1]
            
            if (left_card.suit() == source_car.suit()) and\
                (left_card.rank() == source_car.rank() - 1):
                return True
                
    return False    #If any of the tests didn't pass
        
        


def move(tableau,source_row,source_col,dest_row,dest_col):
    """ This function performs the actual move process """
    
    #make sure the move is valid
    valid = validate_move(tableau,source_row,source_col,dest_row,dest_col)
    
    if valid == False:
        return False
    
    #Get the two cards in play
    ace = tableau[dest_row][dest_col]
    card_being_moved = tableau[source_row][source_col]
    
    #Swap their position
    tableau[dest_row][dest_col] = card_being_moved
    tableau[source_row][source_col] = ace
    
    return True
    


def find_sequence( row ):
    """ This function takes a row of cards and returns false or the 
       limits of the sequence any found """
       
    current_rank = (row[0]).rank()
    current_suit = (row[0]).suit()
    

    
    if current_rank != 2:
        return "N" #There can't be a sequence if the first card isn't of rank 2
    
    for i in range(1,13):
        
        rank = row[i].rank()
        suit = row[i].suit()
        

        if not(rank == current_rank + 1 and suit == current_suit):
            return i - 1
        
        current_rank = rank
        
        #We reach here if the sequence has ended
        
        
    
  
def shuffle_tableau(tableau):
    """ This function is called to shuffle the tableau """
    
    #Extract all cards to be shuffled
    cards_to_shuffle = []
    sequences        = []
    
    
    #We need all rows 
    for i in range(4):
        
        
        result = find_sequence(tableau[i])

        if result == "N":
            sequences.append( None )
            cards_to_shuffle.extend( tableau[i] )
        else:
            sequences.append( result )
            cards_to_shuffle.extend( tableau[i][result + 1:])
    
    
    random.shuffle( cards_to_shuffle )
    #Remove all aces from the
    shuffled_cards_wo_aces = []
    aces                   = []

    for i in range( len(cards_to_shuffle) ):
        if cards_to_shuffle[i].rank() == 1:
            aces.append(cards_to_shuffle[i])
        else:
            shuffled_cards_wo_aces.append(cards_to_shuffle[i])
            

    #We need to repopulate the tableau - aces go first
    for i in range(4):
        
        if sequences[i] == None:
            tableau[i][0] = aces[i]
        else:
            tableau[i][ sequences[i] + 1 ] = aces[i]
    
    #Now the rest goes
    num = 0                     #Keeps track of the numbe of cards dealt
    for i in range(4):
        
        if sequences[i] == None:
            for j in range(1,13):
                tableau[i][j] = shuffled_cards_wo_aces[num]
                num += 1
        else:
            
            for j in range(sequences[i] + 2, 13):
                tableau[i][j] = shuffled_cards_wo_aces[num]
                num += 1
                
            
    return tableau
            
            
            

def check_win(tableau):
    """ The conditions for a win are listed in the project description.
        This algorithm  traverses the table and tells us whether or not 
        there is a win """
    
    for i in range(4):
        
        suit         = tableau[i][0].suit()
        current_rank = tableau[i][0].rank()
        
        if current_rank != 2:
            return False      #The first card in each row needs to be of rank 2
        
        for j in range(1,12):
            
            next_rank = tableau[i][j].rank()
            next_suit = tableau[i][j].suit()
            
            if next_rank == current_rank + 1 and next_suit == suit:
                current_rank = next_rank
            
            else:
                return False
            
        #Check for the ace at the end
        #last_card = tableau[i][j + 1]
        #if not(last_card.rank() == 1):
            #return False

    return True
        
            
             
def main():
    '''
        WRITE DOCSTRING HERE!
    '''
    
    #We initialize the tableau
    print("Montana Solitaire.")       #Display the header
    tableau = initialize()
    display(tableau)
    shuffles = 0
     
    
    '''
    tableau = [
            [cards.Card(5,1),cards.Card(3,1),cards.Card(4,1),cards.Card(5,1),cards.Card(7,1),cards.Card(6,1),cards.Card(1,1),cards.Card(8,1),cards.Card(9,1),cards.Card(10,1),cards.Card(11,1),cards.Card(12,1),cards.Card(13,1)],
            [cards.Card(2,2),cards.Card(3,2),cards.Card(1,2),cards.Card(2,2),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1)],
            [cards.Card(2,3),cards.Card(1,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1),cards.Card(2,1)],
            [cards.Card(2,4),cards.Card(3,3),cards.Card(2,4),cards.Card(2,4),cards.Card(2,4),cards.Card(2,4),cards.Card(2,4),cards.Card(2,4),cards.Card(1,4),cards.Card(2,4),cards.Card(2,1),cards.Card(2,4),cards.Card(2,4)]]
    '''
    
    while True:
        
        user_input = input("Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: ")
        
        if user_input.lower() == 'q':
            pass
            

        elif user_input.lower() == 's':
            if shuffles == 2:
                print("No more shuffles remain.")
            else:

                shuffle_tableau( tableau )
                display( tableau )
                shuffles += 1
            continue
        
        elif len(user_input.strip().split()) == 4:
            
            vals = user_input.split()
            try:
                vals = [int(i) for i in vals]
                a,b,c,d = vals
            except ValueError:
                print("Error: invalid input.  Please try again.")
                continue
            
            if not(a in range(1,5) and c in range(1,5) and b in range(1,14) and\
                d in range(1,14)):
                print("Error: row and/or column out of range. Please Try again.")
                continue
                    
            
            result = move(tableau, a-1, b-1, c-1, d-1)
            if result == False:
                print("Error: invalid move.  Please try again.")
                continue
            else:
                display(tableau)
            
            #Check for a win
            if check_win( tableau ):
                print("You won!")
            else:
                continue
        else:
            print("Error: invalid input.  Please try again.")
            continue
        
        play_again = input("Do you want to play again (y/n)?")
        if play_again == "y":
            #new game
            #We initialize the tableau
            print("Montana Solitaire.")       #Display the header
            tableau = initialize()
            display(tableau)
        else:
            print("Thank you for playing.")
            break
            

    

if __name__ == "__main__":
    main()  
