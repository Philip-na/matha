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
            run_problem_3()   
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

# testing the alarm_circuit function
testData = [
    {"door_open": True, "ignition_on": True, "head_lights_on": False, "expected": "Alarm is triggered"},
    {"door_open": False, "ignition_on": True, "head_lights_on": True, "expected": "Alarm is not triggered"},
    {"door_open": True, "ignition_on": False, "head_lights_on": True, "expected": "Alarm is triggered"},
    {"door_open": False, "ignition_on": False, "head_lights_on": False, "expected": "Alarm is not triggered"},
    {"door_open": True, "ignition_on": False, "head_lights_on": False, "expected": "Alarm is triggered"}, 
]

# Testing the alarm_circuit function with test data
def test_alarm_circuit():
    for test in testData:
        result = alarm_circuit(test["door_open"], test["ignition_on"], test["head_lights_on"])
        print(f"Expected: {test['expected']}, Got: {result}")
    
    
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
        z1 = NOT_gate(BELTP_prim) # z1 in normal 
        # z1 = False  # z1 is internally shorted to ground (for part b of the problem)
        passenger_alarm = NAND_gate(passenger_seat_on,z1)
        
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

def run_problem_3():
    print("....... welcome to syrup manufacturing control logic......")
    # let the user input the values
    l_max = input("Is l_max True? (yes/no): ")
    l_min = input("Is l_min True? (yes/no): ")
    f_inlet = input("Is f_inlet True? (yes/no): ")
    temp = input("Is temp True? (yes/no): ")
    
    # convert the input values to boolean
    l_max = True if l_max.lower() == 'yes' else False
    l_min = True if l_min.lower() == 'yes' else False
    f_inlet = True if f_inlet.lower() == 'yes' else False
    temp = True if temp.lower() == 'yes' else False
    
    # Calling the function for problem 3
    syrup_manufacturing(l_max, l_min, f_inlet, temp)
    print(f"Syrup manufacturing control logic result: {syrup_manufacturing(l_max, l_min, f_inlet, temp)}")


def syrup_manufacturing(l_max, l_min, f_inlet, temp):
    # if l_max is True and l_min is False, the system is invalid
    if l_max and not l_min:
        print("Invalid ")
        return 

    # cumputing the V_inlet using the l_max l_min and f_inlet
    V_inlet = OR_gate(AND_gate(f_inlet, NOT_gate(l_max)), NOT_gate(l_min))
    
    # computing the V_outlet using the l_mim, temp and f_inlet
    v_outlet = AND_gate(NOT_gate(f_inlet), AND_gate(l_min, temp))
    
    
    print("V_inlet: ", V_inlet)
    print("V_outlet: ", v_outlet)
    
    return 
    
    



  
# Calling the main function to start the program      
if __name__ == "__main__":
    main()
    
