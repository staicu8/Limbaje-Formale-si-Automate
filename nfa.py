import json

with open('nfa.json', 'r') as f:
    config = json.load(f)

final_states = config["final"]        
routes = config["routes"]             
start_states= config["start"]
EPSILON = config.get("epsilon_symbol", "ε") 

def epsilon_closure(initial_states_set, all_routes):
    closure = set(initial_states_set)
    worklist = list(initial_states_set) 
    
    idx = 0
    while idx < len(worklist):
        current_s = worklist[idx]
        idx += 1
        
        for route in all_routes:
            if route["inc"] == current_s and route["state"] == EPSILON:
                for next_s in route["fin"]:
                    if next_s not in closure:
                        closure.add(next_s)
                        worklist.append(next_s)
    return closure

input_string = input("Introduceti sirul pentru NFA: ")

active_states = epsilon_closure(set(start_states), routes)

for symbol in input_string:
    next_states_after_symbol_transition = set()
    for current_active_state in active_states:
        for route in routes:
            if route["inc"] == current_active_state and route["state"] == symbol:

                next_states_after_symbol_transition.update(route["fin"]) 
    
    active_states = epsilon_closure(next_states_after_symbol_transition, routes)
    

    if not active_states:
        break

accepted = False
for state in active_states:
    if state in final_states:
        accepted = True
        break

if accepted:
    print("Acceptat")
else:
    print("Respins")