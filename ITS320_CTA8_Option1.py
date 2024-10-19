#-------------------------------------------
# Program Name: ITS320_CTA8_Option1
# Author: Chris Russell
# Date: 8/4/24
#-------------------------------------------
# Pseudocode:
# A small program that allows the user to create an inventory of vehicles and save that inventory to a text file.
# Program includes working menus that respond to user input and ensures input is usable to avoid program crashes.
# The core concept of the program is to create vehicles based on the car class which stores all the information for each vehicle.
# Vehicle objects are stored as values in a dictionary based on a key of year + make + model
# User can add and remove vehicles, and update any data in a vehicle very flexibly.
# When the user is finished they can save the inventory into a text document with the file name of their choice.

#-------------------------------------------
# Program Inputs: 
# Numerical menu inputs to navigate the program.
# Add vehicle: Make, Model, Color, Year, and Mileage.
# Remove vehicle: Choose vehicle and confirm deletion.
# Update vehicle: Choose vehicle, choose data, input new data
# Save inventory: File name
# Confirmations through out the program by entering y or n to prevent user errors.

# Program Outputs: 
# In terminal: Lists of vehicles and data associated with each.
# To file: A .txt document with all the vehicles in the inventory as well as their data
#-------------------------------------------

import os

###############
## Car Class ##
###############

class Car:
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

        print("# New vehicle created!\n")
        print(self.get_info())
    
    def get_info(self):
        data = " | Make: " + self.make + ' | Model: ' + self.model + " | Color: " + self.color + " | Year: " + self.year + " | Mileage: " + self.mileage
        return data
    
    def set_data(self, data, user_input):
        if data == "Make":
            self.make = user_input
        elif data == "Model":
            self.model = user_input
        elif data == "Color":
            self.color = user_input
        elif data == "Year":
            self.year = user_input
        elif data == "Mileage":
            self.mileage = user_input

        update_message = "Updated vehicle ", data, " to: ", user_input
        return update_message

########################
## Core Program Class ##
########################
# This class handles the main functions and loop of the program

class Program:
    def __init__(self):

        #Program states
        self.active = True
        self.state = "Main"

        #Inventory of vehicles
        self.inventory = {}

        #Messages to print based on state
        self.state_text = {
            'Main': ['\n# Main Menu','# Choose an option by entering a number:\n', '##########\n', '1. Add a new vehicle', '2. Remove a vehicle', '3. Update vehicle', '4. Save inventory', '5. Quit program'],
            'Add Vehicle': ["\n# Add Vehicle\n", "# Enter Q at any time to cancel and return to main menu\n"],
            'Remove Vehicle': ["\n# Remove Vehicle", "# Enter Q at any time to cancel and return to main menu\n"],
            'Update Vehicle': ["\n# Update Vehicle", "# Enter Q at any time to cancel and return to main menu\n"],
            'Save Data': ["\n# Save inventory data", '# Enter Q at any time to cancel and return to main menu\n'],
            'Close Program': ["# Quit program?", "# Unsaved progress will be lost."]
        }

        #Inputs for adding and updating vehicles
        self.add_vehicle_inputs = ['Make: ', 'Model: ', 'Color: ', 'Year: ', 'Mileage: ']

