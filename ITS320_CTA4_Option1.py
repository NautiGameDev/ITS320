#-------------------------------------------
# Program Name: ITS320_CTA4_Option1
# Author: Chris Russell
# Date: 7/1/24
#-------------------------------------------
# Pseudocode:
# The program sets-up a while loop.
# A combination of For loop and While loop is used to ensure the user enters a number. If the input isn't a number, the user is prompted again for another number.
# Each input is appended to a list, which is then sorted in numerical order.
# The list is passed through a function that returns the total of all the numbers.
# The total is then used to calculate the average.
# The minimum and maximum numbers are displayed based on the first and last index of the list.
# The list is passed through a new function that calculates the interest of each number and returns a new list.
# A for loop is created to print the interest values and their respected original value.
# A new while loop is created to ask user for input on repetition of the program or termination of the program.
#-------------------------------------------
# Program Inputs: Five floating point values
# Program Outputs: The total, average, maximum, minimum and interest for the set of values.
#-------------------------------------------

#Bool to enable the main program loop
active = True

#Calculates the total of all numbers in the list and returns the amount.
def calc_total(numb):
    total = 0
    for n in numb:
        total += n

    return total

#Calculates the interest of all numbers in the list and returns a second list of interest values
def calc_interest(numb):
    interest_numbers = []

    for n in numb:
        interest_value = n + (n*0.2)
        interest_numbers.append(interest_value)

    return interest_numbers


print("Enter 5 numbers.")

#Core program loop
while active:
    numbers = [] #Numbers list to save user input
    
    for i in range(5): #For loop to run input request 5 times
        print("Enter a number (", i+1, " of 5)")

        #While loop with try/except to ensure the user's input is a number. If not it will reprompt the user for a number without continuing in the program.
        get_input = True
        
        while get_input:
            try:
                value = float(input())
                get_input = False #Ends the while loop to validate the user has entered a number
                print("You entered: ", value)
                numbers.append(value)
            except:
                print("Try again. Please, only enter numbers.")


    numbers.sort() #Sorts the list of inputs in numerical order

    #Calculates needed equations
    total = calc_total(numbers)
    average = total / len(numbers)
    minimum = numbers[0]
    maximum = numbers[len(numbers) - 1]
    interest = calc_interest(numbers)

    #Prints the calculated values
    print("Total: ", total)
    print("Average: ", average)
    print("Minimum: ", minimum)
    print("Maximum: ", maximum)

    #For loop to print the interest values and their respected numbers
    for i, v in enumerate(interest):
        print("The interest value of ", numbers[i], " is ", v)


    #Seeks user input Y or N to repeat or terminate the program. While loop is used to ensure only Y or N can be entered to leave the loop.
    get_menu_input = True

    while get_menu_input:
        menu_input = input("Repeat program? (Y/N)")

        if menu_input == "n" or menu_input == "N": #Terminates program by ending core program loop
            get_menu_input = False
            active = False
            break
        elif menu_input == "y" or menu_input == "Y": #Exits menu_input loop to repeat the core program loop
            get_menu_input = False
        else:
            print("Please, enter Y to repeat program or N to terminate program.")
                
                
        
