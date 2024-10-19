#-------------------------------------------
# Program Name: ITS320_CTA5_Option1
# Author: Chris Russell
# Date: 7/11/24
#-------------------------------------------
# Pseudocode:
# 1. Collect three inputs from the user.
# 2. Create a new variable based on the result of a function
# 3. Pass concatenation of three inputs into the function that reverses the string
# 4. Print the new, reversed string
#-------------------------------------------
# Program Inputs: Three strings from the user
# Program Outputs: A concatenation of all three strings in reverse order
#-------------------------------------------

#Reverses the concatenation of the three strings combined
def reverse_string(string):
    return string[::-1]
        
#Get user input
string1 = input('Enter first string: ')
string2 = input('Enter second string: ')
string3 = input('Enter third string: ')

#Create new_string variable and call function to create the value based on user input
new_string = reverse_string(string1 + string2 + string3)

#print reversed string
print("\nThe reversed concatenation is: " + new_string)
