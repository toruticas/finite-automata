from nondeterministic.delta import TransitionsNfa
from deterministic.delta import TransitionsDfa
from deterministic.algorithm import Deterministic

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

class Nondeterministic:
    def __init__(self, states = [], alphabet = [], initial_states = [], acceptance_states = [], delta = None):
        self.states = states
        self.alphabet = alphabet
        self.initial_states = initial_states
        self.acceptance_states = acceptance_states
        self.delta = delta
        self.dfa_equivalent = self.equivalent_deterministic()

    def equivalent_deterministic(self):
        dfa_new_states = []
        dfa_new_acceptance_states = []
        dfa_new_initial_state = "".join([str(x) for x in self.initial_states])
        dfa_delta = TransitionsDfa([], self.alphabet)

        states_to_be_processed = []
        states_to_be_processed.append(self.initial_states)

        while len(states_to_be_processed) > 0:
            next_state_set = states_to_be_processed.pop(0)
            next_state_name = "".join([str(x) for x in next_state_set])
            
            if dfa_delta.has_state(next_state_name):
                continue

            inter = intersection(next_state_set, self.acceptance_states)
            if inter:
                dfa_new_acceptance_states.append(next_state_name)

            dfa_new_states.append(next_state_name)
                
            dfa_delta.add_state(next_state_name)

            for symbol in self.alphabet:
                final_states = self.delta.get_juction_of_states(next_state_set, symbol)
                final_state = "".join([str(x) for x in final_states])
                dfa_delta.add_transition(next_state_name, symbol, final_state)
                if not dfa_delta.has_state(final_state):
                    states_to_be_processed.append(final_states)
        
        return Deterministic(dfa_new_states, self.alphabet, dfa_delta, dfa_new_initial_state, dfa_new_acceptance_states)

    def process(self, chain):
        return self.dfa_equivalent.process(chain)

    def __str__(self):
        string = "Q:"
        for state in self.states:
            string += " " + str(state)

        string += "\nΣ:"
        for symbol in self.alphabet:
            string += " " + symbol

        string += "\nδ:" + self.delta.__str__()

        string += "\nq: "
        for state in self.initial_states:
            string += " " + str(state)

        string += "\nF:"
        for state in self.acceptance_states:
            string += " " + str(state)

        return string