# =============================================================================
# Project 8
# Working with Video Games Sales Data
# =============================================================================

import csv
import pylab
from operator import itemgetter

def open_file():
    '''
        This function opens a file and returns a file pointer. It repeatedly
        prompts for a filename until one is opened.
    '''
    
    while True:
        filename = input("Enter filename: ")
        try:
            fp = open(filename, encoding = "utf-8")
            break                                       #If the file was successfully opened
        except FileNotFoundError:
            print("File not found! Please try again!")  #Otherwise try again
    
    return fp
            

def sort_dict( a_dictionary ):
    '''
        This function sorts a dicitonary based on the instructions given
        in the read_file function: we sort alphabetically by keys and 
        we sort the values by the last element in each tuple in descending
        order
    '''
    new_dictionary = {}
    sorted_keys = sorted( a_dictionary.keys() )
    
    for  key in sorted_keys:
        
        new_value = sorted( a_dictionary[key], key=itemgetter(-1), reverse = True )
        new_dictionary[key] = new_value
    
    return new_dictionary
    
    
    


def read_file(fp):
    '''
        This function reads a game videos sales file and builds three 
        dictionaries
    '''
    
    #INITIALIZE THE DICTIONARIES THAT WILL BE LATER POPULATED AND RETURNED
    d1 = {}
    d2 = {}
    d3 = {}
    
    fp = csv.reader(fp)         #csv.reader preprocesses a csv file pointer
    next(fp)                    #This line helps us skip the header in the file
    
    for line in fp:        #line_list is a list of all the tokens on an individual line
        #We extract the data we are into
        name           =     line[0].strip().lower()
        platform       =     line[1].strip().lower()
        genre          =     line[3].strip().lower()
        publisher      =     line[4].strip().lower()
        
        try:
            year           =     int(line[2])
            na_sales       =     float(line[5]) * 1000000
            europe_sales   =     float(line[6]) * 1000000
            japan_sales    =     float(line[7]) * 1000000
            other_sales    =     float(line[8]) * 1000000
            global_sales   =     na_sales + europe_sales + japan_sales + other_sales
        except ValueError:
            continue
        
        #The three tuples to add
        tup1 = (name, platform, year, genre, publisher, global_sales)
        tup2 = (genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales)
        tup3 = (publisher, name, year, na_sales, europe_sales, japan_sales, other_sales, global_sales)
        
        if name not in d1:
            d1[name] = [tup1]
        else:
            d1[name].append(tup1)
        
        if genre not in d2:
            d2[genre] = [tup2]
        else:
            d2[genre].append(tup2)
        
        if publisher not in d3:
            d3[publisher] = [tup3]
        else:
            d3[publisher].append(tup3)
    
    #Once we are done building the dictionaries, we sort them using quite a complex schema
    d1 = sort_dict( d1 )
    d2 = sort_dict( d2 )
    d3 = sort_dict( d3 )
    
    return d1, d2, d3
    
        
        

def get_data_by_column(D1, indicator, c_value):
    '''
        This function returns a list of tuples determined by either the 
        indicator parameter or the c_value
    '''
    
    list_of_tupl = []                 #Initialize the list tha will be returned later
    
    if indicator == "year":
        for key in D1:                #Iterate over the dictionary D1
            for tupl in D1[key]:
                if tupl[2] == c_value:
                    list_of_tupl.append( tupl )
    
        list_of_tupl.sort(key=itemgetter(5), reverse = True)  #Sort alphabetically
        list_of_tupl.sort(key=itemgetter(1))
        return list_of_tupl
    
    if indicator == "platform":
        for key in D1:                #Iterate over the dictionary D1
            for tupl in D1[key]:
                if tupl[1] == c_value:
                    list_of_tupl.append( tupl )
    
        list_of_tupl.sort(key=itemgetter(5), reverse = True)  #Sort alphabetically
        list_of_tupl.sort(key=itemgetter(2))
        return list_of_tupl
        
    

def get_publisher_data(D3, publisher):
    '''
        This function iterates through the dictionary 3 and returns a list
        of tuples
    '''
    
    list_of_tupl = []
    for key in D3:
        for tupl in D3[key]:
            if tupl[0] == publisher:
                list_of_tupl.append( tupl )
    
    list_of_tupl.sort(key=itemgetter(1))
    list_of_tupl.sort(key=itemgetter(7), reverse = True)
    
    return list_of_tupl
    
    


