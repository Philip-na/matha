# problem 1 implimatation (Automobile alarm circut)
def alarm_circuit(door_open, car_started, head_lights_on):
    
    alarmkDoor_openCar_started = door_open and car_started # check if the door is open and the car is started
    
    alarmHead_lights_onCar_started = head_lights_on and (not car_started) # check if the headlights are on and the car is not started
    
    trigered_alarm = alarmkDoor_openCar_started or alarmHead_lights_onCar_started # check if the alarm is trigered by either of the two conditions
    
    if trigered_alarm:
        return "Alarm is trigered"
    else:
        return "Alarm is not trigered"
    
    
# problem 2 implimatation (Car Seatbely alarm system)
def seat_belt_alarm(driver_seat_belt, passenger_seat_belt):
    
    pass

# problem 3 implimatation (Syrup Manufacturing control logic)
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
            
            # let the user input the values
            door_open = input("Is the door open? (True/False): ")
            car_started = input("Is the car started? (True/False): ")
            head_lights_on = input("Are the headlights on? (True/False): ")
            
            # convert the input values to boolean
            door_open = True if door_open.lower() == 'true' else False
            car_started = True if car_started.lower() == 'true' else False
            head_lights_on = True if head_lights_on.lower() == 'true' else False
            
            # Call the function for problem 1
            result = alarm_circuit(door_open, car_started, head_lights_on)
            print(f"Alarm circuit result: {result}")
            
        elif choice == '2':
            # Call the function for problem 2
            pass
        elif choice == '3':
            # Call the function for problem 3
            pass
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        print()
  
# Call the main function to start the program      
if __name__ == "__main__":
    main()
    
    