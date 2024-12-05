// SPDX-License-Identifier: MIT

pragma solidity ^0.8.19;

import "./IPatientRecords.sol";
import "./DoctorContract.sol";

contract PatientContract {
    using IPatientRecords for IPatientRecords.Patient;

    struct ExtendedMedicalRecord {
        string ipfsHash;
        string encryptedData;
        uint256 timestamp;
        address doctor;
    }

    mapping(address => IPatientRecords.Patient) public patients;
    mapping(address => mapping(string => ExtendedMedicalRecord)) public patientRecords;
    DoctorContract public doctorContract;
    address public auditContractAddress;

    event PatientRegistered(address indexed patientAddress);
    event RecordAdded(address indexed patient, string ipfsHash, address indexed doctor);
    event AccessGranted(address indexed patient, address indexed doctor);
    event AccessRevoked(address indexed patient, address indexed doctor);

    constructor(address _doctorContractAddress, address _auditContractAddress) {
        doctorContract = DoctorContract(_doctorContractAddress);
        auditContractAddress = _auditContractAddress;
    }

    modifier onlyRegisteredPatient() {
        require(patients[msg.sender].isRegistered, "Not a registered patient");
        _;
    }

    modifier onlyAuthorizedDoctor(address patientAddress) {
        require(doctorContract.isDoctorRegistered(msg.sender), "Not a registered doctor");
        require(patients[patientAddress].authorizedDoctors[msg.sender], "Not authorized for this patient");
        _;
    }

    function registerPatient(string memory _encryptionKey) public {
        require(!patients[msg.sender].isRegistered, "Patient already registered");

        IPatientRecords.Patient storage newPatient = patients[msg.sender];
        newPatient.isRegistered = true;
        newPatient.encryptionKey = _encryptionKey;

        emit PatientRegistered(msg.sender);
    }

    function grantAccess(address doctorAddress) public onlyRegisteredPatient {
        require(doctorContract.isDoctorRegistered(doctorAddress), "Doctor not registered");
        patients[msg.sender].authorizedDoctors[doctorAddress] = true;
        emit AccessGranted(msg.sender, doctorAddress);
    }

    function revokeAccess(address doctorAddress) public onlyRegisteredPatient {
        patients[msg.sender].authorizedDoctors[doctorAddress] = false;
        emit AccessRevoked(msg.sender, doctorAddress);
    }

    function addMedicalRecord(
        address patientAddress,
        string memory ipfsHash,
        string memory encryptedData
    ) public onlyAuthorizedDoctor(patientAddress) {
        // Store the record hash in the patient's array
        patients[patientAddress].recordHashes.push(ipfsHash);

        // Store the extended record information
        patientRecords[patientAddress][ipfsHash] = ExtendedMedicalRecord({
            ipfsHash: ipfsHash,
            encryptedData: encryptedData,
            timestamp: block.timestamp,
            doctor: msg.sender
        });

        emit RecordAdded(patientAddress, ipfsHash, msg.sender);
    }

    function getPatientRecords(address patientAddress)
    public
    view
    returns (string[] memory)
    {
        require(
            msg.sender == patientAddress ||
            patients[patientAddress].authorizedDoctors[msg.sender],
            "Not authorized to view records"
        );
        return patients[patientAddress].recordHashes;
    }

    function getMedicalRecordDetails(
        address patientAddress,
        string memory ipfsHash
    )
    public
    view
    returns (ExtendedMedicalRecord memory)
    {
        require(
            msg.sender == patientAddress ||
            patients[patientAddress].authorizedDoctors[msg.sender],
            "Not authorized to view record details"
        );
        return patientRecords[patientAddress][ipfsHash];
    }

    function getPatientEncryptionKey(address patientAddress)
    public
    view
    returns (string memory)
    {
        require(
            msg.sender == patientAddress ||
            patients[patientAddress].authorizedDoctors[msg.sender],
            "Not authorized to view encryption key"
        );
        return patients[patientAddress].encryptionKey;
    }
}
