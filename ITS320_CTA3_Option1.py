#-------------------------------------------
# Program Name: ITS320_CTA3_Option1
# Author: Chris Russell
# Date: 6/27/24
#-------------------------------------------
# Pseudocode: Retrieves the user input of a year between 1962 and 2014, then outputs the value of the Ferrari 250 GTO in that year.
#-------------------------------------------
# Program Inputs: Any year between 1962 and 2014.
# Program Outputs: The dollar value of the Ferraro 250 GTO in that year.
#-------------------------------------------

#Function to test if input contains only numbers. For loop checks each individual character in the input, if the character isn't a number the function returns as false.
def check_input(user_input):
    passed = True
    
    for i in user_input:
        if not i.isdigit():
            passed = False
        

    return passed

#Retrieves user input
user_input = input("Input a year between 1962 and 2014: ")


#Runs input test to make sure input only contains numbers
input_test = check_input(user_input)

if input_test: #If check input function returns as true, then value is checked. Otherwise, an error message is displayed for the user.
    user_input = int(user_input)

      
    #Conditional statements that print responses based on the user's input.
    if user_input < 1962:
        print("Year is too low. Please, try a different year between 1962 and 2014.")

    elif 1962 <= user_input <= 1964:
        print("The value of the Ferrari 250 GTO in ", user_input, " was approximately $18,500.")

    elif 1965 <= user_input <= 1968:
        print("The value of the Ferrari 250 GTO in ", user_input, " was approximately $6,000.")

    elif 1969 <= user_input <= 1971:
        print("The value of the Ferrari 250 GTO in ", user_input, " was approximately $12,000.")

    elif 1972 <= user_input <= 1975:
        print("The value of the Ferrari 250 GTO in ", user_input, " was approximately $48,000.")

    elif 1976 <= user_input <= 1980:
        print("The value of the Ferrari 250 GTO in ", user_input, " was approximately $200,000.")

    elif 1981 <= user_input <= 1985:
        print("The value of the Ferrari 250 GTO in ", user_input, " was approximately $650,000.")

    elif 1986 <= user_input <= 2012:
        print("The value of the Ferrari 250 GTO in ", user_input, " was approximately $35,000,000.")

    elif 2013 <= user_input <= 2014:
        print("The value of the Ferrari 250 GTO in ", user_input, " was approximately $52,000,000.")

    else:
        print("Year is too high. Please, try a different year between 1962 and 2014.")

else:
    print("Letters aren't allowed. Try again with a year as input.")
          
