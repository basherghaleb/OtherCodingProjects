 

    ###########################################################
    #  Project #4
    #
    #  Calculator
    #    Displayed with options for 4 calculations using functions operation
    #    Pi
    #    Sin
    #      Cosin
    #       Sum of natural numbers
    #       when option is selected, allows user to input any number they like
    #       displays the math module approximation, my approximation, and the difference of the two 
    #       to show the difference and how close my approximation is
    ###########################################################



import math

EPSILON = (1.0* 10**-7)

def display_options(): #function that displays the menu
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the sum of squares of the first N natural numbers.
             B. Display the approximate value of Pi.
             C. Display the approximate value of the sine of X.
             D. Display the approximate value of the cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
       
    print(MENU)

def float_check(num): #function that checks to see if the input is a float
    count = 0
    for i in range (0,len(num)):
        if num [i] == '.':
            count += 1
    if count > 1 or num.find('e') != -1:
        return False
    else:
        return True
   
def sum_natural_squares(n): #function that calculates the sum of the natural squares that come before the number added together
    '''Approximation for the sum of natural squares'''
    try:
        n = int(n)
        if n == 0:
            return None
        s = 0
        for i in range(n+1):
            s += i*i
        return s
    except:
        None

def approximate_pi(): #function that approximates pi
    '''Approximation of pi using the equation'''
    total = 0
    n =  0
    pi = 0
    while True:
        pi = (((-1)**n)/((2 * n) + 1))
        EPSILON = (1.0* 10**-7)
        if not (abs(pi) > EPSILON):
            break
        total += pi
        n += 1
    return round(total * 4, 10)
   
def approximate_sin(x): #function that approximates the product of sin with the number being inputed
    '''Approximation of sin using the equation and factorial'''
    try:
        x = float(x)
        sm = 0.0
        n = 0.0
        total = (x**(2.0*n+1.0))*((-1.0)**n)/(math.factorial(2.0*n+1.0))
        EPSILON = (1.0* 10**-7)
        while (abs(total) >= EPSILON):
            sm = sm + total
            n = n + 1.0
            total = (x**(2.0*n+1.0))*((-1.0)**n)/(math.factorial(2.0*n+1.0))
        return round(sm,10)
    except:
        return None
   
   
def approximate_cos(x): #function that approximates the product of cosin with the number inputed
    '''Approximation of cosin using the equation and factorial'''   
    try:
        x = float(x)
        sm = 0.0
        n = 0.0
        total = (x**(2.0*n)*((-1.0)**n))/(math.factorial(2.0*n))
        EPSILON = (1.0* 10**-7)
        while (abs(total) >= EPSILON):
            sm = sm + total
            n = n + 1.0
            total = (x**(2.0*n)*((-1.0)**n))/(math.factorial(2.0*n))
        return round(sm,10)
    except:
        return None
   
