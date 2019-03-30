from deterministic.delta import TransitionsDfa

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
		return True if next_state in self.acceptance_states else False

	def __str__(self):
		string = "Q:"
		for state in self.states: string += " " + state
		string += "\nΣ:"
		for symbol in self.alphabet: string += " " + symbol
		string += "\nδ:" + self.delta.__str__()
		string += "\nq: " + self.initial_state
		string += "\nF:"
		for state in self.acceptance_states: string += " " + state
		return string