###############
## Utilities ##
###############
# The following functions are used frequently throughout the program.

    def get_text(self):
        #Iterate through list of text and print based on the state of the program.

        for option in self.state_text[self.state]:
            print(option)

    def clear_terminal(self):
        # Clear terminal of previous messages for easy readability
        
        # The intention of this function was to clear all text in terminal and reprint new text to maintain a clean and readable screen.
        # However, after some testing in Idle, this function wasn't behaving the same as it did in Virtual Studio Code.
        # A print statement has been added to adjust for Idle and the original line of code is commented out for reference.

        os.system('cls' if os.name == 'nt' else 'clear')

        #print("\n\n\n#########\n #######\n  #####\n   ###\n    #\n\n\n")
        
    def confirm_check(self):
        # Asks user for confirmation and returns true or false depending on input
        # While loop exists to ensure either y or n is entered before continuing with program

        while True:
            user_input = input("Y or N?: ")

            if user_input.lower() == "y":
                return True
            
            elif user_input.lower() == "n":
                return False

            elif user_input.lower() == "q":
                self.clear_terminal()
                print("# Returning to main menu\n")
                self.state = "Main"
                return False

            else:
                print("# Please enter Y for yes, or N for no.\n")
    
    def test_input_is_int(self, user_input):
        #Test if user input is integer, else provide error message and restart current loop

        try:
            user_input = int(user_input)
            return True, user_input
        except:
            self.clear_terminal()
            print("# Error: Please enter a number to select the option.")
            return False, user_input
        
    def test_input_in_len(self, user_input, list):
        
        #Test if user input is within the legnth of a list - prevents errors if input is too high
        #If input number is too high, display error message and restart current loop

        if user_input > len(list):
            self.clear_terminal()
            print("# Error: Number entered is too high. Please try again.")
            return False
        else:
            return True

    def test_input_to_value(self, user_input, value):
        
        #Test user input against a specified value - Usually "q" or None for exiting to main menu options

        if user_input == value:
            return True
        else:
            return False

        
#########################
## Main Menu Functions ##
#########################
# Check user input is an integer.
# If not int, display error message and repeat menu display
# If int, use condition checks to change state of program or display error message if out of bounds

    def process_main_menu(self):
        user_input = input('Enter Option: ')
        self.clear_terminal()

        int_test, user_input = self.test_input_is_int(user_input)

        if int_test == False:
            return

        if user_input == 1:
            self.state = "Add Vehicle"
            
        elif user_input == 2:
            self.state = "Remove Vehicle"

        elif user_input == 3:
            self.state = "Update Vehicle"

        elif user_input == 4:
            self.state = "Save Data"

        elif user_input == 5:
            self.state = "Close Program"

        else:
            print("## Error: Input out of bounds. Enter one of the menu options available.")

###########################
## Add Vehicle Functions ##
###########################
# Use for loop to retrieve user input for each item in add_vehicle_inputs list
# Check if user has entered Q or q. If so, return to main menu.
# Append user inputs to new list.
# Reprint user inputs and ask for confirmation.
# If not confirmed, repeat add vehicle process
# If confirmed, strip inputs and instantiate new car object with input variables.
# Add car object to key year+make+model in inventory dictionary

    def process_add_vehicle(self):
        vehicle_info = self.new_vehicle_info()

        if vehicle_info:
            make = vehicle_info[0].strip()
            model = vehicle_info[1].strip()
            color = vehicle_info[2].strip()
            year = vehicle_info[3].strip()
            mileage = vehicle_info[4].strip()

            self.clear_terminal()

            new_vehicle = Car(make, model, color, year, mileage)
            vehicle_key = year + " " + make + " " + model
            self.inventory[vehicle_key] = new_vehicle

            self.state = "Main"

    def new_vehicle_info(self):
        vehicle_inputs = []
        for input_text in self.add_vehicle_inputs:
            
            user_input = input(input_text)

            if self.test_input_to_value(user_input.lower(), "q"):
                self.clear_terminal()
                print("## Returning to main menu.\n")
                self.state = "Main"
                return
            
            else:
                vehicle_inputs.append(user_input)

        if self.confirm_new_vehicle(vehicle_inputs):
            return vehicle_inputs


    def confirm_new_vehicle(self, vehicle_inputs):
        self.clear_terminal()

        print("## Is the following vehicle correct?\n")
        print("\n##########\n")

        for i, info in enumerate(vehicle_inputs):
            print(self.add_vehicle_inputs[i], info)

        print("\n##########\n")

        if self.confirm_check():
            return True

