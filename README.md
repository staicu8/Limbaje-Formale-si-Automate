## Deterministic Finite Automata (DFA)

Script-ul (`dfa.py`) încarcă un DFA dintr-un fișier text și verifică dacă un șir introdus este acceptat de acesta.

### Formatul fișierului de intrare (`dfa.txt`)
Exemplu (`dfa.txt`):

[States]
q0,0 # q0 este starea inițială
q1,2
q2,1 # q2 este stare finală
[End]

[Alphabet]
0
1
[End]

[Transitions]
q0,q1,0 # din q0, pe 0, merg în q1
q0,q0,1
q1,q1,0
q1,q2,1
q2,q1,0
q2,q0,1
[End]
### Ce face codul

1. Încarcă definiția unui DFA dintr-un fișier `.txt`
2. Așteaptă un șir de la utilizator
3. Rulează șirul prin automat și returnează `True` dacă este acceptat (ajunge într-o stare finală)

## Nondeterministic Finite Automata (NFA)

Script-ul (`nfa.py`) simuleaza un NFA incarcat dintr-un fisier `.json`.

### Formatul fisierului de intrare (`nfa.json`)

Exemplu:
nfa.json
{
  "alphabet": ["0", "1"],
  "epsilon_symbol": "ε",
  "start": ["q0"],
  "final": ["q2"],
  "routes": [
    { "inc": "q0", "state": "0", "fin": ["q0", "q1"] },
    { "inc": "q0", "state": "ε", "fin": ["q1"] },
    { "inc": "q1", "state": "1", "fin": ["q2"] },
    { "inc": "q2", "state": "0", "fin": ["q2"] }
  ]
}

### Ce face codul
Citeste configuratia unui NFA din fisierul nfa.json

Calculeaza inchiderea epsilon a starilor curente

Simuleaza pas cu pas fiecare simbol din input

Accepta daca cel putin o stare activa finala este atinsa


**## Joc Aventura cu Automate NFA

Script-ul (`nfa_joc.py`) simuleaza un joc cu ajutorul unui NFA.

### Obiectiv
- Gaseste obiectul ascuns (lingura) dintr-o anumita camera
- Apoi ajungi la camera de iesire cu obiectul

### Miscarile Permise
- `0` = Nord
- `1` = Est
- `2` = Sud
- `3` = Vest

### Formatul fisierului `nfa_joc.json`

nfa_joc.json
{
  "states": ["HolIntrare", "Sufragerie", "Bucatarie", "Dormitor", "Baie", "Iesire"],
  "sigma": ["0", "1", "2", "3"],
  "start": ["HolIntrare"],
  "final": ["Iesire"],
  "routes": [
    {"inc": "HolIntrare", "state": "1", "fin": "Sufragerie"},
    {"inc": "HolIntrare", "state": "2", "fin": "Baie"},
    {"inc": "Sufragerie", "state": "3", "fin": "HolIntrare"},
    {"inc": "Sufragerie", "state": "1", "fin": "Bucatarie"},
    {"inc": "Sufragerie", "state": "0", "fin": "Dormitor"},
    {"inc": "Bucatarie", "state": "3", "fin": "Sufragerie"},
    {"inc": "Bucatarie", "state": "2", "fin": "Iesire"},
    {"inc": "Dormitor", "state": "2", "fin": "Sufragerie"},
    {"inc": "Baie", "state": "0", "fin": "HolIntrare"}
  ]
}


### Exemplu de joc:
Introdu secventa de miscari: 1032
Ai pornit din: HolIntrare
 -> Te-ai mutat in: Sufragerie
 -> Te-ai mutat in: Bucatarie
 *** Ai gasit: lingura in Bucatarie! ***
 -> Te-ai mutat in: Iesire
Joc terminat. Locatia finala: Iesire.
Ai la tine: lingura.
Felicitari! Ai evadat cu cheia! Ai CASTIGAT!

## Pushdown Automata(PDA)

Scriptul(`pda.py`) simuleaza un PDA (Pushdown Automaton).

### Fisier de configurare: `pda.json`

{
  "start": "q0",
  "final": ["q0", "q3"],
  "routes": [
    { "inc": "q0", "read": "ε", "pop": "ε", "push": "Z0", "fin": "q1" },
    { "inc": "q1", "read": "a", "pop": "ε", "push": "A", "fin": "q1" },
    { "inc": "q1", "read": "ε", "pop": "ε", "push": "ε", "fin": "q2" },
    { "inc": "q2", "read": "b", "pop": "A", "push": "ε", "fin": "q2" },
    { "inc": "q2", "read": "ε", "pop": "Z0", "push": "ε", "fin": "q3" }
  ]
}

# Simulare Masina Turing


Script-ul (`masina_turing.py`) implementeaza o masina turing simpla configurabila prin fisier json.

## Fisier: masina_turing.json

- `start_state`: starea initiala
- `final_states`: multimea starilor acceptate
- `blank_symbol`: simbolul folosit pentru spatiile libere
- `transitions`: lista de tranzitii in format complet

### Ex:
{
  "start_state": "q0",
  "final_states": ["q_accept"],
  "blank_symbol": "B",
  "transitions": [
    {
      "current_state": "q0",
      "read_symbol": "0",
      "next_state": "q1",
      "write_symbol": "0",
      "move": "R"
    },
    {
      "current_state": "q1",
      "read_symbol": "1",
      "next_state": "q2",
      "write_symbol": "1",
      "move": "R"
    },
    {
      "current_state": "q2",
      "read_symbol": "0",
      "next_state": "q3",
      "write_symbol": "0",
      "move": "R"
    },
    {
      "current_state": "q3",
      "read_symbol": "B",
      "next_state": "q_accept",
      "write_symbol": "B",
      "move": "S"
    }
  ]
}
