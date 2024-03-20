import cirq
import numpy as np
import random

def make_circuit(transform):
    circuit = cirq.Circuit()
    q0, q1 = cirq.LineQubit.range(2)

    circuit.append([cirq.X(q1)])
    circuit.append([cirq.H(q0), cirq.H(q1)])

    if transform == "f0":
        circuit.append([]) # |00> -> |00>, |01> -> |01>, |10> -> |10>, |11> -> |11>
    if transform == "f1":
        circuit.append([cirq.X(q1)])# |00> -> |01>, |01> -> |00>, |10> -> |11>, |11> -> |10>
    if transform == "fx":
        circuit.append([cirq.CNOT(q0, q1)]) # |00> -> |00>, |01> -> |01>, |10> -> |11>, |11> -> |10>
    if transform == "fex":
        circuit.append([cirq.CNOT(q0, q1), cirq.X(q1)]) # |00> -> |01>, |01> -> |00>, |10> -> |10>, |11> -> |11>
    
    circuit.append([cirq.H(q0), cirq.measure(q0, key="Bit 1")])
    print(circuit)
    return circuit

sim = cirq.Simulator()
circuit = make_circuit("fex")

final_results = sim.run(program=circuit, repetitions=5)

print(np.array(final_results.measurements['Bit 1'][:, 0]))