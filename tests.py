
# this test is for the alarm_circuit function (problem 1)
ALARM_TESTS = [
    # Test case 1: Door open, ignition on, headlights off, alarm should trigger
    {"door_open": True, "ignition_on": True, "head_lights_on": False, "expected": "Alarm is triggered"},
    
    # Test case 2: Door closed, ignition on, headlights on, no alarm should trigger
    {"door_open": False, "ignition_on": True, "head_lights_on": True, "expected": "Alarm is not triggered"},
    
    # Test case 3: Door open, ignition off, headlights on, alarm should trigger
    {"door_open": True, "ignition_on": False, "head_lights_on": True, "expected": "Alarm is triggered"},
    
    # Test case 4: Door closed, ignition off, headlights off, no alarm should trigger
    {"door_open": False, "ignition_on": False, "head_lights_on": False, "expected": "Alarm is not triggered"},
    
    # Test case 5: Door open, ignition off, headlights off, alarm should trigger
    {"door_open": True, "ignition_on": False, "head_lights_on": False, "expected": "Alarm is triggered"}, 
]

# this test is for the seat_belt_alarm function (problem 2)
CAR_SEATBELT_ALARM_TEST_CASES = [
    
    # Test case 1: Ignition off, no alarm should trigger
    {
        "ignition_on": False,
        "driver_seat_on": True,
        "driver_seat_belt_on": False,
        "passenger_seat_on": True,
        "passenger_seat_belt_on": False,
        "expected": " Alarm is not triggered"
    },
    # Test case 2: Driver seated without seatbelt, alarm should trigger
    {
        "ignition_on": True,
        "driver_seat_on": True,
        "driver_seat_belt_on": False,
        "passenger_seat_on": False,
        "passenger_seat_belt_on": False,
        "expected": "Alarm is triggered"
    },
    # Test case 3: Passenger seated without seatbelt, alarm should trigger
    {
        "ignition_on": True,
        "driver_seat_on": False,
        "driver_seat_belt_on": False,
        "passenger_seat_on": True,
        "passenger_seat_belt_on": False,
        "expected": "Alarm is triggered"
    },
    # Test case 4: Both driver and passenger seated with seatbelts, no alarm
    {
        "ignition_on": True,
        "driver_seat_on": True,
        "driver_seat_belt_on": True,
        "passenger_seat_on": True,
        "passenger_seat_belt_on": True,
        "expected": " Alarm is not triggered"
    },
    # Test case 5: Driver seated with seatbelt, passenger not seated, no alarm
    {
        "ignition_on": True,
        "driver_seat_on": True,
        "driver_seat_belt_on": True,
        "passenger_seat_on": False,
        "passenger_seat_belt_on": False,
        "expected": " Alarm is not triggered"
    },
    # Test case 6: Ignition off, driver and passenger seated without seatbelts, no alarm
    {
        "ignition_on": False,
        "driver_seat_on": True,
        "driver_seat_belt_on": False,
        "passenger_seat_on": True,
        "passenger_seat_belt_on": False,
        "expected": " Alarm is not triggered"
    }
]

# this test is for the syrup_tank_control_logic function (problem 3)
SYRUP_TANK_CONTROL_TEST_CASES = [
    # Test case 1: l_max is True, l_min is False, f_inlet is True, temp is True, expected result is "Invalid"
    {"l_max": True, "l_min": False, "f_inlet": True, "temp": True, "expected": "Invalid"},
    
    # Test case 2: l_max is False, l_min is True, f_inlet is True, temp is True, expected result is [True, False]
    {"l_max": False, "l_min": True, "f_inlet": True, "temp": True, "expected": [True, False]},
    
    # Test case 3: l_max is False, l_min is False, f_inlet is False, temp is True, expected result is [False, False]
    {"l_max": False, "l_min": False, "f_inlet": False, "temp": True, "expected": [False, False]},
    
    # Test case 4: l_max is True, l_min is True, f_inlet is True, temp is False, expected result is [True, False]
    {"l_max": True, "l_min": True, "f_inlet": True, "temp": False, "expected": [True, False]},
]

