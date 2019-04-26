#!/usr/bin/env python3

LAMBDA_SYMBOL = "-"

class Deterministic:
	def __init__(self, states, alphabet, delta, initial_state, acceptance_states):
		self.states = states
		self.alphabet = alphabet
		self.delta = delta
		self.initial_state = initial_state
		self.acceptance_states = acceptance_states

	def process(self, chain):
		next_state = self.initial_state
		if chain == LAMBDA_SYMBOL and next_state in self.acceptance_states: return True
		for symbol in chain:
			if not symbol in self.alphabet: return False
			next_state = self.delta.get_transition(next_state, symbol)
			if next_state == None: return False
		if next_state in self.acceptance_states:
			return True
		else:
			return False

SEPARATOR = "   "

class TransitionsDfa:
	def __init__(self, states, alphabet):
		self.states = states
		self.alphabet = alphabet
		self.delta = {}
		self.symbols = self.get_adjacents()
		for state in states: self.add_state(state)

	def get_adjacents(self):
		return { letter: None for letter in self.alphabet }

	def add_state(self, state):
		self.states.add(state)
		self.delta[state] = self.get_adjacents()

	def add_transition(self, initial_state, symbol, final_state):
		self.delta[initial_state][symbol] = final_state

	def get_transition(self, state, symbol):
		return self.delta[state][symbol]

	def has_state(self, state):
		if state in self.delta:
			return True
		else:
			return False

	def print_n_character(self, size, character = " "):
		return "".join(character for s in range(size))

class Nondeterministic:
	def __init__(self, states, alphabet, delta, initial_states, acceptance_states):
		self.states = states
		self.alphabet = alphabet
		self.delta = delta
		self.initial_states = initial_states
		self.acceptance_states = acceptance_states
		self.dfa_equivalent = self.equivalent_deterministic()

	def equivalent_deterministic(self):
		dfa_new_states = set()
		dfa_new_acceptance_states = set()
		dfa_new_initial_state = "".join([str(x) for x in self.initial_states])
		dfa_delta = TransitionsDfa(set(), self.alphabet)

		states_to_be_processed = []
		states_to_be_processed.append(self.initial_states)

		while len(states_to_be_processed) > 0:
			next_state_set = states_to_be_processed.pop(0)
			next_state_name = "".join([str(x) for x in next_state_set])

			if dfa_delta.has_state(next_state_name): continue
			if self.acceptance_states.intersection(next_state_set): dfa_new_acceptance_states.add(next_state_name)

			dfa_new_states.add(next_state_name)
			dfa_delta.add_state(next_state_name)

			for symbol in self.alphabet:
				final_states = self.delta.get_juction_of_states(next_state_set, symbol)
				final_state = "".join([str(x) for x in final_states])
				dfa_delta.add_transition(next_state_name, symbol, final_state)
				if not dfa_delta.has_state(final_state):
					states_to_be_processed.append(final_states)

		return Deterministic(
			dfa_new_states, self.alphabet, dfa_delta, dfa_new_initial_state, dfa_new_acceptance_states)

	def process(self, chain):
		return self.dfa_equivalent.process(chain)

SEPARATOR = "   "

class TransitionsNfa:
	def __init__(self, states, alphabet):
		self.states = states
		self.alphabet = alphabet
		self.delta = {}
		self.symbols = { letter: set() for letter in alphabet }
		for state in states: self.add_state(state)

	def get_adjacents(self):
		return { letter: set() for letter in self.alphabet }

	def add_state(self, state):
		self.delta[state] = self.get_adjacents()

	def add_transition(self, initial_state, symbol, final_state):
		if final_state not in self.delta[initial_state][symbol]:
			self.delta[initial_state][symbol].add(final_state)

	def get_juction_of_states(self, initial_states, symbol):
		new_states = []
		for initial_state in initial_states:
			for final_state in self.delta[initial_state][symbol]:
				if final_state not in new_states:
					new_states.append(final_state)
		return new_states

	def get_transition_at_position(self, state, symbol):
		return self.delta[state][symbol]

	def print_n_character(self, size, character = " "):
		return "".join(character for s in range(size))


def read_number_of_states():
	number_of_states = int(raw_input().strip())
	# print(number_of_states)
	if number_of_states < 1 or number_of_states > 10:
		raise Exception("1 <= number of initial states <= 10")
	return set(str(x) for x in range(number_of_states))

def read_alphabet():
	alphabet_list = raw_input().strip().split(" ")
	# print(alphabet_list)
	if len(alphabet_list) - 1 != int(alphabet_list[0]):
		raise Exception("O tamanho do alfabeto diverge do alfabeto informado.")
	return alphabet_list[slice(1, int(alphabet_list[0]) + 1)]

def read_number_of_initial_states(number_of_states):
	number_of_initial_states = int(raw_input().strip())
	# print(number_of_initial_states)
	if number_of_initial_states > number_of_states:
		raise Exception("O numero de estados finais deve ser menor ou igual ao numero de estados iniciais.")
	return set(str(x) for x in range(number_of_initial_states))

def read_acceptance_states(states):
	input_value = raw_input().strip()
	# print(input_value)
	acceptance_states_list = input_value.split(" ")
	if len(acceptance_states_list) -1 != int(acceptance_states_list[0]):
		raise Exception("You must inform " + len(acceptance_states_list) + " acceptance states")
	acceptance_states_list = acceptance_states_list[slice(1, int(acceptance_states_list[0]) + 1)]
	for state in acceptance_states_list:
		if state not in states:
			raise Exception("The acceptance state " + state + " must exists.")
	return set(acceptance_states_list)

def read_transitions(states, alphabet):
	transitions = TransitionsNfa(states, alphabet)
	number_of_transitions = int(raw_input().strip())
	# print(number_of_transitions)
	for x in range(number_of_transitions):
		data = raw_input().strip().split(" ")
		# print(data)
		transitions.add_transition(data[0], data[1], data[2])
	return transitions

states = read_number_of_states()
alphabet = read_alphabet()
initial_states = read_number_of_initial_states(len(states))
acceptance_states = read_acceptance_states(states)
delta = read_transitions(states, alphabet)

afn = Nondeterministic(states, alphabet, delta, initial_states, acceptance_states)


number_of_chains = int(raw_input().strip())

for x in range(number_of_chains):
	chain = raw_input().strip()
	if afn.process(chain):
		print("aceita")
	else:
		print("rejeita")
