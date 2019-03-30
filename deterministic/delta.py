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
		return True if state in self.delta else False

	def print_n_character(self, size, character = " "):
		return "".join(character for s in range(size))

	def __str__(self):
		string = " "

		biggest_state_size = 0
		for state in self.states:
			if biggest_state_size < len(state):
				biggest_state_size = len(state)

		n_characters = self.print_n_character(biggest_state_size - 1)
		string += self.print_n_character(biggest_state_size)

		for symbol in self.alphabet:
			string += f"{SEPARATOR} {symbol} {n_characters}"

		header_separator = self.print_n_character(len(self.alphabet) * len(SEPARATOR) * biggest_state_size + 1, '-')
		string += f"\n {SEPARATOR} {header_separator}"

		for state in self.states:
			string += f"\n   {state} {self.print_n_character(biggest_state_size - len(state))}"
			for symbol in self.alphabet:
				string += f"{SEPARATOR} {self.get_transition(state, symbol)} {n_characters}"
		return string
