SEPARATOR = "   "

class TransitionsNfa:
	def __init__(self, states, alphabet):
		self.states = states
		self.alphabet = alphabet
		self.delta = {}
		self.symbols = { letter: [] for letter in alphabet }
		for state in states: self.add_state(str(state))

	def get_adjacents(self):
		return { letter: [] for letter in self.alphabet }

	def add_state(self, state):
		self.delta[state] = self.get_adjacents()

	def add_transition(self, initial_state, symbol, final_state):
		if final_state not in self.delta[initial_state][symbol]:
			self.delta[initial_state][symbol].append(final_state)

	def get_juction_of_states(self, initial_states, symbol):
		new_states = []
		for initial_state in initial_states:
			for final_state in self.delta[str(initial_state)][symbol]:
				if final_state not in new_states:
					new_states.append(final_state)
		return new_states

	def get_transition_at_position(self, state, symbol):
		return self.delta[state][symbol]

	def print_n_character(self, size, character = " "):
		return "".join(str(character) for s in range(size))

	def __str__(self):
		string = " "

		biggest_state_size = 0
		for state in self.states:
			for symbol in self.alphabet:
				if self.delta[str(state)][str(symbol)]:
					size = len("".join([str(x) for x in self.delta[str(state)][str(symbol)]])) + len(self.delta[str(state)][str(symbol)]) - 1
					if biggest_state_size < size:
						biggest_state_size = size

		string += self.print_n_character(biggest_state_size)
		for symbol in self.alphabet:
			string += SEPARATOR + symbol + self.print_n_character(biggest_state_size - 1)

		string += "\n" + SEPARATOR + self.print_n_character(len(self.alphabet)*len(SEPARATOR)*biggest_state_size + 1, "-")

		for state in self.states:
			string += "\n   " + str(state) + self.print_n_character(biggest_state_size - len(str(state)))
			for symbol in self.alphabet:
				conjunt = self.get_transition_at_position(str(state), str(symbol))
				conjunt_str = "{" + ",".join([str(x) for x in self.delta[str(state)][str(symbol)]]) + "}"
				string += SEPARATOR + conjunt_str + self.print_n_character(biggest_state_size - 1)

		return string