##############################
## Remove Vehicle Functions ##
##############################
# Get info of each vehicle in inventory.
# Get and check if user input is integer, else display error message and repeat
# Return user input - 1 to process_remove_vehicle
# Create list based on inventory to align user input with index of dictionary key
# Ask user to confirm deleting of vehicle
# If confirmed: clear object, delete vehicle from dictionary, and return to main menu.

    def process_remove_vehicle(self):
        vehicle_choice = self.choose_vehicle()

        if self.test_input_to_value(vehicle_choice, None):
            return
        
        vehicle_list = list(self.inventory.keys())

        self.get_text()
        print("# Are you sure you want to remove", vehicle_list[vehicle_choice], "from the inventory?")

        if self.confirm_check():
            self.clear_terminal()
            print("# Removed", vehicle_list[vehicle_choice], "from inventory.\n")
            self.inventory[vehicle_list[vehicle_choice]] = None
            del self.inventory[vehicle_list[vehicle_choice]]
            
        else:
            self.clear_terminal()
            print("# Remove vehicle cancelled. Returning to main menu.\n")

        self.state = "Main"

    #Choose vehicle is accessed from both remove and update vehicle functions
    def choose_vehicle(self):
        vehicle_chosen = False

        while not vehicle_chosen:
            print("# Current inventory:\n")

            for i, vehicle in enumerate(self.inventory):
                print(str(i+1), end="")
                print(self.inventory[vehicle].get_info())

            if self.inventory == {}:
                print("  You haven't added any vehicles yet!")
            
            print("\n##########\n")
            print("# Choose vehicle by entering the correct number.")
            menu_input = input('Enter number: ')

            if self.test_input_to_value(menu_input.lower(), "q"):
                self.state = "Main"
                self.clear_terminal()
                print("# Returning to main menu")
                return

            is_int, user_input = self.test_input_is_int(menu_input)
            

            if is_int:
                is_len = self.test_input_in_len(user_input, self.inventory)
            
                if is_len:
                    self.clear_terminal()
                    vehicle_chosen = True
                    return user_input - 1
                else:
                    return None
            else:
                return None


##############################
## Update Vehicle Functions ##
##############################
# Print list of vehicles that exist in inventory
# Get user input on chosen vehicle
# Print list of data for chosen vehicle
# Get user input for which data they want to update
# Get new data input from user
# Confirm new data before changing


    def process_update_vehicle(self):

        ## Step 1: User chooses vehicle ##

        vehicle_choice = self.choose_vehicle()

        if self.test_input_to_value(vehicle_choice, None):
            return
        
        self.get_text()

        vehicle_list = list(self.inventory.keys())
        chosen_vehicle = vehicle_list[vehicle_choice]
        print("# Updating", chosen_vehicle, "\n")


        ## Step 2: User chooses which data to modify ##

        detail_selection = self.choose_detail(chosen_vehicle)

        
        
        if self.test_input_to_value(detail_selection, None):
            return

        self.get_text()

        print("# Updating ", detail_selection)

        ## Step 3: Get new values from user ##

        new_data = self.get_new_data(chosen_vehicle, detail_selection)

        ## Step 4: Confirm user input ##

        print("\n# Update ", detail_selection, " to ", new_data, "?")
        
        if self.confirm_check():
            self.clear_terminal()
            confirm_message = self.inventory[chosen_vehicle].set_data(detail_selection, new_data)

            for part in confirm_message:
                print(part, end="")

            print("\n")
            self.state = "Main"

        else:
            return
                           
    def choose_detail(self, chosen_vehicle):
        detail_chosen = False

        while not detail_chosen:

            ## Print list of details for vehicle with values ##

            print("\n##########\n")
            for i, choice in enumerate(self.add_vehicle_inputs):
                print(str(i+1), ":", choice, end="")
                
                if "Make" in choice:
                    print(self.inventory[chosen_vehicle].make)
                elif "Model" in choice:
                    print(self.inventory[chosen_vehicle].model)
                elif "Color" in choice:
                    print(self.inventory[chosen_vehicle].color)
                elif "Year" in choice:
                    print(self.inventory[chosen_vehicle].year)
                elif "Mileage" in choice:
                    print(self.inventory[chosen_vehicle].mileage)

            print("\n##########\n")
            print("# Enter number to select data you want to update.")

            user_input = input("Enter number: ")

            ## Run full test of user input ##

            if self.test_input_to_value(user_input.lower(), "q"):
                self.state = "Main"
                return
            
            is_int, user_input = self.test_input_is_int(user_input)

            if is_int:
                is_len = self.test_input_in_len(user_input, self.add_vehicle_inputs)

                if is_len:
                    self.clear_terminal()
                    choice = self.add_vehicle_inputs[user_input - 1]
                    return choice[:-2]
                else:
                    ## If input fails int and length test, restart loop in current menu
                    return None
            else:
                return None

    def get_new_data(self, chosen_vehicle, choice):
    
        print("\n##########\n")
        print(choice, " : ", end="")

        if "Make" in choice:
            print(self.inventory[chosen_vehicle].make)
        elif "Model" in choice:
            print(self.inventory[chosen_vehicle].model)
        elif "Color" in choice:
            print(self.inventory[chosen_vehicle].color)
        elif "Year" in choice:
            print(self.inventory[chosen_vehicle].year)
        elif "Mileage" in choice:
            print(self.inventory[chosen_vehicle].mileage)

        user_input = input("Enter new value: ")

        return user_input


