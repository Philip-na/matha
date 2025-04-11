# problem 1 implimentation (Automobile alarm circuit)
def alarm_circuit(door_open, ignition_on, head_lights_on):
    
    alarmDoor_openIgnition_on = door_open and ignition_on # check if door is open while ignition is on
    
    alarmHead_lights_onIgnition_on = head_lights_on and (not ignition_on) # check if the headlight is on while the ignition is off.
    
    trigger_alarm = alarmDoor_openIgnition_on or alarmHead_lights_onIgnition_on # check if the alarm is triggered by either of the two conditions
    
    if trigger_alarm:
        return "Alarm is triggered"
    else:
        return "Alarm is not triggered"
    
    
# problem 2 implimentation (Car Seatbely alarm system)
def seat_belt_alarm(driver_seat_belt, passenger_seat_belt):
    
    pass

# problem 3 implimentation (Syrup Manufacturing control logic)
def syrup_manufacturing(temperature, pressure, viscosity):

    pass


# main shell programdef main():
is_running = True

def main():
    while is_running:
        print("Select a problem to solve:")
        print("1. Automobile alarm circuit")
        print("2. Car Seatbelt alarm system")
        print("3. Syrup Manufacturing control logic")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':

            print("....... welcome to alarmcircuit......")
            print("....door closed...")
            
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
            
        elif choice == '2':
            # Calling the function for problem 2
            pass
        elif choice == '3':
            # Calling the function for problem 3
            pass
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        print()
  
# Calling the main function to start the program      
if __name__ == "__main__":
    main()
    
    