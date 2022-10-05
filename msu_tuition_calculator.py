###########################################################
#
#   Computer Project 
#    Ask if resident
#     If resident then will be prompted to provide level
#      If level freshman or sophomore, then will be asked if you're admitted to the college of engineering or james madison college
#       If level junior or sAenior, then will be asked what college you're in and if none then will be asked if you're in the cmse college
#        if non resident then will be asked if international and prompted the same questions as above
#          last question asked will be how mnay credits enrolled in this semester
#          calculates tuition based on rates provided in the chart of the pdf file
#
#
#
###########################################################
BANNER = print("2019 MSU Undergraduate Tuition Calculator.")

ASMSU_Tax = 21
ASMSU_Tax_Int = int(ASMSU_Tax)
FM_Radio_Tax = 3
FM_Radio_Tax_Int = int(FM_Radio_Tax)
State_News_Tax = 5
State_News_Tax_Int = int(State_News_Tax)
JMC_Senate_Tax = 7.50
JMC_Senate_Tax_Int = int(JMC_Senate_Tax)

Resident = input("\nResident (yes/no): ").lower()
while Resident == "yes":
    while True:
        Level = input(
            "Level—freshman, sophomore, junior, senior: ").lower()  # asking what level and is lowercased incase the user inputs uppercase letters
        if Level not in ('freshman', 'sophomore', 'junior', 'senior'):  # inputs have to be one of these in the quotes
            print("Invalid input. Try again.")
        else:
            break  # goes into loop if invalid input
    if Level == "freshman":
        EGR_Admission = input("Are you admitted to the College of Engineering (yes/no): ").lower()
        JMC_Admission = input("Are you in the James Madison College (yes/no): ").lower()
        while True:  # this while loop makes sure that the input is a number and an integer and if it's not then will be prompted to input again
            Credits = input("Credits: ")
            if not Credits.isdigit() or int(Credits) == 0:
                print("Invalid input. Try again.")
            else:
                Credits_Int = int(Credits)  # converted string ot an integer
                break
        if EGR_Admission != "yes" and JMC_Admission != "yes":
            if Credits_Int <= 6:
                tuition = (Credits_Int * 482) + 24
            if 6 < Credits_Int <= 12:
                tuition = (Credits_Int * 482) + 5 + 24
            if 12 <= Credits_Int <= 18:
                tuition = 7230 + 5 + 24  # flate rate
            if Credits_Int > 19:
                tuition = ((
                                       Credits_Int - 18) * 482) + 7230 + 5 + 24  # flat rate + tuition with the taxes of taking 6 credits or higher
            print("Tuition is ${:,.2f}.".format(
                tuition))  # this takes whatever number is printed and formats it so that coma is added in with the number
            PROMPT = input(
                "Do you want to do another calculation (yes/no): ").lower()  # after tuition is printed this will be asked and will stop if you say no or continue if you say "yes"
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ").lower()
                continue  # loops code if user says yes
        if EGR_Admission == "yes":
            if Credits_Int <= 4:  # this inequality serves so that they can be charged on if they're a part time student
                coe_tuition = 402
            if Credits_Int >= 12:
                coe_tuition = 670
            if Credits_Int <= 6:
                tuition = (Credits_Int * 482) + 24 + coe_tuition
            if 6 < Credits_Int < 12:
                tuition = (Credits_Int * 482) + 24 + 5 + coe_tuition
            if 12 <= Credits_Int <= 18:
                tuition = 7230 + 24 + 5 + coe_tuition
            if Credits_Int >= 19:
                tuition = ((Credits_Int * 482) - 18) + 24 + 5 + coe_tuition
            print("Tuition is ${:,.2f}.".format(tuition))
            PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ").lower()
                continue
        if JMC_Admission == "yes":
            if Credits_Int <= 6:
                tuition = (Credits_Int * 482) + 24 + 7.5
            if 6 < Credits_Int <= 12:
                tuition = (Credits_Int * 482) + 5 + 24 + 7.5
            if 12 <= Credits_Int <= 18:
                tuition = 7230 + 5 + 24 + 7.5
            if Credits_Int > 19:
                tuition = ((Credits_Int - 18) * 482) + 7230 + 5 + 24 + 7.5
            print("Tuition is ${:,.2f}.".format(tuition))
            PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ").lower()
                continue
    if Level == "sophomore":
        EGR_Admission = input("Are you admitted to the College of Engineering (yes/no): ").lower()
        JMC_Admission = input("Are you in the James Madison College (yes/no): ").lower()
        while True:
            Credits = input("Credits: ")
            if not Credits.isdigit() or int(Credits) == 0:
                print("Invalid input. Try Again.")
            else:
                Credits_int = int(Credits)
                break
        if EGR_Admission != "yes" and JMC_Admission != "yes":  # if resident answers yes to both questions
            Credits_Int = int(Credits)
            if 1 < Credits_Int < 6:
                Cost = (Credits_Int * 494)
            if 6 < Credits_Int <= 11:
                Cost = (Credits_Int * 494) + 5
            if 12 <= Credits_Int < 18:
                Cost = 7410 + 5
            if Credits_Int > 18:
                Cost = (Credits_Int * 494) + 7410 + 5
            tuition = Cost + FM_Radio_Tax_Int + ASMSU_Tax_Int
            print("Tuition is ${:,.2f}.".format(tuition))
            PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ").lower()
                continue
        if EGR_Admission == "yes":
            if Credits_int <= 4:
                coe_tuition = 402  # charge for the college of engineering if doing part time
            if Credits_Int >= 12:
                coe_tuition = 670  # charge for the college of engineering if doing full time
            if Credits_Int <= 6:
                tuition = (Credits_Int * 494) + 24 + coe_tuition
            if 6 < Credits_int < 12:
                tuition = (Credits_Int * 494) + 24 + 5 + coe_tuition
            if 12 <= Credits_Int <= 18:
                tuition = 7230 + 24 + 5 + coe_tuition
            if Credits_Int >= 19:
                tuition = ((Credits_Int * 494) - 18) + 24 + 5 + coe_tuition
            print("Tuition is ${:,.2f}.".format(tuition))
            PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ").lower()
                continue
        if JMC_Admission == "yes":
            if Credits_Int <= 6:
                tuition = (Credits_Int * 494) + 24 + 7.5
            if 6 < Credits_Int <= 12:
                tuition = (Credits_Int * 494) + 5 + 24 + 7.5
            if 12 <= Credits_Int <= 18:
                tuition = 7230 + 5 + 24 + 7.5
            if Credits_Int > 19:
                tuition = ((Credits_Int - 18) * 494) + 7230 + 5 + 24 + 7.5
            print("Tuition is ${:,.2f}.".format(tuition))
            PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ").lower()
                continue
    if Level == "junior" or Level == "senior":
        Level_Junior_Sciences = input("Enter college as business, engineering, health, sciences, or none: ").lower()
        if Level_Junior_Sciences == 'business' or Level_Junior_Sciences == 'engineering' or Level_Junior_Sciences == 'health' or Level_Junior_Sciences == 'sciences':
            Level_Junior_CMSE = input(
                "Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ").lower()
            while True:
                Credits = input("Credits: ")
                if not Credits.isdigit() or int(Credits) == 0:
                    print("Invalid input. Try again.")
                else:
                    Credits_Int = int(Credits)
                    break
            if Level_Junior_Sciences == "health" or Level_Junior_Sciences == "sciences":
                if Credits_Int <= 4:
                    cohs = 50
                if Credits >= 12:
                    cohs = 100
                if Credits <= 6:
                    tuition = (573 * Credits_Int) + 24 + cohs
                if 6 < Credits_Int < 12:
                    tuition = (Credits_Int * 573) + 24 + 5 + cohs
                if 12 <= Credits_Int <= 18:
                    tuition = (Credits_Int * 573) + 24 + 5 + cohs
                if 12 <= Credits_Int < 18:
                    tuition = 8595 + cohs + 24 + 5
                if Credits_Int >= 19:
                    tuition = ((Credits_Int - 18) * 573) + 8, 595 + 24 + 5
                print("Tuition is ${:,.2f}.".format(tuition))
                PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
                if PROMPT != "yes":
                    break
                if PROMPT == "yes":
                    Resident = input("Resident (yes/no): ").lower()
                    continue  # runs in a loop if yes
            if Level_Junior_Sciences == "business":
                if Credits_Int <= 4:
                    cob = 113
                if Credits_Int >= 12:
                    cob = 226
                if Credits_Int <= 6:
                    tuition = (Credits_Int * 573) + cob + 24
                if 6 < Credits_Int < 12:
                    tuition = (Credits_Int * 573) + 5 + cob + 24
                if 12 <= Credits_Int <= 18:
                    tuition = 8595 + 5 + cob + 24
                if Credits_Int > 18:
                    tuition = ((Credits_Int - 18) * 573) + 8, 595 + 5 + 24 + cob
                print("Tuition is ${:,.2f}.".format(tuition))
                PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
                if PROMPT != "yes":
                    break
                if PROMPT == "yes":
                    Resident = input("Resident (yes/no): ").lower()
                    continue
            if Level_Junior_Sciences == "engineering":
                if Credits_Int <= 4:
                    tuition = 573 * Credits_Int + 24 + 402
                if 5 <= Credits_Int <= 6:
                    tuition = 573 * Credits_Int + 24 + 670
                if 6 < Credits_Int < 12:
                    tuition = (Credits_Int * 573) + 24 + 5 + 670
                if 12 <= Credits_Int <= 18:
                    tuition = 8595 + 5 + 670 + 24
                if Credits_Int >= 19:
                    tuition = ((Credits_Int - 18) * 573) + 8595 + 24 + 5
                print("Tuition is ${:,.2f}.".format(tuition))
                PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
                if PROMPT != "yes":
                    break
                if PROMPT == "yes":
                    Resident = input("Resident (yes/no): ").lower()
                    continue
        if not (
                Level_Junior_Sciences == 'business' or Level_Junior_Sciences == 'engineering' or Level_Junior_Sciences == 'health' or Level_Junior_Sciences == "sciences"):
            Level_Junior_CMSE = input(
                "Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ").lower()
            if Level_Junior_CMSE == "yes":
                JMC_Admission = input("Are you in the James Madison College (yes/no): ").lower()
                while True:
                    Credits = input("Credits: ")
                    if not Credits.isdigit() or int(Credits) == 0:
                        print("Invalid input. Try again.")
                    else:
                        Credits_Int = int(Credits)
                        break
                if Credits_Int <= 4:
                    tuition = 555 * Credits_Int + 24 + 402
                if 5 <= Credits_Int <= 6:
                    tuition = 555 * Credits_Int + 24 + 670
                if 6 < Credits_Int < 12:
                    tuition = 555 * Credits_Int + 670 + 24 + 5
                if 12 <= Credits_Int <= 18:
                    tuition = 8325 + 24 + 5 + 670
                if Credits_Int >= 19:
                    tuition = 8325 + ((Credits_Int - 18) * 555) + 29 + 670
                print("Tuition is ${:,.2f}.".format(tuition))
                PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
                if PROMPT != "yes":
                    break
                if PROMPT == "yes":
                    Resident = input("Resident (yes/no): ")
                    continue
            if Level_Junior_CMSE != "yes":
                Credits = input("Credits: ").isdigit()
                if Credits == True:
                    continue
                if Credits == False:
                    print("Invalid input. Try again.")
                if Credits_Int <= 6:
                    tuition = 555 * Credits_Int + 24
                if 6 < Credits_Int < 12:
                    tuition = 555 * Credits_Int + 24 + 5
                if 12 <= Credits_Int <= 18:
                    tuition = 8325 + 24 + 5
                if Credits_Int >= 18:
                    tuition = 8325 + ((Credits_Int - 18) * 555) + 24 + 5
                print("Tuition is ${:,.2f}.".format(tuition))
                PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
                if PROMPT != "yes":
                    break
                if PROMPT == "yes":
                    Resident = input("Resident (yes/no): ")
                    continue
