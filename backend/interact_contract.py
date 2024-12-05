from web3 import Web3
import json

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Ensure connection is successful
if web3.is_connected():
    print("Connected to Ganache!")

# Load the contract ABI (from the build folder)
with open('build/contracts/AuditContract.json', 'r') as abi_file:
    audit_abi = json.load(abi_file)['abi']

# Set the contract address (from deployment output)
audit_address = '0x5a6d9a6E8F327fB7F52aef83055792893702D42F'

# Create the contract instance
audit_contract = web3.eth.contract(address=audit_address, abi=audit_abi)

# First, ensure the account is authorized by calling authorizeContract
# Authorize the account (web3.eth.accounts[0]) to log actions
tx_hash = audit_contract.functions.authorizeContract(web3.eth.accounts[0]).transact({'from': web3.eth.accounts[0]})

# Wait for the transaction receipt
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print("Authorization Transaction receipt:", receipt)

# Now, you can call the logAction function
tx_hash = audit_contract.functions.logAction(
    web3.eth.accounts[0],  # Actor address
    web3.eth.accounts[1],  # Subject address
    "Action Example"
).transact({'from': web3.eth.accounts[0]})

# Wait for transaction receipt
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction receipt:", receipt)
