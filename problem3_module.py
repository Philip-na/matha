from logic_gates import AND_gate, OR_gate, NOT_gate, NAND_gate
from tests import SYRUP_TANK_CONTROL_TEST_CASES

# problem 3 implimentation (Syrup Manufacturing control logic)

# the function for the syrup tank V_inlet truth table
def syrup_tank_control_inlet_table( l_min, l_max, f_inlet):
    
    # if l_max is True and l_min is False, the system is invalid
    if l_max and not l_min:
        return "Invalid "
    
    V_inlet = OR_gate(AND_gate(f_inlet, NOT_gate(l_max)), NOT_gate(l_min))
    
    return V_inlet


# the function for the syrup tank V_outlet truth table
def syrup_tank_control_outlet_table(l_min,l_max, f_inlet, temp):
    
     # if l_max is True and l_min is False, the system is invalid
    if l_max and not l_min:
        return "Invalid "
    
    v_outlet = AND_gate(NOT_gate(f_inlet), AND_gate(l_min, temp))
    
    return v_outlet


# the function for the syrup tank logic circuit
def syrup_tank_control_logic(l_max, l_min, f_inlet, temp):
    # if l_max is True and l_min is False, the system is invalid

    
    V_inlet = OR_gate(AND_gate(f_inlet, NOT_gate(l_max)), NOT_gate(l_min))
    v_outlet = AND_gate(NOT_gate(f_inlet), AND_gate(l_min, temp))
    
    return [V_inlet, v_outlet]


# the function to run the syrup manufacturing control logic
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
    

def syrup_manufacturing(l_max, l_min, f_inlet, temp):
    # if l_max is True and l_min is False, the system is invalid
    if l_max and not l_min:
        print("Invalid ")
        return 
    
    value = syrup_tank_control_logic(l_max, l_min, f_inlet, temp)
    V_inlet = value[0]
    v_outlet = value[1]
    
    print(f"results for Inlet truth table (V_inlet): {V_inlet}")
    print(f"results for Outlet truth table (V_outlet): {v_outlet}")
    return


# Testing the syrup_tank_control_logic function with test data
def test_syrup_tank_control_logic():
  
    
    for test in SYRUP_TANK_CONTROL_TEST_CASES:
        result = syrup_tank_control_logic(test["l_max"], test["l_min"], test["f_inlet"], test["temp"])
        print(f"Expected: {test['expected']}, Got: {result}")
        
    
   