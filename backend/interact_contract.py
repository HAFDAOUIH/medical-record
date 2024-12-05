from web3 import Web3
import json

# Connect to local Ganache
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Check if connected
if web3.is_connected():
    print("Connected to Ganache!")

# Load the ABI from the generated JSON file
with open('build/contracts/AuditContract.json', 'r') as abi_file:
    audit_abi = json.load(abi_file)['abi']

# Set contract address (from deployment output)
audit_address = '0x34052a6d033482Edd7C35ef728ee2A8f36ee2B4f'  # AuditContract address

# Create contract instance
audit_contract = web3.eth.contract(address=audit_address, abi=audit_abi)

# Get the admin address (first account from Ganache)
admin_address = web3.eth.accounts[0]
print(f"Admin Address: {admin_address}")

# Authorize the contract (replace with the contract address calling logAction)
contract_address_to_authorize = '0x34052a6d033482Edd7C35ef728ee2A8f36ee2B4f'  # DoctorContract address

tx_hash = audit_contract.functions.logAction(
    web3.eth.accounts[0],  # Actor address
    web3.eth.accounts[1],  # Subject address
    "Test Action"
).transact({
    'from': web3.eth.accounts[0],
    'gas': 5000000  # Increase gas limit if needed
})


# Wait for transaction receipt
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction Receipt: ", receipt)
