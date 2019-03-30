from nondeterministic.algorithm import Nondeterministic
from nondeterministic.delta import TransitionsNfa

def read_number_of_states():
    number_of_states = int(input())
    
    if number_of_states < 1 or number_of_states > 10:
        raise Exception("1 ≤ numero de estados iniciais ≤ 10")

    return list(range(number_of_states))

def read_alphabet():
    alphabet = input()
    alphabet_list = alphabet.split(" ")
    
    if len(alphabet_list) -1 != int(alphabet_list[0]):
        raise Exception("O tamanho do alfabeto diverge do alfabeto informado.")

    return alphabet_list[slice(1, int(alphabet_list[0]) + 1)]

def read_number_of_initial_states(number_of_states):
    number_of_initial_states = int(input())

    if number_of_initial_states > number_of_states:
        raise Exception("O número de estados finais deve ser menor ou igual ao número de estados iniciais.")

    return list(range(number_of_initial_states))

def read_acceptance_states(states):
    input_value = input()
    acceptance_states_list = input_value.split(" ")
    
    if len(acceptance_states_list) -1 != int(acceptance_states_list[0]):
        raise Exception("A quantidade de estados de aceitação diverge dos estados informados.")
        
    acceptance_states_list = acceptance_states_list[slice(1, int(acceptance_states_list[0]) + 1)]
    
    for state in acceptance_states_list:
        if int(state) not in states:
            raise Exception("O estado de aceitação '" + state + "' deve existir")
    
    return acceptance_states_list

def read_transitions(states, alphabet):
    transitions = TransitionsNfa(states, alphabet)
    number_of_transitions = int(input())

    for x in range(number_of_transitions):
        data = input().split(" ")
        transitions.add_transition(data[0], data[1], data[2])

    return transitions

states = read_number_of_states()
alphabet = read_alphabet()
initial_states = read_number_of_initial_states(len(states))
acceptance_states = read_acceptance_states(states)
delta = read_transitions(states, alphabet)

afn = Nondeterministic(states, alphabet, initial_states, acceptance_states, delta)

number_of_chains = int(input())

# print("\n-----\n")
# print(afn)
# print("\n-----\n")
# print(afn.dfa_equivalent)
# print("\n-----\n")

for x in range(number_of_chains):
    chain = input()
    print("aceita") if afn.process(chain) else print("rejeita")