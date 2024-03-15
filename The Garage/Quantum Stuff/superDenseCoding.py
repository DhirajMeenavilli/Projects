import cirq
import numpy as np

def make_circuit(msg):
    circuit = cirq.Circuit()
    alice, bob = cirq.LineQubit.range(2)
    
    circuit.append([cirq.H(alice), cirq.CNOT(alice, bob)])

    circuit.append([msg(alice)])

    circuit.append([cirq.CNOT(alice, bob), cirq.H(alice)])

    circuit.append([cirq.measure(alice, key="Alice"), cirq.measure(bob, key="Bob")])
    return circuit

sim = cirq.Simulator()
circuit = make_circuit(cirq.X)

final_results = sim.run(program=circuit, repetitions=1)

a = np.array(final_results.measurements['Alice'][:, 0])
b = np.array(final_results.measurements['Bob'][:, 0])

print(a)
print(b)