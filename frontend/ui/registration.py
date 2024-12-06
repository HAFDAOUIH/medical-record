import tkinter as tk
from web3 import Web3
import json

class PatientRegistration(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Patient Registration")
        self.geometry("400x200")

        self.label = tk.Label(self, text="Enter Patient Encryption Key")
        self.label.pack()

        self.encryption_key_entry = tk.Entry(self, width=30)
        self.encryption_key_entry.pack(pady=10)

        self.register_button = tk.Button(self, text="Register Patient", command=self.register_patient)
        self.register_button.pack(pady=10)

    def register_patient(self):
        encryption_key = self.encryption_key_entry.get()
        
        if encryption_key:
            # Web3 setup
            w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

            # Load contract ABI
            with open('build/contracts/PatientContract.json', 'r') as abi_file:
                abi = json.load(abi_file)['abi']

            # Contract address from deployment
            contract_address = '0x5a6d9a6E8F327fB7F52aef83055792893702D42F'

            # Create contract instance
            contract = w3.eth.contract(address=contract_address, abi=abi)

            # Register the patient by calling the contract function
            tx_hash = contract.functions.registerPatient(encryption_key).transact({
                'from': w3.eth.accounts[0]  # Make sure to use a valid account from Ganache
            })

            # Wait for the transaction receipt
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            print("Patient registered:", receipt)
            tk.Label(self, text=f"Patient Registered! Tx Hash: {tx_hash.hex()}").pack(pady=10)
        else:
            print("Encryption key is required.")

# Run the Tkinter app
if __name__ == "__main__":
    app = PatientRegistration()
    app.mainloop()
