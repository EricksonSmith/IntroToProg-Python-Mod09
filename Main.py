# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# ESmith,12.13.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__=="__main__":

    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported.")

# Main Body of Script  ---------------------------------------------------- #
# -- Data -- #
lst_emp_table = []
lst_file_data = []

# Load data from file into a list of employee objects when script starts

lst_file_data = Fp.read_data_from_file("EmployeeData.txt")
for row in lst_file_data:
    lst_emp_table.append(Emp(row[0],row[1],row[2].strip()))

# Show user a menu of options

while True:
    Eio.print_menu_items()
# Get user's menu option choice
    str_choice = Eio.input_menu_options()
    if str_choice == "1":
    # Show user current data in the list of employee objects
        Eio.print_current_list_items(lst_emp_table)
        continue
    elif str_choice == "2":
    # Let user add data to the list of employee objects
        lst_emp_table.append(Eio.input_employee_data())
        print("Employee Data Added.")
        continue
    elif str_choice == "3":
    # let user save current data to file
        Fp.save_data_to_file("EmployeeData.txt", lst_emp_table)
        print("Employee Data Saved.")
        continue
    elif str_choice == "4":
    # Let user exit program
        print("""
        *************************
        You've exited the program
        *************************
        """)
        break

# Main Body of Script  ---------------------------------------------------- #
