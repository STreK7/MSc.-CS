"""Design to recognize strings NFA"""
import string
from collections import deque

class NFA:
    def __init__(self, states, symbols, t_state, start_state, final_state):     # initialization
        self.states = states                    # State set
        self.symbols = symbols                  # Input symbol set / alphabet
        self.t_state = t_state                  # State transition function
        self.start_state = start_state          # Start state
        self.final_state = final_state          # End state

    # The collection of the next state that the
    # current state can reach through a character, including empty closures
    def next_state(self, current_states, c):    
        next_states = []                        # The next state set, including the set of empty closures of the next state set
        for state in current_states:
            if state in self.t_state.keys():
                if c in self.t_state[state].keys():
                    n_states = self.t_state[state][c]
                    for s in n_states:          # Gets the empty closure of the next state set
                        s_closure = self.e_closure(s)
                        for s_c in s_closure:   # Add the set of empty closures to the next state set
                            if s_c not in next_states:
                                next_states.append(s_c)
        print('State transition:')
        print(current_states, end=' ')
        print('-' + c + '->', end=' ')
        print(next_states)
        return next_states                      # Returns the set of the next state obtained / the state set through the character c
    

    def e_closure(self, state):                 # Find the empty closure of a state
        d_state = deque()                       # Dual ended queue, storing intermediate status
        empty_bag = []                          # Empty closure of a state
        d_state.append(state)
        empty_bag.append(state)
        while (len(d_state)):
            current_state = d_state[0]
            if current_state in self.t_state.keys():  # If the current state exists
                if 'e' in self.t_state[current_state].keys():  # If there is a null character transfer
                    for s in self.t_state[current_state]['e']:
                        if s not in empty_bag:  # If the state is not in an empty closure
                            d_state.append(s)   # Queue and join the state arrived via e into the empty closure
                            empty_bag.append(s)
            d_state.popleft()                   # Throw the current state
        return empty_bag



    def match_final_state(self, final_current_states: list) ->bool :         # The final state matches the end state
        for state in final_current_states:
            if state in self.final_state:
                return True
        return False
    
    
    def read_string(self, input_str):           # Read string to enter NFA authentication
        for c in input_str:                     # Judge whether the string meets the alphabet
            if c not in self.symbols:
                print('Illegal character in string')
                return

        next_states = [self.start_state]
        for i in str:
            next_states = self.next_state(next_states, i)    #call
            #print(next_states)

        result = self.match_final_state(next_states)        #call
        if result == True:
            print('NFA This string is acceptable')
        else:
            print('NFA The string cannot be received')


if __name__ == '__main__':
    states = ['q1', 'q2', 'q3', 'q4']   # NFA state set
    symbols = ['0', '1']                # NFA alphabet
    t_state = {
        'q1': {
            '0': ['q1'],
            '1': ['q1', 'q2']
        },
        'q2': {
            'e': ['q3'],
            '0': ['q3']
        },
        'q3': {
            '1': ['q4']
        },
        'q4': {
            '0': ['q4'],
            '1': ['q4']
        }
    }                     # State transition function
    start_state = 'q1'                  # Start state
    final_state = ['q4']                # End state set

    while True:
        str = input("Please enter the test string:")
        if str == 'exit':
            break
        nfa = NFA(states, symbols, t_state, start_state, final_state)
        nfa.read_string(str)
