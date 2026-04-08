from web3 import Web3
import sys

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Check if connected to the provider
if not w3.is_connected():
    print("Failed to connect to the Ethereum network")
    sys.exit(1)

# Contract ABI and address
contract_address = '0xdaeb7e5d590ce1987fbc53c90db70706144e2ebe'
contract_address = Web3.to_checksum_address(contract_address)  # Convert to checksum address

contract_abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "string",
                "name": "hash",
                "type": "string"
            }
        ],
        "name": "HashStored",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "hash",
                "type": "string"
            }
        ],
        "name": "storeFileHash",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "fileHash",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getFileHash",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# private key
private_key = '0xc28ba76cf2f6c13ea006eb601dc70bdd0fc463556fa29330293c31b0fe784632'

# Create the contract object
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def set_file_hash(file_hash):
    # Generate account from private key
    account = w3.eth.account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(account.address)

    # Build transaction with reasonable gas limit
    transaction = contract.functions.storeFileHash(file_hash).build_transaction({
        'chainId': 1337,
        'gas': 100000,
        'gasPrice': w3.to_wei('1', 'gwei'),
        'nonce': nonce,
    })

    try:
        # Sign the transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

        # Send the transaction
        txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f'Transaction hash: {w3.to_hex(txn_hash)}')

        # Wait for the transaction to be mined
        receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
        print(f'Transaction receipt: {receipt}')

    except Exception as e:
        print(f"Error sending transaction: {e}")

def main():
    # Use the generated hash directly
    generated_hash = "4e6170d41857c83c77d5906fe6c3c5bdb9192b295fff90ddcf1f0d0175e0d5fd"
    set_file_hash(generated_hash)

if __name__ == "__main__":
    main()
