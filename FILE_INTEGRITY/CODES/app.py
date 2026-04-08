from flask import Flask, jsonify, render_template
import subprocess
import sys
from web3 import Web3

app = Flask(__name__)

# Function to run scripts
def run_script(script_name):
    try:
        subprocess.run([sys.executable, script_name], check=True)
        return {"status": "success"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}

# Function to get hash from blockchain
def get_file_hash():
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
    if not w3.is_connected():
        return {"status": "error", "message": "Failed to connect to the Ethereum network"}

    contract_address = Web3.to_checksum_address('0xdaeb7e5d590ce1987fbc53c90db70706144e2ebe')
    contract_abi = [
        {
            "inputs": [],
            "name": "getFileHash",
            "outputs": [{"internalType": "string", "name": "", "type": "string"}],
            "stateMutability": "view",
            "type": "function"
        }
    ]
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    try:
        file_hash = contract.functions.getFileHash().call()
        return {"status": "success", "file_hash": file_hash}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Default route
@app.route('/')
def home():
    return "Welcome to the File Integrity Management System project By Sandip Bhattacharya"

# Route to upload file to S3
@app.route('/upload', methods=['POST'])
def upload():
    result = run_script('upload_to_s3.py')
    return jsonify(result)

# Route to generate file hash
@app.route('/generate-hash', methods=['POST'])
def generate_hash():
    result = run_script('add_hash.py')
    return jsonify(result)

# Route to store hash on blockchain
@app.route('/store-hash', methods=['POST'])
def store_hash():
    result = run_script('blockchain.py')
    return jsonify(result)

# Route to save hash to S3
@app.route('/save-hash', methods=['POST'])
def save_hash():
    result = run_script('save_hash_s3.py')
    return jsonify(result)

# Route to retrieve hash from blockchain
@app.route('/retrieve-hash', methods=['GET'])
def retrieve_hash():
    result = get_file_hash()
    if result["status"] == "success":
        file_hash = result["file_hash"]
    else:
        file_hash = "Error retrieving hash"
    return render_template('hash_display.html', file_hash=file_hash)

# New route for running the full process
@app.route('/full-process', methods=['POST'])
def full_process():
    steps = [
        ('upload_to_s3.py', 'Uploading file to S3...'),
        ('add_hash.py', 'Generating file hash...'),
        ('blockchain.py', 'Storing file hash on blockchain...'),
        ('save_hash_s3.py', 'Saving hash to S3...'),
        ('view.py', 'Retrieving file hash from blockchain...')
    ]
    
    for script, message in steps:
        print(message)
        result = run_script(script)
        if result["status"] == "error":
            return jsonify(result)
    
    return jsonify({"status": "success", "message": "All operations completed successfully!"})

if __name__ == '__main__':
    app.run(debug=True)