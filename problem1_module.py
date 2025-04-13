from logic_gates import AND_gate, OR_gate, NOT_gate
from tests import ALARM_TESTS

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



# Testing the alarm_circuit function with test data
def test_alarm_circuit():
    for test in ALARM_TESTS:
        result = alarm_circuit(test["door_open"], test["ignition_on"], test["head_lights_on"])
        print(f"Expected: {test['expected']}, Got: {result}")