def display_global_sales_data(L, indicator):
    '''
        This function prints a table of all the global game sales stored
        in L1 by either all platforms in a single year or all years for 
        a single platform
    '''
    
    
    h1 = ['Name', 'Platform', 'Genre', 'Publisher', 'Global Sales']
    h2 = ['Name', 'Year', 'Genre', 'Publisher', 'Global Sales']
    
    if indicator == "year":
        print("\n{:^80s}".format("Video Game Sales in " + str(L[0][2])))
        #Display the header
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format(h1[0], h1[1], h1[2],
                                                      h1[3], h1[4]))
        global_sales_sum = 0
        #This for loop is used to display all the individuals rows
        for tup in L:
            global_sales_sum += tup[5]
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(
                    tup[0][:25], tup[1], tup[3], tup[4][:25], tup[5]))
            
        #Display the total global sales row
        print("\n{:90s}{:<12,.02f}".format("Total Sales", global_sales_sum))
    
    
    if indicator == "platform":
        print("\n{:^80s}".format("Video Game Sales for " + str(L[0][1])))
        #Display the header
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format(h2[0], h2[1], h2[2],
                                                      h2[3], h2[4]))
        global_sales_sum = 0
        #This for loop is used to display all the individuals rows
        for tup in L:
            global_sales_sum += tup[5]
            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(
                    tup[0][:25], str(tup[2]), tup[3], tup[4][:25], tup[5]))
            
        #Display the total global sales row
        print("\n{:90s}{:<12,.02f}".format("Total Sales", global_sales_sum))
    
    
    

    

def get_genre_data(D2, year):
    '''
        As the previous ones, this function iterates through D2 and returns
        a list of tuples.
    '''
    
    list_of_tupl = []
    for key in D2:
        count             = 0
        total_na_sales    = 0
        total_eur_sales   = 0
        total_jpn_sales   = 0
        total_other_sales = 0
        toal_global_sales = 0
        for tupl in D2[key]:
            #We are on a specific genre 
            if tupl[1] == year:
                count             += 1
                total_na_sales    += tupl[2]
                total_eur_sales   += tupl[3]
                total_jpn_sales   += tupl[4]
                total_other_sales += tupl[5]
                toal_global_sales += tupl[6]
                
        if count != 0:
            list_of_tupl.append( (key, count, total_na_sales, 
                                  total_eur_sales, total_jpn_sales,
                                  total_other_sales, toal_global_sales))
    
    list_of_tupl.sort()
    list_of_tupl.sort( key=itemgetter(6), reverse = True)
    
    return list_of_tupl
    
                
            
    
  
def display_genre_data(genre_list):
    '''
        This function displays the genre data
    '''
    
    print("\nRegional Video Games Sales per Genre")
    
    h = ['Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    #Display the header first
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(h[0], h[1], h[2],
                                                        h[3], h[4], h[5]))
    global_sales_sum = 0
    for tup in genre_list:
        global_sales_sum += tup[6]
        print("{:15s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".
              format(tup[0], tup[2], tup[3], tup[4], tup[5], tup[6]))
    
    #Display the last row
    print("\n{:75s}{:<15,.02f}".format("Total Sales", global_sales_sum))
    
    

def display_publisher_data(pub_list):
    '''
        This function displays the publisher data
    '''
    pub = pub_list[0][0]
    
    print("\nVideo Games Sales for {}".format(pub))
    
    h = ['Title', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    print("{:30s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(h[0],h[1],h[2],
                                                        h[3],h[4],h[5]))
    global_sales_sum = 0
    for tup in pub_list:
        global_sales_sum += tup[7]
        print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(tup[1][:25], tup[3], tup[4], tup[5], tup[6], tup[7]))
    
    print("\n{:90s}{:<15,.02f}".format("Total Sales", global_sales_sum))
        

def get_totals(L, indicator):
    '''
        This function receives a list of tuples received by the get_data_by_
        column function. It returns two lists
    '''
    
    l_as_dict = {}       #Use L to build a dictionary
    
    if indicator == "year":
        #Build a dictionary with platforms as keys
        for tupl in L:
            platform_name = tupl[1]
            if platform_name in l_as_dict:
                l_as_dict[platform_name] += tupl[5]
            else:
                l_as_dict[platform_name] = tupl[5]
                
    if indicator == "platform":
        #Build a dictionary with years as keys
        for tupl in L:
            year = tupl[2]
            if year in l_as_dict:
                l_as_dict[year] += tupl[5]
            else:
                l_as_dict[year] = tupl[5]
    
    l_as_dict_sorted = sorted(l_as_dict.items())
    L1 = [i[0] for i in l_as_dict_sorted]
    L2 = [i[1] for i in l_as_dict_sorted]
        
    return L1, L2
                
            

