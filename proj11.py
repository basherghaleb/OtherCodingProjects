# =============================================================================
# Project 11: Building our own custom classes in Python to simulate a rush game
# Date : 04/22/2020
# Author: Basher Ghaleb
# =============================================================================

#DO NOT DELETE THis LINES
MAP = {"U":"Up","D":"Down","L":"Left","R":"Right"}

class Student(object):
    """ Implementation of the student class which describes an MSU student
        waking up for class """
    
    def __init__(self, item_list=None, classroom_id=-1):
        '''Initializes yourself, with an empty backpack by default. The default position of the student is room -1.'''

        if item_list == None:
            self.backpack = []
        else:
            self.backpack = item_list
        self.classroom_id = classroom_id
    
    

    def __repr__(self):
        '''Returns a string representation of the student.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the student's inventory.'''
        s = "Backpack: "
        if len(self.backpack) == 0:
            s += "Empty"
        else:
            for item in self.backpack:
                s += item + ", "
            else:
                s = s[:-2] # remove trailing comma and space
        return s

    def __eq__( self, S ):
        """ This function compares two Student objects """
        
        return (S.classroom_id == self.classroom_id) and (S.backpack == self.backpack)
                    
    

     
    def place(self, classroom_id):
        """ This function places the student in a classroom """
        
        self.classroom_id = classroom_id
    

    
    def add_item(self, item):
        """ Adds a new item to the backpack """
        
        #If the backpack is already full
        if len( self.backpack ) == 6:
            print("Backpack is full.")
        else:
            self.backpack.append( item )
            
            
            

    def remove_item(self, item):
        """ This function removes an item from the backpack """
        
        try:
            found = self.backpack.index( item )
            self.backpack.pop( found )
            return True
        
        except ValueError:
            print("Failed to remove item from backpack.")
            return False
            
        
        


class Classroom(object):
    """ This function describes a classroom object """
    
    def __init__(self, text_desc="0 empty"):
        '''Initialzes a classroom. By default it has id 0 and is a "empty" room with no inventory or exits.'''
        description = text_desc.split()

        self.id = int(description[0])
        self.course = description[1]

        # Initialize a dictionary of potential exits as empty
        self.exits = {}

        # Initialize a "backpack" of items as empty list
        self.backpack = []
        
        #Build the lists
        number_of_tokens = len( description )
        
        if number_of_tokens > 2:
            for i in range(2, number_of_tokens ):
                #An exit or an item
                token = description[i]
                
                if token[0] in MAP:   #An exit 
                    direction = token[0]
                    integer   = token[1:]
                    
                    self.exits[direction] = int(integer)
                else:                 #An item
                    self.backpack.append( token )
                

    def __repr__(self):
        '''Returns a string representation of the classroom.'''
        classroom_repr = '''Classroom("''' + repr(self.id) + " " + self.course

        for direction in self.exits:
            classroom_repr += " {}".format(direction) + repr(self.exits[direction])

        for item in self.backpack:
            classroom_repr += " " + item

        classroom_repr += '''")'''

        return classroom_repr

    def __str__(self):
        '''Returns a string representing the room in a nice conversational style.'''

        # Basic classroom description
        classroom_str = "You see a " + self.course + " classroom."

        # List the things in the classroom
        if len(self.backpack) == 1:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + "."
        if len(self.backpack) == 2:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + \
                             " and a " + self.backpack[1] + "."
        elif len(self.backpack) > 2:
            classroom_str += " On the desk you see "
            for item in self.backpack[:-1]:
                classroom_str += "a " + item + ", "
            classroom_str += "and a " + self.backpack[-1] + "."

        # List the exits
        if len(self.exits) == 0:
            classroom_str += " Run through the classroom grab what you need (if possible). Exit and run to the exam!"
        elif len(self.exits) == 1:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + "."
        elif len(self.exits) == 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + " or " + MAP[list(self.exits.keys())[1]] + "."
        elif len(self.exits) > 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go "
            for direction in list(self.exits.keys())[:-1]:
                classroom_str += MAP[direction] + ", "
            classroom_str += "or " + MAP[list(self.exits.keys())[-1]] + "."

        return classroom_str
    
    def __eq__( self, C ):
        """ Compares two classroom objects """
        
        return (C.id == self.id) and (C.exits == self.exits) and \
             (C.course == self.course) and (C.backpack == self.backpack)
        
    
    
    def add_item(self, item):
        """ We add a new item to the backpack """
        
        self.backpack.append( item )
        
    
        

    def remove_item(self, item):
        """ Removes the item from the backpack """
    
        try:
            found = self.backpack.index( item )
            self.backpack.pop( found )
            return True
        
        except ValueError:
            print("Failure to find the item in the classroom.")
            return False
            
            

    def get_room(self, direction):
        """ We return either the room in that direction or False """
        
        try:
            return self.exits[direction]
        except KeyError:
            return False
    

    


