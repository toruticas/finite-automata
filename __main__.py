from nondeterministic.algorithm import Nondeterministic
from nondeterministic.delta import TransitionsNfa

def read_number_of_states():
	number_of_states = int(input())
	if number_of_states < 1 or number_of_states > 10:
		raise Exception("1 ≤ number of initial states ≤ 10")
	return set(str(x) for x in range(number_of_states))

def read_alphabet():
	alphabet_list = input().split(" ")
	if len(alphabet_list) - 1 != int(alphabet_list[0]):
		raise Exception("O tamanho do alfabeto diverge do alfabeto informado.")
	return alphabet_list[slice(1, int(alphabet_list[0]) + 1)]

def read_number_of_initial_states(number_of_states):
	number_of_initial_states = int(input())
	if number_of_initial_states > number_of_states:
		raise Exception("O número de estados finais deve ser menor ou igual ao número de estados iniciais.")
	return set(str(x) for x in range(number_of_initial_states))

def read_acceptance_states(states):
	input_value = input()
	acceptance_states_list = input_value.split(" ")
	if len(acceptance_states_list) -1 != int(acceptance_states_list[0]):
		raise Exception(f"You must inform '{len(acceptance_states_list)}' acceptance states")
	acceptance_states_list = acceptance_states_list[slice(1, int(acceptance_states_list[0]) + 1)]
	for state in acceptance_states_list:
		if state not in states:
			raise Exception(f"The acceptance state '{state}' must exists.")
	return set(acceptance_states_list)

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

afn = Nondeterministic(states, alphabet, delta, initial_states, acceptance_states)

print("\n-----\n")
print(afn)
print("\n-----\n")
print(afn.dfa_equivalent)
print("\n-----\n")

number_of_chains = int(input())

for x in range(number_of_chains):
	chain = input()
	print("aceita") if afn.process(chain) else print("rejeita")
