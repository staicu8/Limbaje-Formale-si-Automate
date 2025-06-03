import json


with open('masina_turing.json', 'r') as f:
    config = json.load(f)


current_state = config["start_state"]
final_states = set(config["final_states"]) 
transitions = config["transitions"]
BLANK = config["blank_symbol"]

input_str = input("Introduceti sirul pentru Masina Turing: ")
tape = list(input_str) if input_str else [BLANK]
head_pos = 0


while True:


    symbol_under_head = ""
    if head_pos < 0:
        symbol_under_head = BLANK
    elif head_pos >= len(tape):
        symbol_under_head = BLANK
    else: 
        symbol_under_head = tape[head_pos]

    found_transition_rule = None
    for rule in transitions:
        if rule["current_state"] == current_state and rule["read_symbol"] == symbol_under_head:
            found_transition_rule = rule
            break
    
    if not found_transition_rule:
        break 
    
    symbol_to_write = found_transition_rule["write_symbol"]
    if head_pos < 0: 
        tape.insert(0, symbol_to_write)
        head_pos = 0
    elif head_pos >= len(tape):

        while len(tape) <= head_pos:
            tape.append(BLANK)
        tape[head_pos] = symbol_to_write
    else: 
        tape[head_pos] = symbol_to_write
    
    current_state = found_transition_rule["next_state"]
    
    move = found_transition_rule["move"]
    if move == "R":
        head_pos += 1
    elif move == "L":
        head_pos -= 1
  
if current_state in final_states:
    print("Acceptat")
else:
    print("Respins")