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
contract_address = Web3.to_checksum_address(contract_address)

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

# Create the contract object
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def get_file_hash():
    try:
        file_hash = contract.functions.getFileHash().call()
        print(f'File hash from blockchain: {file_hash}')
    except Exception as e:
        print(f"Error retrieving hash: {e}")

if __name__ == "__main__":
    get_file_hash()
