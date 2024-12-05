// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

library IPatientRecords {
    struct Patient {
        bool isRegistered;
        string[] recordHashes;
        mapping(address => bool) authorizedDoctors;
        string encryptionKey;
    }

    struct Doctor {
        bool isRegistered;
        string name;
        string speciality;
        string encryptionKey;
    }

    struct MedicalRecord {
        string ipfsHash;
        uint256 timestamp;
        address creator;
        string encryptedData;
    }
}
