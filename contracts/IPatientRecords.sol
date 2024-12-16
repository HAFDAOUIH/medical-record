// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

library IPatientRecords {
    struct Patient {
        bool isRegistered;
        string[] recordHashes;
        mapping(string => bool) authorizedDoctors;
        string encryptionKey;
        string fullName;
        string gender;
        uint age;
        uint weight;
        uint height;
        string bloodType;
        string allergies;
        string walletAddress;
        string password;
    }

    struct Doctor {
        bool isRegistered;
        string name;
        string speciality;
        string licenseNumber;
        string contactInfo;
        string walletAddress; 
        string password;
    }

    struct Admin {
        bool isRegistered;
        string name;
        address walletAddress;
        string hashPassword;
    }

    struct MedicalRecord {
        string ipfsHash;
        uint256 timestamp;
        address creator;
        string encryptedData;
    }

    
}
