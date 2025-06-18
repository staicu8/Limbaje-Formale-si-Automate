import json

# incarca configuratia din fisierul json
with open('nfa.json', 'r') as f:
    config = json.load(f)

final_states = config["final"]        # starile finale
routes = config["routes"]             # lista cu tranzitii
start_states = config["start"]        # starile de start
EPSILON = config.get("epsilon_symbol", "ε")  # simbolul folosit pentru epsilon


# calculam inchiderea epsilon a unui set de stari
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


# citeste sirul de la utilizator
input_string = input("Introduceti sirul pentru NFA: ")

# pornim cu starile de start si aplicam inchiderea epsilon
active_states = epsilon_closure(set(start_states), routes)

# procesam fiecare simbol din sir
for symbol in input_string:
    next_states_after_symbol_transition = set()
    for current_active_state in active_states:
        for route in routes:
            if route["inc"] == current_active_state and route["state"] == symbol:
                # adauga starile in care putem ajunge dupa simbol
                next_states_after_symbol_transition.update(route["fin"])
    
    # calculam inchiderea epsilon pentru noile stari
    active_states = epsilon_closure(next_states_after_symbol_transition, routes)

    if not active_states:
        break  # daca nu mai avem stari active iesim


# verificam daca una din starile active este finala
accepted = False
for state in active_states:
    if state in final_states:
        accepted = True
        break

# afisam rezultatul
if accepted:
    print("Acceptat")
else:
    print("Respins")
