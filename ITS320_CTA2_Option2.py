#-------------------------------------------
# Program Name: ITS320_CTA2_Option2
# Author: Chris Russell
# Date: 6/23/24
#-------------------------------------------
# Pseudocode: Receives the user input regarding information of a car and stores that information in a dictionary. Then prints out the dictionary.
#-------------------------------------------
# Program Inputs: car brand, model, year, starting odometer reading, ending odometer reading, and estimated MPG
# Program Outputs: A dictionary containing the stored information of the vehicle
#-------------------------------------------

#user inputs
print("Please enter the following information about the vehicle.")
brand = input("Brand: ")
model = input("Model: ")
year = input("Year: ")
st_odometer = input("Starting odometer reading: ")
end_odometer = input("Ending odometer reading: ")
mpg = input("Est. Miles per gallon: ")

print(test)

#Create dictionary with variables
vehicle = {
        "brand": brand,
        "model": model,
        "year": year,
        "starting odometer": st_odometer,
        "ending odometer": end_odometer,
        "mpg": mpg
    }

#Dictionary output
print("Vehicle information: ", vehicle)