def prepare_pie(genres_list):
    '''
        This function receives a list of global sales per genre 
        for a particulary year. It returns two lists that will help
        to plot
    '''
    
    list_of_tupl = []         #TWe extract the genre and the global sales in this list
    
    for tupl in genres_list:
        list_of_tupl.append(  (tupl[0], tupl[-1])  )
    
    list_of_tupl.sort( key=itemgetter(1), reverse = True )
    L1 = [i[0] for i in list_of_tupl]
    L2 = [i[1] for i in list_of_tupl]
    
    return L1, L2
    


def plot_global_sales(x,y,indicator, value):
    '''
        This function plots the global sales per year or platform.
        
        parameters: 
            x: list of publishers or year sorted in ascending order
            y: list of global sales that corresponds to x
            indicator: "publisher" or "year"
            value: the publisher name (str) or year (int)
        
        Returns: None
    '''
    
    if indicator == 'year':    
        pylab.title("Video Game Global Sales in {}".format(value))
        pylab.xlabel("Platform")
    elif indicator == 'platform':    
        pylab.title("Video Game Global Sales for {}".format(value))
        pylab.xlabel("Year")
    
    pylab.ylabel("Total copies sold (millions)")
    
    pylab.bar(x, y)
    pylab.show()

def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.
        
        parameters: 
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order 
            year: the year of the genre data (int)
        
        Returns: None
    '''
            
    pylab.pie(values, labels=genre,autopct='%1.1f%%')
    pylab.title("Video Games Sales per Genre in {}".format(year))
    pylab.show()
    
def main():
    
    #Open the file
    fp = open_file()
    d1,d2,d3 = read_file(fp)
    

    
    #Menu options for the program
    MENU = '''Menu options
    
    1) View data by year
    2) View data by platform
    3) View yearly regional sales by genre
    4) View sales by publisher
    5) Quit
    
    Enter choice: '''
    
    choice = input(MENU)
    while choice != '5':
        #An invalid choice
        if choice not in ["1","2","4","3"]:
            print("Invalid option. Please Try Again!")
        
        #Option 1: Display all platforms for a single year
        if choice == "1":
            #Prompt for a year
            try:
                year = int(input("Enter year: "))
                data = get_data_by_column(d1, 'year', year)
                #If data is empty, we show an error message
                if data == []:
                    print("The selected year was not found in the data.")
                else:
                    display_global_sales_data(data, 'year')
                    #Does the user want to plot?
                    plot = input("Do you want to plot (y/n)? ")
                    if plot == "y":
                        l1, l2 = get_totals(data, 'year')
                        plot_global_sales(l1, l2,'year', year)
    
            except ValueError:
                print("Invalid year")
        
        if choice == "2":
            #Prompt for a platform
            platform = input("Enter platform: ")
            if platform.isalpha():
                data = get_data_by_column(d1, 'platform', platform)
                #If data is empty, we show an error message
                if data == []:
                    print("The selected platform was not found in the data.")
                else:
                    display_global_sales_data(data, 'platform')
                    #Does the user want to plot?
                    plot = input("Do you want to plot (y/n)? ")
                    if plot == "y":
                        l1, l2 = get_totals(data, 'platform')
                        plot_global_sales(l1, l2,'platform', platform)
    
            else:
                print("Invalid platform")
            
        
        if choice == "3":
            try:
                year = int(input("Enter year: "))
                data = get_genre_data(d2, year)
                if data == []:
                    print("The selected year was not found in the data.")
                else:
                    display_genre_data(data)
                    plot = input("Do you want to plot (y/n)? ")
                    if plot == "y":
                        l1, l2 = prepare_pie(data)
                        plot_genre_pie(l1, l2, year)
                        
            except ValueError:
                print("Invalid year")
                

        #Option 4: Display publisher data
        if choice == "4":
            # Enter keyword for the publisher name
            keyword = input("Enter keyword for publisher: ")
                
            # search all publisher with the keyword
            match = []
            for publisher_i in d3.keys():
                if keyword in publisher_i:
                    match.append( publisher_i )  #We are performing a linear search
  
    
            # print the number of matches found with the keywords
            if len(match) > 1:    
                print("There are {} publisher(s) with the requested keyword!".format(len(match)))
                for i,t in enumerate(match):
                    print("{:<4d}{}".format(i,t))
                        
                # PROMPT USER FOR INDEX
                try:
                    index = int(input("Select the index for the publisher to use: "))
                except ValueError:
                    pass
                
                try:
                    publisher = match[index]
                    data = get_publisher_data(d3, publisher)
                    #print(data)
                    display_publisher_data(data)
                    
                except IndexError:
                    pass
                
                        
            else:
                print('No publisher name containing "{}" was found!'.format(keyword))
        

        choice = input(MENU)
    
    print("\nThanks for using the program!")
    print("I'll leave you with this: \"All your base are belong to us!\"")

if __name__ == "__main__":
    main()
