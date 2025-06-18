import json

nume_fisier = 'nfa_joc.json'

# citim datele din fisierul json
with open(nume_fisier, 'r') as f:
    config_joc = json.load(f)

lista_camere = config_joc["states"]         # toate camerele din joc
miscarile_permise = config_joc["sigma"]     # miscarile valide
tranzitii = config_joc["routes"]            # reguli de mutare
camera_initiala = config_joc["start"][0]    # camera de start
camera_iesire = config_joc["final"][0]      # camera unde trebuie sa ajungi

# locatia unde se afla cheia si cum se numeste obiectul
camera_unde_e_cheia = "Bucatarie"
nume_obiect_cheie = "lingura"

# afisam instructiunile jocului
print("--- Jocul Aventurii (Versiune Simpla) ---")
print(f"Camere: {', '.join(lista_camere)}")
print(f"Miscarile sunt: 0 (Nord) 1 (Est) 2 (Sud) 3 (Vest)")
print(f"Pornesti din: {camera_initiala}")
print(f"Obiectiv: Ia '{nume_obiect_cheie}' din '{camera_unde_e_cheia}' si ajungi la '{camera_iesire}'")
print("-------------------------------------------")

# citim miscarile de la jucator
secventa_introdusa = input("Introdu secventa de miscari: ")


locatie_curenta = camera_initiala
are_cheia = False

print(f"\nAi pornit din: {locatie_curenta}")

# procesam fiecare miscare
for miscare in secventa_introdusa:
    if miscare not in miscarile_permise:
        print(f" -> '{miscare}' nu e o miscare valida")
        continue

    mutare_gasita = False
    for regula in tranzitii:
        if regula["inc"] == locatie_curenta and regula["state"] == miscare:
            locatie_curenta = regula["fin"]
            print(f" -> Te-ai mutat in: {locatie_curenta}")
            mutare_gasita = True
            break

    if not mutare_gasita:
        print(f" -> Nu te poti muta asa din {locatie_curenta}")

    if locatie_curenta == camera_unde_e_cheia and not are_cheia:
        are_cheia = True
        print(f" *** Ai gasit: {nume_obiect_cheie} in {camera_unde_e_cheia}! ***")

print("-------------------------------------------")
print(f"Joc terminat. Locatia finala: {locatie_curenta}")
if are_cheia:
    print(f"Ai la tine: {nume_obiect_cheie}")
else:
    print(f"NU ai la tine: {nume_obiect_cheie}")

if locatie_curenta == camera_iesire:
    if are_cheia:
        print("Felicitari! Ai evadat cu cheia! Ai CASTIGAT!")
    else:
        print(f"Ai ajuns la iesire dar ai uitat '{nume_obiect_cheie}'. Pierdut!")
else:
    if are_cheia:
        print(f"Ai '{nume_obiect_cheie}' dar nu la iesire. Mai incearca!")
    else:
        print("Esti pierdut si fara cheie. Pierdut!")
