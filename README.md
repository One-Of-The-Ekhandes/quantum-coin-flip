# Quantum Coin Flip
This project simulates a quantum coin flip using Qiskit 1.4.

## How It Works
- A single qubit is put in **superposition** using the Hadamard gate.
- When measured, the qubit collapses to **0 (Tails) or 1 (Heads)** with equal probability.
- The experiment is repeated **1024 times**, and results are counted.

## How to Run
1. Install Qiskit:  
pip install qiskit
markdown
Copy
Edit
2. Run the script:  
python quantum_coin_flip.py
lua
Copy
Edit
3. Check the output:  
{'0': 508, '1': 516}
markdown
Copy
Edit
- The output should be roughly 50-50, just like a fair coin flip.

## Contributing
- Feel free to fork this repo and improve it.
- You can modify it to use **real IBM Quantum computers** instead of a simulator.

## Author
- [Rujuta]