class Rush(object):
    """ This function describes The Rush process """
    

    def __init__(self, filename="rushing.txt"):
        '''Initializes the student rushing to class.  The student starts in the classroom with the lowest id.'''

        # First make a student start with an empty inventory
        self.student = Student()

        # Create classrooms are an empty dictionary
        self.classrooms = {}
        
        # Now read the file to get the classroom lines
        file_pointer = open( filename, "r")            #We open the text file for reading
        
        for line in file_pointer:
            line = line.strip()
            
            classroom = Classroom(line)   #Make a classroom object
            
            classroom_id = int( line.split()[0] )
            
            self.classrooms[classroom_id] = classroom
        

        # Place the student in the room with lowest id
        self.student.place(min(self.classrooms.keys()))
        

    def __repr__(self):
        '''Returns a string representation.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the journey to the class, simply giving the number of rooms.'''
        search_str = "You are searched in "
        if len(self.classrooms) == 0:
            search_str += "no classrooms at all, you are in the hallway. You are late run in a random class and get items from the desks."
        elif len(self.classrooms) == 1:
            search_str += "a classroom."
        else:
            search_str += "a set of " + str(len(self.classrooms)) + \
                          " classrooms."

        return search_str

    def intro(self):
        '''Prints an introduction to the search for items because you are late
        This prompt includes the commands.'''
        print("\nAHHHH! I'm late for class\n")
        print("*runs out the house to catch the bus with an empty backpack*")

        print("\nYou're popular and have friends in many classes. Find and collect any items you find useful for your exam.")
        print("You are already late, and have a CSE231 Final Exam in 10 mins.\n")
        self.print_help()


    def print_help(self):
        '''Prints the valid commands.'''
        print("Use your instincts: ")
        print("*thinks*.. *thinks*.. what to do?!?!?!?!")
        print("*running*")
        print("S or search -- prints a description of the classroom you ran into")
        print("B or backpack - prints a list of items in your backpack")
        print("P pencil or pickup pencil - *mental* instruction to pick up an item called pencil")
        print("DR pencil or drop pencil - *mental* instruction to drop off an item called pencil")
        print("U or up - *mental* instruction to up the hallway to find another classroom")
        print("D or down - *mental* instruction to down the hallway to find another classroom")
        print("R or right - *mental* instruction to right in the hallway to find another classroom")
        print("L or left - *mental* instruction to left in the hallway to find another classroom")
        print("G or giveup - I have no more time, I need to get to class!!!")
        print("H or help - prints this list of options again")
        print()
        print("Remember that uppercase and lowercase SHOULD NOT matter. ")
        print("JUST GRAB WHAT YOU NEED AND GET TO CLASS TO START YOUR FINAL EXAM!!! HURRYYYY!!!")
        print()

    def prompt(self):
        '''Prompts for input and handles it, whether by error message or handling a valid command.
        Returns True as long as the user has not chosen to quit, False if they have.'''

        print("In room {} with course {}".format(self.student.classroom_id,self.classrooms[self.student.classroom_id].course))
        print(self.student)
        user_input = input("Enter a command (H for help): ")
        print()

        # Handle input: split for pickup/drop, capitalization unimportant for commands
        input_list = user_input.split()

        if len(input_list) == 0:
            user_input = "?"  # No command is not a valid command
            return False
        else:
            try:
                command = input_list[0].upper()  # The command
                if len(input_list) > 1:
                    item = input_list[1]
                if command == 'S':
                    self.search()
                elif command == 'B':
                    self.backpack()
                elif command == 'P':
                    self.pickup(item)
                elif command == 'DR':
                    self.drop(item)
                elif command in "UDLR":
                    self.move(command)
                elif command == 'G':
                    print("I have no more time, I need to get to class!!!")
                    return False
                elif command == 'H':
                     self.print_help() 
                else:
                    print("Unfortunately, that's not a valid option.")
                    return False
            except:
                print("Problem with the option or the item.")
                return False
        if self.win():
            return "win"
        return True

    def search(self):
        '''Prints the description of the current room.'''
        current_classroom = self.classrooms[self.student.classroom_id]
        print(current_classroom)

    def backpack(self):
        """ This method prints the student's backpack inventory """
        
        print(self.student)
    

    def pickup(self, item):
        """ The main idea here is to pick up an item from the student
            classroom and add it to the student backpack """
        
        classroom = self.classrooms[ self.student.classroom_id ]
        
        result  = classroom.remove_item( item )
        if result == False:
            pass
        else:
            self.student.add_item( item )
            return True
        

    
    
    def drop(self, item):
        """ Drop an item in a classroom """
        
        result = self.student.remove_item( item )
        if result == False:
            pass
        else:
            self.classrooms[ self.student.classroom_id ].add_item( item )
    

    def move(self, direction):
        """ This function moves the student """
        
        classroom = self.classrooms[ self.student.classroom_id ]
        
        result = classroom.get_room( direction )
        if result == False:
            errMsg = "Unfortunately, you went " + MAP[direction] + " and there was no classroom."
            print(errMsg)
        else:
            self.student.place(result)
            print("You went " + MAP[direction] + " and found a new classroom.")
            
            

    def win(self):
        '''
            WRITE DOCSTRING HERE!
        '''
        winning_backpack = ['cheatsheet', 'eraser', 'paper', 'pencil']
        
        current_classroom = self.classrooms[ self.student.classroom_id ]
        
        if current_classroom.course == "CSE231" and sorted(self.student.backpack) == winning_backpack:
            return True
        else:
            return False
            

    
def main():
    '''
    Prompts the user for a file, then plays that file until the user chooses to give up.
    Does not check formatting of input file.
    '''

    while True:
        try:
            filename = input("Enter a text filename: ")
            escapade = Rush(filename)
            break
        except IOError:
            print("Cannot open file:{}. Please try again.".format(filename))
            continue
    
    escapade.intro()
    escapade.__str__()
    escapade.search()
    
    keep_going = True
    while keep_going:
        keep_going = escapade.prompt()
        if keep_going == 'win':
            break
    if keep_going == 'win':
        print("You succeeded!")
    else:
        print("Thank you for playing")

if __name__ == "__main__":    
    main()