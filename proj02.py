w# -*- coding: utf-8 -*-
 

    ###########################################################

    #  Computer Project #2

    #  Algorithm

    #   Input your customer code

    #   Input how many days you would like to rent the car

    #    Input how many miles the odomoter reading had at the start

    #      Input how many miles the odomoter reading had at the end 

    #      Then it will print you customer summarry

    #      The customer summary will include all your inputs with the math of how much money is due


    ###########################################################

 
import math
BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 

print(BANNER)
PROMPT = input('''\nWould you like to continue (Y/N)? ''')
PROMPT_temp = 0
if PROMPT == "Y":
    while PROMPT == "Y":
            cust_code = input("\nCustomer code (BDW): ")
            if cust_code == "B" or cust_code == "D" or cust_code == "W": 
                if cust_code == "B":    
                    days_float = float(input("\nNumber of days: "))
                    odomoter_start_float = float(input("Odometer reading at the start: "))
                    odomoter_end_float = float(input("Odometer reading at the end:   "))
                    miles_driven = ((odomoter_start_float - odomoter_end_float) - 1000000) / 10 # so that the odometer can reset at 1000000 miles
                    miles_driven_od = math.sqrt(miles_driven**2) # this gets rid of the negative integer
                    cost_B = days_float*40 + miles_driven_od/4
                    print("\nCustomer summary:")
                    print("\tclassification code:", cust_code)
                    print("\trental period (days):", int(days_float))
                    print("\todometer reading at start:",int(odomoter_start_float))
                    print("\todometer reading at end:  ", int(odomoter_end_float))
                    print("\tnumber of miles driven: ", miles_driven_od)
                    print("\tamount due: $", cost_B)
                    PROMPT_temp = input("\nWould you like to continue (Y/N)? ")
                if cust_code == "D":
                    days_float = float(input("\nNumber of days: "))
                    odomoter_start_float = float(input("Odometer reading at the start: "))
                    odomoter_end_float = float(input("Odometer reading at the end:   "))
                    miles_driven = (odomoter_end_float - odomoter_start_float) / 10 # conversion for odometer miles 
                    cost_D = days_float * 60
                    if miles_driven/days_float > 100:
                        average_week = miles_driven/days_float
                        mile_charge_D = (miles_driven - 100 * days_float)/4
                        cost_D = (days_float*60) + (mile_charge_D)
                    print("\nCustomer summary:")
                    print("\tclassification code:", cust_code)
                    print("\trental period (days):", int(days_float))
                    print("\todometer reading at start:",int(odomoter_start_float))
                    print("\todometer reading at end:  ", int(odomoter_end_float))
                    print("\tnumber of miles driven: ", miles_driven)
                    print("\tamount due: $", cost_D)
                    PROMPT_temp = input("\nWould you like to continue (Y/N)? ")
  
                if cust_code == "W":
                    days_float = float(input("\nNumber of days: "))
                    week = float(days_float//7)
                    if days_float % 7: 
                        week +=1
                    week_leftover = week % 7 
                    odomoter_start_float = float(input("Odometer reading at the start:   "))
                    odomoter_end_float = float(input("Odometer reading at the end:   "))
                    cost_W = (week * 190)
                    miles_driven = (odomoter_end_float - odomoter_start_float) / 10
                    if  miles_driven/week <= 900: # this is when th mileage is under 900
                        cost_W = (week * 190)
                    if  1500 >= miles_driven/week > 900: # this is when the mileage exceeds 900 but it is stil under 1500 
                        cost_W = (190 * week) + (100 * week)
                    if  miles_driven/week > 1500: # this is when the mileage exceeds 1500 
                        cost_W = (190 * week) + (200 * week) + (miles_driven - 1500 * week) / 4
                    print("\nCustomer summary:")
                    print("\tclassification code:", cust_code)
                    print("\trental period (days):", int(days_float))
                    print("\todometer reading at start:", int(odomoter_start_float))
                    print("\todometer reading at end:  ", int(odomoter_end_float))
                    print("\tnumber of miles driven: ", miles_driven)
                    print("\tamount due: $", cost_W)
                    PROMPT_temp = input("\nWould you like to continue (Y/N)? ")
                if PROMPT_temp == "N":
                        print("Thank you for your loyalty.")
                        break
                if PROMPT_temp == "Y":
                    continue
            elif not cust_code != "B" or "D" or "W":
                print("\n\t*** Invalid customer code. Try again. ***")
if PROMPT == "N":
    print("Thank you for your loyalty.")


