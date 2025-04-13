from problem1_module import run_problem_1
from problem2_module import run_problem_2
from problem3_module import run_problem_3, syrup_tank_control_logic

is_running = True # This variable is used to control the main loop of the program

# The main function that runs the program
def main():
    while is_running:
        # Displaying the menu to the user
        print("******Welcome to Assessment 3 Simulator******")
        print("Select a problem to solve:")
        print("1. Automobile alarm circuit")
        print("2. Car Seatbelt alarm system")
        print("3. Syrup Manufacturing control logic")
    
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Calling the function to run problem 1
            run_problem_1()
        elif choice == '2':
            # Calling the function for problem 2
            run_problem_2()
        elif choice == '3':
            # Calling the function for problem 3
            run_problem_3()   
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        print()
          
# Calling the main function to start the program      
if __name__ == "__main__":
    main()
    
