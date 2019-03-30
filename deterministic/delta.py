SEPARATOR = "   "

class TransitionsDfa:
	def __init__(self, states, alphabet):
		self.states = states
		self.alphabet = alphabet
		self.delta = {}
		self.symbols = self.get_adjacents()
		for state in states: self.add_state(str(state))

	def get_adjacents(self):
		return { letter: None for letter in self.alphabet }

	def add_state(self, state):
		self.states.append(state)
		self.delta[state] = self.get_adjacents()

	def add_transition(self, initial_state, symbol, final_state):
		self.delta[initial_state][symbol] = final_state

	def get_transition_at_position(self, state, symbol):
		return self.delta[state][symbol]

	def has_state(self, state):
		return True if state in self.delta else False

	def print_n_character(self, size, character = " "):
		return "".join(str(character) for s in range(size))

	def __str__(self):
		string = " "

		biggest_state_size = 0
		for state in self.states:
			if biggest_state_size < len(state):
				biggest_state_size = len(state)

		string += self.print_n_character(biggest_state_size)
		for symbol in self.alphabet:
			string += SEPARATOR + symbol + self.print_n_character(biggest_state_size - 1)

		string += "\n" + SEPARATOR + self.print_n_character(len(self.alphabet)*len(SEPARATOR)*biggest_state_size + 1, "-")

		for state in self.states:
			string += "\n   " + state + self.print_n_character(biggest_state_size - len(state))
			for symbol in self.alphabet:
				string += SEPARATOR + self.get_transition_at_position(state, symbol) + self.print_n_character(biggest_state_size - 1)
		return string
