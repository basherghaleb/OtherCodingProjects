# =============================================================================
# Project 9: Doing some analysis on a NCOVID-19 Dataset
# =============================================================================

import csv
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from operator import itemgetter


def open_file():
    """ This funtion opens a file and returns the file pointer. It 
        repeatedely prompts for a filename until one is successfully
        opened """
        
    while True:
        try:
            filename = input("Data file: ")
            if not filename:
                return open("ncov.csv")   #In the case no filename was provided
            else:
                return open(filename)
        except FileNotFoundError:
            print("Error. Try again.")  #File couldn't be found
    


def build_dictionary(fp):
    """ This function takes as argument the file pointer returned by the 
        function above and builds a quite complex dictionary """
    
    dictionary = {}   #Initialize the dictionary
    reader = csv.reader( fp )
    next(reader)                #Skip the first line in the csv file
    
    for row in reader:
        row = [i.strip() for i in row]  #Do a bit of cleanup in each cell
        #Extract the data
        country = row[2]
        area    = row[1]
        if area == "":
            area = "N/A"    #For any missing area, we put "N/A"
        last_up = row[3]
        cases   = int(row[4])
        deaths  = int(row[5])
        reco    = int(row[6])
        
        #Build the tupl
        datagr  = (last_up, cases, deaths, reco)
        
        #Populate the dictionary with the data
        if country in dictionary:  #If that country already exists
            new_area_dict = {area : datagr}
            dictionary[country].append(new_area_dict)
        else:
            new_area_dict = {area : datagr}
            dictionary[country] = [new_area_dict] #If not, make some place for
            #it
    
    return dictionary
            
        
   
    

def top_affected_by_spread(master_dict):
    """ This function returns a list of the top 10 countries with the 
        most areas affected """
    
    dictionary = {}  #It will have coutries as keys and the number of 
    #areas with cases as values
    
    for country in master_dict:
        dictionary[country] = len(master_dict[country]) 
    
    #We need to sort the data by the the number of areas 
    
    result = sorted(dictionary.items(), key=itemgetter(0))
    result = sorted(result, key=itemgetter(1), reverse = True)
    

    
    return result[:10] #Just the top 10

            
        
    
def top_affected_by_numbers(master_dict):
    """ This function produces the list of the top 10 countries with the most 
        total people affected within every country provided the dictionary
        returned by the function above """
        
    dictionary = {}   #The dictionary will have countries as keys and their
       #respective number of cases as values
      
    for country in master_dict:
        dictionary[country] = 0  #Initialize the cases coun to 0
        for dic in master_dict[country]:
            dictionary[country] += list(dic.values())[0][1]
    
    result = sorted(dictionary.items(), key=itemgetter(1), reverse = True )
    
    return result[:10]  #Return the top 10

def is_affected(master_dict, country):
    """ This function returns a boolean based on whether or not the 
        country specified in the  argument is affected or not """
    
    for country_i in master_dict:
        if country_i.lower() == country.lower():
            return True #The country does exist in the dictionary
    
    return False


def plot_by_numbers(list_of_countries, list_of_numbers):
    '''
        This function plots the number of areas/people inffected by country.
        
        parameters: 
            list_of_countries: list of countries
            list_of_numbers: list of the number of areas/people inffected
            
        Returns: None
    '''
    fig, ax = plt.subplots()
    
    x_pos = [i for i, _ in enumerate(list_of_countries)]
    
    ax.barh(x_pos, list_of_numbers, align='center', color='red')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(list_of_countries)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Novel Coronavirus statistics')
    
    plt.show()


def affected_states_in_country(master_dict, country):
    """ This function returns a list of all the affected regions in a 
        country """
    
    for country_i in  master_dict:
        if country_i.lower() == country.lower(): #We have found a match
            areas_set = set()
            for dic in master_dict[country_i]:
                areas_set.add(list(dic.keys())[0])
            return areas_set
    #We reach this stage if there was no match   
    return set()



def main():
    

    BANNER = '''
.__   __.   ______   ______   ____    ____
|  \ |  |  /      | /  __  \  \   \  /   /
|   \|  | |  ,----'|  |  |  |  \   \/   / 
|  . `  | |  |     |  |  |  |   \      /  
|  |\   | |  `----.|  `--'  |    \    /   
|__| \__|  \______| \______/      \__/  
    '''
    print(BANNER)
    MENU = ''' 
[1] Countries with most areas infected
[2] Countries with most people affected
[3] Affected areas in a country
[4] Check if a country is affected
[5] Exit

Choice: '''
    #Open the file and build the dictionary
    D = build_dictionary(open_file())

    while True: #The interaction starts
        
        choice = input(MENU)
        if choice == "1":
            data = top_affected_by_spread(D)
            print("{:<20s} {:15s}".format("Country", "Areas affected"))
            print("-"*40)
            for entry in data:
                print("{:<20s} {:5d}".format(entry[0], entry[1]))
            plot_answer = input('Plot? (y/n) ')
            if plot_answer == "y":
                list_of_countries = [i[0] for i in data][:5]
                list_of_numbers   = [i[1] for i in data][:5]
                plot_by_numbers(list_of_countries, list_of_numbers)
                
            
            
        elif choice == "2":
            data = top_affected_by_numbers(D)
            print("{:<20s} {:15s}".format("Country", "People affected"))
            print("-"*40)
            for entry in data:
                print("{:<20s} {:5d}".format(entry[0], entry[1]))
            plot_answer = input('Plot? (y/n) ')
            if plot_answer == "y":
                list_of_countries = [i[0] for i in data][1:6]
                list_of_numbers   = [i[1] for i in data][1:6]
                plot_by_numbers(list_of_countries, list_of_numbers)
            
            
        elif choice == "3":
            country = input("Country name: ")
            print("-"*30)
            areas   = affected_states_in_country(D, country)
            if areas == set():
                print("Error. Country not found.")
            else:
                areas = sorted( list(areas) )
                print("{:<30s}".format("Affected area"))
                print("-"*30)
                for i in range(len(areas)):
                    print("[{:02d}] {:<30s}".format(i+1, areas[i]))
                    
                    
        elif choice == "4":
            country = input("Country name: ")
            print("-"*30)
            if is_affected(D, country) == True:
                print("{} is affected.".format(country))
            else:
                print("{} is not affected.".format(country))
            
        elif choice == "5":
            print("Stay at home. Protect your community against COVID-19")
            break
        else:
            print("Error. Try again.")
         
if __name__ == "__main__":    
    main()