while Resident != "yes":  # if the resident says no and will be prompted if they are an international student
    International_Resident = input("International (yes/no): ").lower()
    while True:
        Level = input("Level—freshman, sophomore, junior, senior: ").lower()
        if Level not in ('freshman', 'sophomore', 'junior', 'senior'):
            print("Invalid input. Try again")
        else:
            break
    if Level == "freshman" or Level == "sophomore":  # repeats same prompts as if they are a resident, just with different fees and rates
        EGR_Admission = input("Are you admitted to the College of Engineering (yes/no): ").lower()
        while True:
            Credits = input("Credits: ")
            if not Credits.isdigit() or int(Credits) == 0:
                print("Invalid input. Try again.")
            else:
                Credits_Int = int(Credits)
                break
        if EGR_Admission != "yes":
            if Credits_Int <= 4:
                tuition = 1325.50 * Credits_Int + 375 + 24  # 375 is the international rate if part time
            if 5 <= Credits_Int <= 6:
                tuition = 1325.50 * Credits_Int + 24 + 750  # 750 is the international rate if full time
            if 6 < Credits_Int < 12:
                tuition = 1325.50 * Credits_Int + 24 + 5 + 750
            if 12 <= Credits_Int < 18:
                tuition = 19883 + 5 + 750 + 24
            if Credits_Int >= 19:
                tuition = 24 + 5 + 750 + 19883 + ((Credits_Int - 18) * 1325.50)
            print("Tuition is ${:,.2f}.".format(tuition))
            PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ")
                continue
        if EGR_Admission == "yes":
            if Credits_Int <= 4:
                tuition = 1325.50 * Credits_Int + 375 + 24 + 402
            if 5 <= Credits_Int <= 6:
                tuition = 1325.50 * Credits_Int + 24 + 750 + 670
            if 6 < Credits_Int < 12:
                tuition = 1325.50 * Credits_Int + 24 + 5 + 750 + 670
            if 12 <= Credits_Int < 18:
                tuition = 19883 + 5 + 750 + 24 + 670
            if Credits_Int >= 19:
                tuition = 24 + 5 + 750 + 670 + 19883 + ((Credits_Int - 18) * 1325.50)
            print("Tuition is ${:,.2f}.".format(tuition))
            PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ")
                continue
    if Level == "junior" or Level == "senior":
        EGR_Admission = input("Are you admitted to the College of Engineering (yes/no): ").lower()
        while True:
            Credits = input("Credits: ")
            if not Credits.isdigit() or int(Credits) == 0:
                print("Invalid input. Try again.")
            else:
                Credits_Int = int(Credits)
                break
        if EGR_Admission == "no":
            if Credits_Int <= 4:
                coe_tuition = 402
            if Credits_Int <= 12:
                coe_tuition = 670
            if Credits_Int <= 6:
                tuition = Credits_Int * 1366.75 + 24 + coe_tuition + 750
            if 6 < Credits_Int < 12:
                tuition = Credits_Int * 1366.75 + 24 + coe_tuition + 750 + 5
            if 12 <= Credits_Int <= 18:
                tuition = 20786 + 24 + 5 + coe_tuition
            if Credits_Int > + 19:
                tuition = 20786 + ((Credits_Int - 18) * 1366.75) + coe_tuition + 24 + 5
            print("Tuition is ${:,.2f}.".format(tuition))
            PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ")
                continue
        if EGR_Admission == "yes":
            if Credits_Int <= 4:
                coe_tuition = 402
            if Credits_Int >= 12:
                coe_tuition = 670
            if Credits_Int <= 6:
                tuition = (1385.75 * Credits_Int) + 24 + coe_tuition
            if 6 < Credits_Int < 12:
                tuition = (1385.75 * Credits_Int) + 24 + 5 + coe_tuition
            if 12 <= Credits_Int <= 18:
                tution = 20786 + 24 + 5 + coe_tuition
            if Credits_Int >= 19:
                tuition = 20786 + ((Credits_Int - 18) * 1385.75) + 24 + 5 + coe_tuition
            PROMPT = input("Do you want to do another calculation (yes/no): ").lower()
            if PROMPT != "yes":
                break
            if PROMPT == "yes":
                Resident = input("Resident (yes/no): ")
                continue
