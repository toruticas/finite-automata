from deterministic.delta import TransitionsDfa

LAMBDA_SYMBOL = "-"

class Deterministic:
    def __init__(self, states = [], alphabet = [], delta = {}, initial_state = None, acceptance_states = []):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.acceptance_states = acceptance_states
        self.delta = delta

    def process(self, chain):
        next_state = self.initial_state

        if chain == LAMBDA_SYMBOL and next_state in self.acceptance_states:
            return True

        for symbol in chain:
            if not symbol in self.alphabet:
                return False

            tmp_state = self.delta.get_transition_at_position(next_state, symbol)
            next_state = tmp_state
            if next_state == None:
                return False

        if next_state in self.acceptance_states:
            return True    
        else:
            return False

    def __str__(self):
        string = "Q:"
        for state in self.states:
            string += " " + str(state)

        string += "\nΣ:"
        for symbol in self.alphabet:
            string += " " + symbol

        string += "\nδ:" + self.delta.__str__()

        string += "\nq: " + self.initial_state

        string += "\nF:"
        for state in self.acceptance_states:
            string += " " + state

        return string

            