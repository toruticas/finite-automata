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

	def __str__(self):
		string = " "

		biggest_state_size = 0
		for state in self.states:
			for symbol in self.alphabet:
				if self.delta[state][symbol]:
					transition_size = len("".join([str(x) for x in self.delta[state][symbol]]))
					size = transition_size + len(self.delta[state][symbol]) - 1
					if biggest_state_size < size: biggest_state_size = size

		string += self.print_n_character(biggest_state_size)
		for symbol in self.alphabet: string += f"{SEPARATOR} {symbol} {self.print_n_character(biggest_state_size - 1)}"

		header_separator = self.print_n_character(len(self.alphabet)*len(SEPARATOR)*biggest_state_size + 1, '-')
		string += f"\n {SEPARATOR} {header_separator}"

		for state in self.states:
			string += f"\n   {state} {self.print_n_character(biggest_state_size - len(state))}"
			for symbol in self.alphabet:
				conjunt = self.get_transition_at_position(state, symbol)
				conjunt_str = "{" + ",".join([str(x) for x in self.delta[state][symbol]]) + "}"
				string += SEPARATOR + conjunt_str + self.print_n_character(biggest_state_size - 1)

		return string

