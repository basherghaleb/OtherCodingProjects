''' Insert heading comments here.'''
#Project 6
#This code will take the scoring_per_game.csv and organize it into these 6 categories
# The number of left and right hand shooters
# The number of hockey players in position for left, right, center, defense
# The number of players playing left and right wing
# The top ten points per game
# The top ten games played
# The top ten shots taken
import csv

def open_file():
    '''function that opens the file when called in the main'''
    while True:
        try:
            f_open = input("Enter filename: ")  #asks user to input the file name
            f_pointer = open(f_open)
            return f_pointer
        except FileNotFoundError:
            print("Error, please try again:") #if file name is invalid, will be prompted to try again

def read_file(fp):
    '''reads the file using the csv reader'''
    reader = csv.reader(fp) #needed to read excel files
    master = []
    next(reader, None)
    for line in reader:
        master.append(line)
    return master
   
def shoots_left_right(master_list):
    '''displays the number of left and right hand shooters'''
    shoot_left_count = 0 #initializing at 0 because it is going to be counted
    shoot_right_count = 0
    for shooting_hand in master_list:
        x = shooting_hand[1] #indexing all the shooting hands
        if x == "L":
            shoot_left_count += 1
        else:
            shoot_right_count += 1
    return shoot_left_count, shoot_right_count

def position(master_list):
    '''displays the counts the number of players in the left, right, center, and defense positions'''
    L = 0 #intializing each position for the counter
    R = 0
    C = 0
    D = 0
    for position in master_list: 
        if position[2] == "L": #if position is in the third column then add 1 and the same for all the other if statements
            L += 1
        if position[2] == "R":
            R += 1
        if position[2] == "C":
            C += 1
        if position[2] == "D":
            D += 1
    return L, R, C, D

def off_side_shooter(master_list):
    '''displays the number of players in the left and right wings'''
    left_wing = 0 #initializing
    right_wing = 0
    for x in master_list:
        shooting_hand = x[1]
        position = x[2]
        if shooting_hand == "R": #if shooting hand is right and thier position is L then add 1 to left wing
            if position == "L":
                left_wing += 1
        if shooting_hand == "L" : #if shooting hand is left and thier position is R then add 1 to right wing
            if position == "R":
                right_wing += 1
    return left_wing, right_wing

def points_per_game(master_list):
    '''displays the top ten points per game scored'''
    l = []
    for x in master_list: 
        name = x[0] #indexing name
        position = x[2]
        goals_per_game = float(x[18]) #converting the goals to floats because when you index from a csv its only a string
        tupl = (goals_per_game, name, position)
        l.append(tupl)
        
    top = sorted(l, reverse = True) #sorts the best games played
    return top[:10] #shows only the 10 best

def games_played(master_list):
    '''displays the top ten games played'''
    l = []
    for x in master_list:
        name = x[0]
        gp = x[3]
        gp_int = int(gp.replace(',', '')) #converts to an int because they're strings and removes commas from the big numbers
        tupl2 = (gp_int, name)
        l.append(tupl2)
    top_ten = sorted(l, reverse = True) #sorts the best games played
    return top_ten[:10] 

def shots_taken(master_list):
    '''displays the top ten shots taken'''
    l= []
    for x in master_list:
        name = x[0]
        shots_taken = x[9]
        if shots_taken == "--": #since there are some in the column with -- I'm continuing them when the code is ran
            continue
        shots_taken_int = int(shots_taken.replace(',',''))
        tupl3 = (shots_taken_int, name)
        l.append(tupl3)
    best_shots = sorted(l, reverse = True)
    return best_shots[:10]

def main():
    '''Calls all function and takes .csv files and organizes everything into categories'''
    fp = open_file()
    master = read_file(fp)
    shoot_left_count, shoot_right_count = shoots_left_right(master) #using the return values for shoots_left_right in master and converting it to a variable

    print("{:^10s}".format("Shooting"))
    print("left:  {:4d}".format(shoot_left_count))
    print("right: {:4d}".format(shoot_right_count))
   
    L, R, C, D = position(master) #using the return values for position in master and converting to a variable 
    print("{:^12s}".format("Position"))
    print("left:    {:4d}".format(L))
    print("right:   {:4d}".format(R))
    print("center:  {:4d}".format(C))
    print("defense: {:4d}".format(D))
  
    left_wing, right_wing = off_side_shooter(master) #using the return values for offside shooter in master and converting to a variable 
    print("{:^24s}".format("Off-side Shooter"))
    print("left-wing shooting right: {:4d}".format(left_wing))
    print("right-wing shooting left: {:4d}".format(right_wing))
    
    points = points_per_game(master) #creating variable for 
    print("{:^36s}".format("Top Ten Points-Per-Game"))
    print("{:<20s}{:>8s}{:>16s}".format("Player", "Position", "Points Per Game")) #formatting categories for each column 
    for i in points: 
        print("{:<20s}{:>8s}{:>16.2f}".format(i[1],i[2],i[0])) #using the indexing of the function to format
   
    games = games_played(master)
    print("{:^36s}".format("Top Ten Games-Played"))
    print("{:<20s}{:>16s}".format("Player", "Games Played"))
    for i in games: 
        print("{:<20s}{:>16,d}".format(i[1],i[0]))
    
    shots = shots_taken(master)
    print("{:^36s}".format("Top Ten Shots-Taken"))
    print("{:<20s}{:>16s}".format("Player", "Shots Taken"))
    for i in shots: 
        print("{:<20s}{:>16,d}".format(i[1],i[0]))

   

if __name__ == "__main__": #needed for the main function to be called 
    main()
