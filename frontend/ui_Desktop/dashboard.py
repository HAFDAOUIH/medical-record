import customtkinter as ctk
from tkinter import messagebox
import datetime
from web3 import Web3
import json
import os

class TransactionViewer(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Transaction Logs Viewer")
        self.geometry("900x500")

        # Initialize Web3 connection
        self.w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))  # Update with your provider URL
        self.contract_address = "0x1fA7aE314cE421d0BdA5540F92Bb53cBE450784C"  # Replace with your deployed contract address
        self.abi_path = "build/contracts/AuditContract.json"  # Update with the actual ABI path
        self.contract = self.load_contract()

        # Main Frame
        self.main_content1 = ctk.CTkFrame(self)
        self.main_content1.pack(fill="both", expand=True, padx=20, pady=20)

        self.view_transaction()

    def load_contract(self):
        """
        Loads the smart contract using the ABI and contract address.
        """
        if not os.path.exists(self.abi_path):
            messagebox.showerror("Error", f"ABI file not found at {self.abi_path}. Ensure the file exists.")
            self.quit()

        # Load the ABI from the JSON file
        with open(self.abi_path, 'r') as abi_file:
            contract_abi = json.load(abi_file)['abi']

        # Initialize the contract
        return self.w3.eth.contract(address=self.contract_address, abi=contract_abi)

    def fetch_transactions(self):
        """
        Fetches transaction logs from the blockchain.
        """
        try:
            logs = self.contract.functions.getAuditLogs().call()
            print("log")
            print(logs)
            transactions = [
                {
                    "actor": log[0],
                    "subject": log[1],
                    "action": log[2],
                    "timestamp": log[3]
                } for log in logs
            ]
            return transactions
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch transactions: {str(e)}")
            return []

    def view_transaction(self):
        """
        Displays transaction logs in the GUI.
        """
        # Clear previous content
        for widget in self.main_content1.winfo_children():
            widget.destroy()

        # Title Label
        title_label = ctk.CTkLabel(
            self.main_content1,
            text="Transaction Logs",
            font=("Arial", 30, "bold"),
            fg_color="#E1EBEE",
            text_color="black",
            corner_radius=10
        )
        title_label.grid(row=0, column=0, columnspan=4, padx=(20, 20), pady=(20, 20), sticky="w")

        # Headers
        headers = ["Actor", "Subject", "Action", "Timestamp"]
        for col, header in enumerate(headers):
            header_label = ctk.CTkLabel(
                self.main_content1,
                text=header,
                font=("Arial", 16, "bold"),
                text_color="black"
            )
            header_label.grid(row=1, column=col, padx=(10, 10), pady=(10), sticky="w")

        # Fetch transactions from the smart contract
        transactions = self.fetch_transactions()

        # Display transactions
        for idx, tx in enumerate(transactions):
            actor_value = ctk.CTkLabel(
                self.main_content1,
                text=tx["actor"],
                font=("Arial", 14),
                text_color="black"
            )
            actor_value.grid(row=2 + idx, column=0, padx=(10, 10), pady=(5), sticky="w")

            subject_value = ctk.CTkLabel(
                self.main_content1,
                text=tx["subject"],
                font=("Arial", 14),
                text_color="black"
            )
            subject_value.grid(row=2 + idx, column=1, padx=(10, 10), pady=(5), sticky="w")

            action_value = ctk.CTkLabel(
                self.main_content1,
                text=tx["action"],
                font=("Arial", 14),
                text_color="black"
            )
            action_value.grid(row=2 + idx, column=2, padx=(10, 10), pady=(5), sticky="w")

            timestamp_value = ctk.CTkLabel(
                self.main_content1,
                text=datetime.datetime.fromtimestamp(tx["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'),
                font=("Arial", 14),
                text_color="black"
            )
            timestamp_value.grid(row=2 + idx, column=3, padx=(10, 10), pady=(5), sticky="w")

# Run the application
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = TransactionViewer()
    app.mainloop()
