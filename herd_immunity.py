# Project #5
#
# THis code will write into the MMR.txt file and display the herd immunity
# There are 3 fucntions that will be used
# The minimum value function to find the state with lowest percentage of immunity
# The maximum value function to find the state with the highest percentage of immunity
# The display herd immunity funtion will be used in another function to write into the MMR.txt file with the measles statement

''' This code will take your the MMR.txt file and display the herd immunity'''

def open_file():  
    '''function that opens the file when called in the main'''
    try:
        f_open = input("Input a file name: ")  #asks user to input the file name
        f_pointer = open(f_open)
        return f_pointer
    except FileNotFoundError:
        print("Error, please try again:") #if file name is invalid, will be prompted to try again
        
def get_us_value(fp):
    '''strips the .txt to file to show the states and percentage values'''
    fp.seek(1)
    fp.readline() 
    fp.readline()
    percentage = 0 
    for line in fp:
        if "NA" in line:
            continue
        percentage = float(line[25:].strip()) #strips the percetnatages
        name = line[0:25].strip() #strips the states
        if name == "United States":
            return percentage

def get_min_value_and_state(fp): 
    '''function that finds the lowest percentage for all of the states'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    min_value = 999999999
    min_state = ""
    for line in fp:
        if "NA" in line:
            continue
        try:
            name = line[0:25].strip()
            state = float(line[25:].strip())
            if state < min_value: # if the value for the states is lower than the min value variable then the lowest percentage state will be printed 
                min_value = state
                min_state = name
        except ValueError:
            continue
        
    return min_state, min_value

def get_max_value_and_state(fp): 
    '''function that fins the highest percentage for all of the states'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    max_value = -999999999
    max_state = ""
    for line in fp: 
        if "NA" in line:
            continue
        try:
            name = line[0:25].strip()
            state = float(line[25:].strip())
            if state > max_value:
                max_value = state
                max_state = name
        except ValueError:
            continue
    return max_state, max_value #formats the values into state and the percentage

        
def display_herd_immunity(fp): 
    '''this function displays the herd immunity of the lowest and highest percentages states'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State","Percent"))
    for line in fp:  
        if "NA" in line: 
            continue
        try: 
            percentage = float(line[25:].strip())
            state = line[0:25].strip()
            if percentage < 90:
                print("{:<25s}{:>5.1f}%".format(state, percentage))
        except ValueError:
            continue

def write_herd_immunity(fp):
    '''uses the herd.txt file for displaying the herd immunity percentages'''
    out_file = open("herd.txt", "w") 
    fp.seek(0)
    fp.readline()
    fp.readline()
    print("\nStates with insufficient Measles herd immunity.", file = out_file)
    print("{:<25s}{:>5s}".format("State","Percent"), file = out_file)
    for line in fp:
        if "NA" in line: 
            continue
        try: 
            percentage = float(line[25:].strip())
            state = line[0:25].strip()
            if percentage < 90:
                print("{:<25s}{:>5.1f}%".format(state, percentage), file = out_file)  
        except ValueError:
            continue

def main():    
    '''the main function that displays all of the functions '''
    file_pointer = open_file()
    print()
    header = file_pointer.readline()
    print(header) #prints the first line as the header
    U_value = get_us_value(file_pointer)

    min_state,minimum_value = get_min_value_and_state(file_pointer)  #variable that will be formatted for the print statement
    max_state,maximum_value = get_max_value_and_state(file_pointer)  #variable that will be formatted for the print statement
    
    print("Overall US MMR coverage: {}%".format(U_value)) #adds statement of the average to the final output
    print("State with minimal MMR coverage: {} {}%".format(min_state,minimum_value)) #adds statement for the lowest percentage value
    print("State with maximum MMR coverage: {} {}%".format(max_state,maximum_value)) #adds statement for the highest percentage value
    
    display_herd_immunity(file_pointer)
    write_herd_immunity(file_pointer)
    
if __name__ == "__main__": #needed to run the main function 
    main()    

