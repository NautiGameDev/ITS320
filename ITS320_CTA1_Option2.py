#-------------------------------------------
# Program Name: ITS320_CTA1_Option2
# Author: Chris Russell
# Date: 6/16/24
#-------------------------------------------
# Pseudocode: Receives the input of two integers from the user and passes them through three different equations, then prints the outputs.
#-------------------------------------------
# Program Inputs: Two integers from the user
# Program Outputs: The answers to three different equations
#-------------------------------------------

print("Hello!")

#User inputs
numb_1 = int(input('Enter your first number: '))
numb_2 = int(input('Enter your second number: '))

#Equations
answer1 = numb_1 // numb_2
answer2 = numb_1 / numb_2
answer3 = numb_1 % numb_2

#Outputs
print("Answers:")

print("Integer division: ", numb_1, " // ", numb_2, " = ", answer1)
print("Float division: ", numb_1, " / ", numb_2, " = ", answer2)
print("Modulo division: ", numb_1, " % ", numb_2, " = ", answer3)
