# Importing necessary libraries
from qiskit import QuantumCircuit
from qiskit_aer  import AerSimulator  # ✅ Use the new simulator



qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

backend = AerSimulator()  # ✅ Use AerSimulator instead of `get_backend`
job = backend.run(qc, shots=1024)  # ✅ Use `run()` instead of `execute`
result = job.result()
counts = result.get_counts()
print(counts)

