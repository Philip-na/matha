# Logic gates required for the problems
def AND_gate(a, b): # AND gate
    return a and b


def OR_gate(a, b): # OR gate
    return a or b


def NOT_gate(a): # NOT gate
    return not a


def NAND_gate(a, b): # NAND gate
    return not (a and b)


is_running = True # This variable is used to control the main loop of the program
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
            pass
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        print()
        


# problem 1 implimentation (Automobile alarm circuit)
def alarm_circuit(door_open, ignition_on, head_lights_on):
    
    alarmDoor_openIgnition_on = AND_gate(door_open, ignition_on)# check if door is open while ignition is on
    
    alarmHead_lights_onIgnition_on = AND_gate(head_lights_on, NOT_gate(ignition_on)) # check if the headlight is on while the ignition is off.
    
    trigger_alarm = OR_gate(alarmDoor_openIgnition_on, alarmHead_lights_onIgnition_on)  # check if the alarm is triggered by either of the two conditions
    
    if trigger_alarm:
        return "Alarm is triggered"
    else:
        return "Alarm is not triggered"
    
def run_problem_1():
    print("....... welcome to alarmcircuit......")
   
    # let the user input the values
    door_open = input("Is the door open? (True/False): ")
    ignition_on = input("Is the car started? (True/False): ")
    head_lights_on = input("Are the headlights on? (True/False): ")
    # convert the input values to boolean
    door_open = True if door_open.lower() == 'true' else False
    ignition_on = True if ignition_on.lower() == 'true' else False
    head_lights_on = True if head_lights_on.lower() == 'true' else False
    # Calling the function for problem 1
    result = alarm_circuit(door_open, ignition_on, head_lights_on)
    print(f"Alarm circuit result: {result}")
    
    
# problem 2 implimentation (Car Seatbely alarm system)

def run_problem_2():
    print("....... welcome to carseatbelt alarm system......")
    # let the user input the values
    ignition_on = input("Is the ignition on? (yes/no): ")
    driver_seat_on = input("Is the driver seat occupied? (yes/no): ")
    driver_seat_belt_on = input("Is the driver wearing a seatbelt? (yes/no): ")
    passenger_seat_on = input("Is the passenger seat occupied? (yes/no): ")
    passenger_seat_belt_on = input("Is the passenger wearing a seatbelt? (yes/no): ")
    
    # convert the input values to boolean
    ignition_on = True if ignition_on.lower() == 'yes' else False
    driver_seat_on = True if driver_seat_on.lower() == 'yes' else False
    driver_seat_belt_on = True if driver_seat_belt_on.lower() == 'yes' else False
    passenger_seat_on = True if passenger_seat_on.lower() == 'yes' else False
    passenger_seat_belt_on = True if passenger_seat_belt_on.lower() == 'yes' else False
    
    # Calling the function for problem 2
    result = seat_belt_alarm(ignition_on, driver_seat_on, driver_seat_belt_on, passenger_seat_on, passenger_seat_belt_on)
    print(f"Seat belt alarm result: {result}")
    
   

def seat_belt_alarm(ignition_on,driver_seat_on, driver_seat_belt_on,passenger_seat_on, passenger_seat_belt_on):
        
        # Check if the driver is seated without a seatbelt
        # Use NAND gate to check if the driver is seated and not wearing a seatbelt
        BELTD = driver_seat_belt_on
        BELTD_prim = NOT_gate(BELTD)
        driver_alarm = NAND_gate(driver_seat_on, NOT_gate(BELTD_prim))
        
        # Check if the passenger is seated without a seatbelt
        # Use NAND gate to check if the passenger is seated and not wearing a seatbelt
        BELTP = passenger_seat_belt_on
        BELTP_prim = NOT_gate(BELTP)
        passenger_alarm = NAND_gate(passenger_seat_on,NOT_gate(BELTP_prim) )
        
        if not passenger_seat_on:
            passenger_alarm = False  # If the passenger seat is not occupied, the alarm should not trigger
              
        seat_belt_alarm = OR_gate(driver_alarm, passenger_alarm)  # Check if either the driver or passenger alarm is triggered
            
        # If the ignition is off, the alarm should not trigger
        # Use NAND gate to check if the ignition is on and the seat belt alarm is triggered
        trigger_alarm = NAND_gate(ignition_on, seat_belt_alarm)  
        
        if trigger_alarm:
            return " Alarm is not triggered"
        else:
            return "Alarm is triggered"
        
        
# problem 3 implimentation (Syrup Manufacturing control logic)
def syrup_manufacturing(temperature, pressure, viscosity):

    pass


  
# Calling the main function to start the program      
if __name__ == "__main__":
    main()
    
