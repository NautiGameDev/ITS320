#-------------------------------------------
# Program Name: ITS320_CTA6_Option1
# Author: Chris Russell
# Date: 7/20/24
#-------------------------------------------
# Pseudocode:
# 1. Collect real and imaginary number inputs from user in the format: A B and C D
# 2. split input by space and convert numbers to floats
# 3. Pass converted lists into Complex class
# 4. Define operators of class
# 5. Output operations of both complex numbers
#-------------------------------------------
# Program Inputs: Two sets of numbers in the format A B and C D
# Program Outputs: Operations of complex numbers based on the two user inputs
#-------------------------------------------


import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary     
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = (self.real*no.real) - (self.imaginary*no.imaginary)
        imaginary = (self.real*no.imaginary) + (self.imaginary*no.real)
        return Complex(real, imaginary)

    def __truediv__(self, no):
        denominator = (no.real**2 + no.imaginary**2)
        real = (self.real*no.real + self.imaginary*no.imaginary) / denominator
        imaginary = (self.imaginary*no.real - self.real*no.imaginary) / denominator
        return Complex(real, imaginary)

    def mod(self):
        real = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(real, 0)

    def __str__(self):
        result = str(round(self.real, 2)) + "+" + str(round(self.imaginary, 2)) + "i"
        return result

C = map(float, input("Input two numbers(A B): ").split())
D = map(float, input("Input two numbers(C D): ").split())
x = Complex(*C)
y = Complex(*D)
print ('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))) 
