SEPARATOR = "   "

class TransitionsDfa:
    def __init__(self, states, alphabet):
        self.states = states
        self.alphabet = alphabet
        self.delta = {}
        self.symbols = {}
        for letter in alphabet:
            self.symbols[letter] = None
        for state in states:
            self.add_state(str(state))

    def get_adjacents(self):
        symbols = {}
        for letter in self.alphabet:
            symbols[letter] = None
        return symbols
    
    def add_state(self, state):
        self.states.append(state)
        self.delta[state] = self.get_adjacents()

    def add_transition(self, initial_state, symbol, final_state):
        self.delta[initial_state][symbol] = final_state

    def get_transition_at_position(self, state, symbol):
        return self.delta[state][symbol]

    def has_state(self, state):
        if state in self.delta:
            return True
        else:
            return False

    def print_n_character(self, size, character = " "):
        string = ""
        for x in range(size):
            string += character
        return string

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
