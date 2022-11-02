# =============================================================================
# Project 7
# Working on US Census State Representative Partionement 
# def open_file
# def calc_multupliers 
# def calc_priorities
# def read_file_make_priorities
# def add_to_state
# def display(states)
# def main
# =============================================================================

import math

def open_file():
    ''' This function opens a file and returns a file pointer '''
    
    while True:
        filename = input("Enter filename: ")
        try:
            fp = open(filename, "r")
            return fp
        except FileNotFoundError:
            print("Error in file. Try again.")
            continue
        


def calc_multipliers():
    ''' This function returns a list of multipliers '''
    
    multipliers = [] # Make an empty list that we will then populate
    
    for n in range(2,61):
        
        multiplier_n = 1 / math.sqrt( n * ( n- 1) )
        multipliers.append( multiplier_n )
    
    return multipliers
    

    
def calc_priorities(state_name, state_population, list_of_multipliers):
    ''' This function returns a list of priorities values for the given state.
    That list is a list of tuples in the form (priority_val, state_name) '''
    
    priorities = []   #An empty list at the beginning
    
    for multiplier in list_of_multipliers:
        
        priority_val = int(multiplier * state_population)  #The priority val needs to be an integer
        priorities.append( (priority_val, state_name) )    #Add the ith tuple
    
    #Once we're done, we sort the list in decreasing value of priority_val
    priorities  = sorted( priorities, reverse = True )
    
    return priorities
        
        
    
    
def read_file_make_priorities(fp, multipliers): 
    ''' This function takes in a file pointer and a list of multipliers. It
        reads the file pointer and builds two lists: 
        '''
    state_reps = []
    priorities = []
    
    next(fp)                    #This instruction skips the first line in the file
    #Read the file pointer
    
    for line in fp:            #line is a string representing a single line in the file
        line_tokens = line.strip().split(",")
        state = line_tokens[1].strip().strip('"')
        
        #We don't include DC and Puerto Rico
        if state  == "District of Columbia" or state == "Puerto Rico":
            continue
        state_reps.append( [state, 1] )
        
        population = int(line_tokens[2])
        
        priorities.extend(calc_priorities(state, population, multipliers))
        

    state_reps = sorted( state_reps )
    priorities = sorted(priorities, reverse = True )[0:385] #We only need 385
    
    
    return state_reps, priorities
        

def add_to_state(state,states):
    ''' This function is meant to increase the count of representatives of a 
        a given state. It returns nothing '''
        
    #We recall that states is a list of lists in the form [[state1, count1], [state2, count2], ...]
    for entry in states:
        if entry[0] == state:
            entry[1] += 1
    

def display(states):
    ''' This function is meant to display all the states along with their
        representative counts '''
        
    print("{:<15}{}".format("State", "Representatives"))
    for entry in states:
        
        print("{:<15s}{:>4d}".format(entry[0], entry[1]))
    

def main():
    
    #Tests for now
    fp = open_file()
    multipliers = calc_multipliers()
    
    states, representatives = read_file_make_priorities(fp, multipliers)
    
    #Populate the representative count for each state
    for element in representatives:
        add_to_state(element[1], states)
    
    #Display the results
    display(states)
    


if __name__ == "__main__":
    main()
