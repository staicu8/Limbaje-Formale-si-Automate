def load_dfa(file_name):
    states = []
    initial = ''
    finals = []
    transitions = dict()
    alphabet = []
    with open(file_name, "r") as fin:
        lines = fin.readlines()
    section = ""  
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "#" in line:
            line = line.split("#", 1)[0].strip()      
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            if line.upper() == "[END]":
                section = ""  
            else:
                section = line  
            continue 
        if section == "[States]":
            parts = line.split(",")
            if len(parts) == 2:
                state = parts[0].strip()
                code_str = parts[1].strip()
                if state not in states:
                    states.append(state)
                if code_str:
                    code_val = int(code_str) 
                    if code_val == 0 and not initial:
                        initial = state
                    elif code_val == 1 and state not in finals:
                        finals.append(state)
        elif section == "[Alphabet]":
            symbol = line.strip()
            if symbol and symbol not in alphabet:
                alphabet.append(symbol)
        
        elif section == "[Transitions]":
            parts = line.split(",")
            if len(parts) == 3:
                s1 = parts[0].strip()
                s2_dest = parts[1].strip()
                sym_trans = parts[2].strip()
                transitions[(s1, sym_trans)] = s2_dest 
    return {
        "states": states,
        "initial": initial,
        "finals": finals,
        "transitions": transitions,
        "alphabet": alphabet
    }


def run_dfa(automata, input_str):
    current_state = automata["initial"] 
    for char_in_string in input_str:
        if char_in_string not in automata["alphabet"]:
            return False 
        transition_key = (current_state, char_in_string)
        if transition_key not in automata["transitions"]:
            return False     
        current_state = automata["transitions"][transition_key]   
    return current_state in automata["finals"]

str=input("Enter a string:")
print(run_dfa(load_dfa("dfa.txt"), str))
