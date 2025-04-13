
# this test is for the alarm_circuit function (problem 1)
ALARM_TESTS = [
    {"door_open": True, "ignition_on": True, "head_lights_on": False, "expected": "Alarm is triggered"},
    {"door_open": False, "ignition_on": True, "head_lights_on": True, "expected": "Alarm is not triggered"},
    {"door_open": True, "ignition_on": False, "head_lights_on": True, "expected": "Alarm is triggered"},
    {"door_open": False, "ignition_on": False, "head_lights_on": False, "expected": "Alarm is not triggered"},
    {"door_open": True, "ignition_on": False, "head_lights_on": False, "expected": "Alarm is triggered"}, 
]

SYRUP_TANK_CONTROL_TEST_CASES = [
        {"l_max": True, "l_min": False, "f_inlet": True, "temp": True, "expected": "Invalid"},
        {"l_max": False, "l_min": True, "f_inlet": True, "temp": True, "expected": [True, False]},
        {"l_max": False, "l_min": False, "f_inlet": False, "temp": True, "expected": [False, False]},
        {"l_max": True, "l_min": True, "f_inlet": True, "temp": False, "expected": [True, False]},
    ]

