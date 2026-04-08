import boto3
import os
from botocore.exceptions import NoCredentialsError
from web3 import Web3

# AWS S3 bucket name
BUCKET_NAME = 'sandipproject'
FILE_NAME = 'file_hash.txt'

def save_to_s3(data, bucket_name, file_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=data)
        print(f'Successfully uploaded {file_name} to {bucket_name}')
    except NoCredentialsError:
        print('Credentials not available')
    except Exception as e:
        print(f"Error uploading to S3: {e}")

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Check if connected to the provider
if not w3.is_connected():
    print("Failed to connect to the Ethereum network")
    exit(1)

# Contract ABI and address
contract_address = '0xdaeb7e5d590ce1987fbc53c90db70706144e2ebe'
contract_address = Web3.to_checksum_address(contract_address)

contract_abi = [
    {
        "inputs": [],
        "name": "getFileHash",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
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
        return file_hash
    except Exception as e:
        print(f"Error retrieving hash: {e}")
        return None

if __name__ == "__main__":
    file_hash = get_file_hash()
    if file_hash:
        save_to_s3(file_hash, BUCKET_NAME, FILE_NAME)
