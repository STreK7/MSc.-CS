from nfa_utils import *
import sys
import time

class NFA:
    """Class representing a non-deterministic finite automaton"""

    def __init__(self):
        """Creates a blank NFA"""

        # all NFAs have a single initial state by default
        self.alphabet = set()
        self.states = {0}
        self.transition_function = {}
        self.accept_states = set()

        # set of states that the NFA is currently in
        self.in_states = {0}

    def add_state(self, state, accepts=False):
        self.states.add(state)

        if accepts:
            self.accept_states.add(state)

    def add_transition(self, from_state, symbol, to_states):
        self.transition_function[(from_state, symbol)] = to_states

        if symbol != "":
            self.alphabet.add(symbol)


    def is_accepting(self):
        # accepts if we are in ANY accept states
        # ie. if in_states and accept_states share any states in common
        return len(self.in_states & self.accept_states) > 0


    def __str__(self):
        return "NFA:\n" \
               "Alphabet: {}\n" \
               "States: {}\n" \
               "Transition Function: \n {} \n" \
               "Accept States: {}\n" \
               "In states: {}\n" \
               "Accepting: {}\n"\
            .format(self.alphabet,
                    self.states,
                    self.transition_function,
                    self.accept_states,
                    self.in_states,
                    "Yes" if self.is_accepting() else "No")

if __name__ == "__main__":

    # regular expression string to compare against provided input
    regex = None
    regex_nfa = None
    # last line of user input read from the command line
    line_read = ""

    # read in line of user input
    line_read = input("Enter the regex pattern \n>")
    # make a lowercase copy of the input for case insensitive comparisons
    regex = line_read.lower()
    print("Given Regex pattern:", regex, "\n")
    print("Building NFA ")
    start_time = time.time()
    
    # turn regular expression string into an NFA object
    regex_nfa = get_regex_nfa(regex)
    
    finish_time = time.time()
    ms_taken = (finish_time - start_time) * 1000

    print("\nBuilt NFA in {:.3f} ms.\n".format(ms_taken))
    print(regex_nfa)

