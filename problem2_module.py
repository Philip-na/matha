from logic_gates import AND_gate, OR_gate, NOT_gate, NAND_gate
from tests import CAR_SEATBELT_ALARM_TEST_CASES
    
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
        

# testing the function

def test_seat_belt_alarm():
    
    for test_case in CAR_SEATBELT_ALARM_TEST_CASES:
        ignition_on = test_case["ignition_on"]
        driver_seat_on = test_case["driver_seat_on"]
        driver_seat_belt_on = test_case["driver_seat_belt_on"]
        passenger_seat_on = test_case["passenger_seat_on"]
        passenger_seat_belt_on = test_case["passenger_seat_belt_on"]
        
        expected = test_case["expected"]
        
        result = seat_belt_alarm(ignition_on, driver_seat_on, driver_seat_belt_on, passenger_seat_on, passenger_seat_belt_on)
        
        print(f"Expected: {expected}, Got: {result}")