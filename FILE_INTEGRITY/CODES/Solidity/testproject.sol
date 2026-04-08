// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FileIntegrity {
    string public fileHash;

    // Event to emit when a hash is stored
    event HashStored(string indexed hash);

    // Store the file hash
    function storeFileHash(string memory hash) public {
        fileHash = hash;
        emit HashStored(hash); // Emit an event for the stored hash
    }

    // Retrieve the file hash
    function getFileHash() public view returns (string memory) {
        return fileHash;
    }
}
