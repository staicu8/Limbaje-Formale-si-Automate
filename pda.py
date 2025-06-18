import json

with open('pda.json', 'r') as f:
    config = json.load(f)

# starea curenta este cea de start
current_state = config["start"]

stack = []  # stiva PDA
routes = config["routes"]  # tranzitiile
final_states = config["final"]  # starile finale

# verificam daca exista o tranzitie epsilon la inceput
for route in routes:
    if route["inc"] == current_state and route["read"] == "ε":
        if route["push"] != "ε":
            stack.append(route["push"])  # punem ceva pe stiva
        current_state = route["fin"]  # trecem in noua stare
        break

# citim sirul de la utilizator
input_string = input("Introduceti sirul: ")

# parcurgem fiecare caracter
for char_input in input_string:
    found_transition_for_char = False

    # cautam o tranzitie care se potriveste
    for route in routes:
        if route["inc"] == current_state and route["read"] == char_input:

            # daca nu trebuie sa scoata nimic sau scoate ce e in varf
            if route["pop"] == "ε" or (stack and stack[-1] == route["pop"]):

                if route["pop"] != "ε":
                    stack.pop()  # scoatem din stiva

                if route["push"] != "ε":
                    stack.append(route["push"])  # adaugam in stiva

                current_state = route["fin"]  # trecem in noua stare
                found_transition_for_char = True
                break

    # daca nu s-a putut face nicio tranzitie pentru caracterul curent
    if not found_transition_for_char:
        print("Respins")
        exit()

# verificam daca mai avem o tranzitie epsilon dupa terminarea sirului
for route in routes:
    if route["inc"] == current_state and route["read"] == "ε":
        if route["pop"] != "ε" and stack and stack[-1] == route["pop"]:
            stack.pop()
        current_state = route["fin"]
        break

# verificam daca starea curenta e finala si stiva e goala
if current_state in final_states and not stack:
    print("Acceptat")
else:
    print("Respins")