#########################
## Save Data Functions ##
#########################
# Get file name from user
# Display inventory and confirm file name with user
# If confirmed, iterate through inventory, retrieve data for each object, and save to text file

    def process_save_data(self):

        #Step 1: Get file name from user
        print('\n# Please, enter the name of the file you wish to save data to.')
        file_name = self.get_file_name()
        
        if self.test_input_to_value(file_name, None):
            return
        
        self.get_text()


        #Step 2: Confirm file name with user
        print("\n##########\n")
        print("# Vehicle Inventory:")
        for i, vehicle in enumerate(self.inventory):
            print(str(i+1), self.inventory[vehicle].get_info(),"\n")

        print("\n##########\n")
        print("Save inventory as", file_name, " ?")
        
        #Step 3: If confirmed, save file as name
        if self.confirm_check():
            self.save_inventory(file_name)
            self.state = "Main"
            self.clear_terminal() 
            print("# Vehicle inventory has been saved to", file_name)

        else:
            self.clear_terminal()
            self.state = "Main"
            print("\n# Save inventory file cancelled. Returning to main menu.\n")
        

    def get_file_name(self):
        file_name = input("\nFile Name: ")

        if self.test_input_to_value(file_name.lower(), "q"):
            self.clear_terminal()
            print("# Returning to main menu.\n")
            self.state = "Main"
            return
        
        file_name = file_name.strip()

        #Tests if .txt already exists in file name. If not, add .txt to file name.
        if file_name[-4:] != ".txt":
            file_name = file_name + ".txt"

        self.clear_terminal()
        return file_name

    def save_inventory(self, file_name):
        with open(file_name, 'w') as file:
            for i, vehicle in enumerate(self.inventory):
                file.write(str(i+1))
                file.write(self.inventory[vehicle].get_info())
                file.write("\n")

#############################
## Close Program Functions ##
#############################
# Get user confirmation to close program
# If yes, end main program loop
# If no, return to main menu

    def process_close_program(self):

        if self.confirm_check():
            self.active = False

        else:
            self.state = "Main"
        
        self.clear_terminal()


#######################
## Main Program Loop ##
#######################
# Main while loop that retrieves and prints text based on program state
# Calls necessary function to process the program state

    def run(self):
        print("# Welcome!\n")

        while self.active:

            self.get_text()
            print("\n##########\n")

            if self.state == "Main":     
                self.process_main_menu()

            elif self.state == "Add Vehicle":
                self.process_add_vehicle()
                
            elif self.state == "Remove Vehicle":
                self.process_remove_vehicle()

            elif self.state == "Update Vehicle":
                self.process_update_vehicle()

            elif self.state == "Save Data":
                self.process_save_data()

            elif self.state == "Close Program":
                self.process_close_program()

        print("## Thank you! \n\n ## Closing program...")
        
if __name__ == "__main__":
    program = Program()
    program.run()
