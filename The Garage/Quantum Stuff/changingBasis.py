# First have a qubit which is in some binomial distribution between ground and excited, then have the second qubit assume the firsts position, and collapse it under a different measurement basis.

import random
import numpy as np
import cirq

def make_bell_test_circuit():
    a = cirq.GridQubit(0, 0) # Intialises a qubit at the row 0 col 0
    b = cirq.GridQubit(1, 0) # Intialises a qubit at the row 1 col 0
    a_ref = cirq.GridQubit(0, 1)
    b_ref = cirq.GridQubit(1, 1)

    circuit = cirq.Circuit() # Intialising the circuit

    # Preparing an entangled pair
    circuit.append([cirq.H(a), cirq.CNOT(a,b), cirq.X(a)**-0.25]) 
    # So the circuit is basically Haddamarding Alices qubit, then doing a control not with Bobs qubit, entangling the two, and then 4th root NOTing alices qubit 
    
    # Referee circuits
    circuit.append([cirq.H(a_ref), cirq.H(b_ref)]) # Somehow this results in both the a_ref and b_ref lines being drawn.

    # Players flip their basis according to the outcome of the referee bit.
    circuit.append([cirq.CNOT(a_ref, a)**0.5, cirq.CNOT(b_ref, b)**0.5])

    # Then we measure
    circuit.append([cirq.measure(a, key="Alice"), cirq.measure(b, key="Bob"), cirq.measure(a_ref, key="Alice Ref"), cirq.measure(b_ref, key="Bob Ref")])

    return circuit

wins = 0.0

# Game

for i in range(1000000):
    x, y = random.randint(0,1),random.randint(0,1) #So Alice and Bob recieve either 0 or 1 as thir input.
    a, b = 0, 0 # Alica and Bobs bits, without Qubits this is the optimal strategy and after 1,000,000 trials it appears to be roughly coherent with a win rate of 75% 
    if x * y == 1:
        if a != b: # (a+b)%2 Basically just asking a and b not to be equal
            wins += 1.0

    else:
        if a == b:
            wins += 1.0

print("The win rate in the classical regime is: "+str(wins/1000000.0)+".")

circuit = make_bell_test_circuit()
results = cirq.Simulator().run(program=circuit, repetitions=1000000)

a = np.array(results.measurements['Alice'][:, 0]) # Getting all the measurments belonging to Alice by taking all the rows and only the first column
b = np.array(results.measurements['Bob'][:, 0])
a_ref = np.array(results.measurements['Alice Ref'][:, 0])
b_ref = np.array(results.measurements['Bob Ref'][:, 0])

outcomes = np.bitwise_xor(a, b) == np.bitwise_and(a_ref, b_ref) # Basically only if a_ref and b_ref is both 1 is there a 1 on the RHS in which a and b must xor i.e be different else RHS is 0 and LHS must be the same.

unique, counts = np.unique(outcomes, return_counts=True)

print("The win rate in the Quantum regime is: "+str(float(dict(zip(unique, counts))[True])/1000000.0)+".")