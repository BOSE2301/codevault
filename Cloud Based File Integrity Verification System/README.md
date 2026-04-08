
---

# 📁 File Integrity Verification Using AWS S3 & Blockchain

## 🚀 Project Overview

This project demonstrates how to verify the integrity of files using a hybrid solution involving **AWS S3** for cloud storage and **Blockchain** for tamper-proof hash storage. The system ensures that a file, once uploaded to S3, can be validated against its cryptographic hash stored on the blockchain, preventing unauthorized modifications.

---

## 🛠️ Technologies Used

* **Python**
* **Boto3** (AWS SDK for Python)
* **Web3.py** (Ethereum blockchain interface)
* **AWS S3** (Cloud storage)
* **Ganache** (Local blockchain network)
* **Remix IDE** (Smart contract development and deployment)

---

## 🧩 Project Structure

```
📦 file-integrity-verification/
├── upload_to_s3.py       # Uploads files to AWS S3
├── add_hash.py           # Generates SHA-256 hash of a file
├── blockchain.py         # Interacts with Ethereum blockchain to store hash
├── view.py               # Retrieves and verifies hash from the blockchain
├── save_hash.py          # Uploads hash file to S3
├── Solidity
│   └── testproject.sol   # Solidity smart contract
├── weather.csv           # sample dataset
└── README.md             # Project documentation
```

---

## 📌 Objectives

* Secure file storage using AWS S3
* Immutable file integrity verification via blockchain
* Automated hash generation and comparison
* Seamless integration of all components

---

## 🧪 Development Sessions

### ✅ **Session 1: Development Phase 1**

**Goal:** Set up the project and begin core implementation.

* Install dependencies: `boto3`, `web3`, `ganache-cli`, `py-solc-x`
* Configure AWS CLI and S3 bucket
* Implement:

  * `upload_to_s3.py`: Upload CSV file (e.g., `weather.csv`)
  * `add_hash.py`: Generate SHA-256 hash of uploaded file

---

### ✅ **Session 2: Development Phase 2**

**Goal:** Implement blockchain components.

* Deploy `testproject.sol` smart contract on Ganache via Remix IDE
* Record the deployed contract address
* Implement:

  * `blockchain.py`: Send file hash to the blockchain
  * `view.py`: Retrieve and verify file hash from blockchain

---

### ✅ **Session 3: Final Testing and Integration**

**Goal:** Perform integration testing and begin documentation.

* Test full workflow:

  1. Upload file to S3
  2. Generate hash
  3. Store hash on blockchain
  4. Retrieve and verify hash
  5. Save hash to S3 (`save_hash.py`)
* Start final report:

  * Introduction
  * Problem formulation
  * Methodology & implementation
  * Results & screenshots
* Prepare:

  * Architecture diagrams
  * System flowcharts

---

### ✅ **Session 4: Final Review and Submission**

**Goal:** Finalize and submit the project.

* Review and comment all code
* Polish report and add visuals
* Create presentation slides (if required)
* Ensure all deliverables are complete and well-formatted

---

