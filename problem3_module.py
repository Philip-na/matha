from logic_gates import AND_gate, OR_gate, NOT_gate, NAND_gate

def syrup_tank_control_inlet_table( l_min, l_max, f_inlet):
    
    # if l_max is True and l_min is False, the system is invalid
    if l_max and not l_min:
        return "Invalid "
    
    V_inlet = OR_gate(AND_gate(f_inlet, NOT_gate(l_max)), NOT_gate(l_min))
    
    return V_inlet

    


def syrup_tank_control_outlet_table(l_min,l_max, f_inlet, temp):
    
     # if l_max is True and l_min is False, the system is invalid
    if l_max and not l_min:
        return "Invalid "
    
    v_outlet = AND_gate(NOT_gate(f_inlet), AND_gate(l_min, temp))
    
    return v_outlet


def syrup_tank_control_logic(l_max, l_min, f_inlet, temp):
    # if l_max is True and l_min is False, the system is invalid

    
    V_inlet = OR_gate(AND_gate(f_inlet, NOT_gate(l_max)), NOT_gate(l_min))
    v_outlet = AND_gate(NOT_gate(f_inlet), AND_gate(l_min, temp))
    
    return [V_inlet, v_outlet]