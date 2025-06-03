import json


with open('pda.json', 'r') as f:
    config = json.load(f)

current_state = config["start"]
stack = []
routes = config["routes"]
final_states = config["final"]

for route in routes:
    if route["inc"] == current_state and route["read"] == "ε":
        if route["push"] != "ε":
            stack.append(route["push"])
        current_state = route["fin"]
        break 

input_string = input("Introduceti sirul: ")

for char_input in input_string:
    found_transition_for_char = False
    for route in routes:
        if route["inc"] == current_state and route["read"] == char_input:
     
            if route["pop"] == "ε" or (stack and stack[-1] == route["pop"]):
           
                if route["pop"] != "ε":
                    stack.pop() 
 
                if route["push"] != "ε":
                    stack.append(route["push"])
                
                current_state = route["fin"]
                found_transition_for_char = True
                break 
    
    if not found_transition_for_char:
        print("Respins")
        exit()


for route in routes:
    if route["inc"] == current_state and route["read"] == "ε":

        if route["pop"] != "ε" and stack and stack[-1] == route["pop"]:
            stack.pop()
        current_state = route["fin"]
        break 


if current_state in final_states and not stack:
    print("Acceptat")
else:
    print("Respins")