def main(): #main function
    display_options() #calling the display function
    PROMPT = input("\n\tEnter option: ")
    while PROMPT != PROMPT.isdigit() or PROMPT in ("A" or "B" or "C" or "D" or "M" or "X" or "a" or "b" or "c" or "d" or "m" or "x"):
       #if the prompt is one of the options whether uppercase or lowercase
        if PROMPT == "A" or PROMPT == "a":
            a_input = input("\nEnter N: ") 
            if not a_input.isdigit() or int(a_input) == 0:
                print("\n\tError: N was not a valid natural number. [{}]".format(a_input.upper())) #uppercases the wrong input
                PROMPT = input("\n\tEnter option: ")
                continue
            else:
                a_int = int(a_input)
                print("The sum:", sum_natural_squares(a_int)) #calls the fucntion for the sum of natural squares with the input
                PROMPT = input("\n\tEnter option: ") #goes into loop when prompted the menu options
                continue 
           
        elif PROMPT == "B" or PROMPT == "b":
            print("\n\tApproximation: {:.10f}".format(approximate_pi())) #calls the approximate function
            print("\tMath module:   {:.10f}".format(math.pi)) #calculates pi using math module
            print("\tdifference:    {:.10f}".format(abs(approximate_pi() - math.pi))) #finds the difference between my approximation and math module pi
            PROMPT = input("\n\tEnter option: ")
            continue
           
        elif PROMPT == "C" or PROMPT == "c":
            c_input = input("\n\tEnter X: ")
            if c_input.isalpha():
                print("\n\tError: X was not a valid float. [{}]".format(c_input))
                PROMPT = input("\n\tEnter option: ")
                continue
            if float_check(c_input) == True: #calls float check function for sin
                c_float = float(c_input)
                print("\n\tApproximation: {:.10f}".format(approximate_sin(c_float))) 
                print("\tMath module:   {:.10f}".format(math.sin(c_float))) 
                print("\tdifference:    {:.10f}".format(abs((approximate_sin(c_float)) - math.sin(c_float)))) 
                PROMPT = input("\n\tEnter option: ")
                continue
            if not c_input.isdigit():
                print("\n\tError: X was not a valid float. [{}]".format(c_input))
                PROMPT = input("\n\tEnter option: ")
                continue
            if c_input == "0":
                c_float = float(c_input)
                print("\n\tApproximation: {:.10f}".format(approximate_sin(c_float))) #calls my sin approximation with the input tested
                print("\tMath module:   {:.10f}".format(math.sin(c_float))) #calculates the sin math module with the input
                print("\tdifference:    {:.10f}".format(abs((approximate_sin(c_float)) - math.sin(c_float)))) #find the difference between my sin approximation and math module sin
                PROMPT = input("\n\tEnter option: ")
                continue
            else:
                c_float = float(c_input)
                print("\n\tApproximation: {:.10f}".format(approximate_sin(c_float)))
                print("\tMath module:   {:.10f}".format(math.sin(c_float)))
                print("\tdifference:    {:.10f}".format(abs((approximate_sin(c_float)) - math.sin(c_float))))
                PROMPT = input("\n\tEnter option: ")
                continue
           
        elif PROMPT == "D" or PROMPT == "d":
            d_input = input("\n\tEnter X: ")
            if d_input.isalpha():
                print("\n\tError: X was not a valid float. [{}]".format(d_input))
                PROMPT = input("\n\tEnter option: ")
                continue
            if float_check(d_input) == True: #calls float check function for cosine
                d_float = float(d_input) 
                print("\n\tApproximation: {:.10f}".format(approximate_cos(d_float))) #calls my cos approximation with the input tested
                print("\tMath module:   {:.10f}".format(math.cos(d_float))) #calculates the cosine math module with the input
                print("\tdifference:    {:.10f}".format(abs((approximate_cos(d_float)) - math.cos(d_float)))) #find the difference between my cosine approximation and math module cosine
                PROMPT = input("\n\tEnter option: ")
                continue
            if not d_input.isdigit():
                print("\n\tError: X was not a valid float. [{}]".format(d_input))
                PROMPT = input("\n\tEnter option: ")
                continue
            if d_input == "0":
                d_float = float(d_input)
                print("\n\tApproximation: {:.10f}".format(approximate_sin(d_float)))
                print("\tMath module:   {:.10f}".format(math.cos(d_float)))
                print("\tdifference:    {:.10f}".format(abs((approximate_cos(d_float)) - math.cos(d_float))))
                PROMPT = input("\n\tEnter option: ")
                continue
            else:
                d_float = float(d_input)
                print("\n\tApproximation: {:.10f}".format(approximate_cos(d_float)))
                print("\tMath module:   {:.10f}".format(math.cos(d_float)))
                print("\tdifference:    {:.10f}".format(abs((approximate_cos(d_float)) - math.cos(d_float))))
                PROMPT = input("\n\tEnter option: ")
                continue
               
        elif PROMPT == "M" or PROMPT == "m":  #displays options when m is inputed
            display_options()
            PROMPT = input("\n\tEnter option: ")
            continue
       
        elif PROMPT == "X" or PROMPT == "x": #stops code when x is inputed
            print('Hope to see you again.') 
            break
       
        elif PROMPT != "A" and PROMPT != "B" and PROMPT != "C" and PROMPT != "D" and PROMPT != "M" and PROMPT != "X" and PROMPT != "a" and PROMPT != "b" and PROMPT != "c" and PROMPT != "d" and PROMPT != "m" and PROMPT != "x" :
            print("\nError:  unrecognized option [{}]".format(PROMPT.upper())) #if neither of options is inputed, will be prompted the menu options again
            display_options()
            PROMPT = input("\n\tEnter option: ")
            continue
        PROMPT = input("\n\tEnter option: ") 
if __name__ == "__main__": #needed to run the main function
    main()
