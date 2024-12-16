// SPDX-License-Identifier: MIT

pragma solidity ^0.8.19;

import "./IPatientRecords.sol";
import "./DoctorContract.sol";

contract PatientContract {
    using IPatientRecords for IPatientRecords.Patient;

    mapping(string => IPatientRecords.Patient) public patients;

    DoctorContract public doctorContract;
    address public auditContractAddress;

    event PatientRegistered(address indexed patientAddress);
    event RecordAdded(address indexed patient, string ipfsHash);
    event AccessGranted(address indexed patient, string doctor);
    event AccessRevoked(address indexed patient, string doctor);
    
    constructor(address _doctorContractAddress, address _auditContractAddress) {
        doctorContract = DoctorContract(_doctorContractAddress);
        auditContractAddress = _auditContractAddress;
    }

    modifier onlyRegisteredPatient(string memory _patientAddress) {
        require(patients[_patientAddress].isRegistered, "Not a registered patient");
        _;
    }

    modifier onlyAuthorizedDoctor(string memory _patientAddress, string memory _walletAddress) {
        require(doctorContract.isDoctorRegistered(_walletAddress), "Not a registered doctor");
        require(patients[_patientAddress].authorizedDoctors[_walletAddress], "Not authorized for this patient");
        _;
    }

    function registerPatient(
        string memory _fullName,
        string memory _gender,
        uint _age,
        uint _weight,
        uint _height,
        string memory _bloodType,
        string memory _allergies,
        string memory _patientAddress,
        string memory _password,
        string memory _encryptionKey
    ) public {
        require(!patients[_patientAddress].isRegistered, "Patient already registered");

        patients[_patientAddress].isRegistered = true;
        patients[_patientAddress].fullName = _fullName;
        patients[_patientAddress].gender = _gender;
        patients[_patientAddress].age = _age;
        patients[_patientAddress].weight = _weight;
        patients[_patientAddress].height = _height;
        patients[_patientAddress].bloodType = _bloodType;
        patients[_patientAddress].allergies = _allergies;
        patients[_patientAddress].walletAddress = _patientAddress;
        patients[_patientAddress].password = _password;
        patients[_patientAddress].encryptionKey = _encryptionKey;

        emit PatientRegistered(msg.sender);
    }

    function grantAccess(string memory _walletAddress,string memory _patientAddress) public onlyRegisteredPatient(_patientAddress) {
        require(doctorContract.isDoctorRegistered(_walletAddress), "Doctor not registered");
        patients[_patientAddress].authorizedDoctors[_walletAddress] = true;
        emit AccessGranted(msg.sender , _walletAddress);
    }

    function revokeAccess(string memory _walletAddress,string memory _patientAddress) public onlyRegisteredPatient(_patientAddress) {
        patients[_patientAddress].authorizedDoctors[_walletAddress] = false;
        emit AccessRevoked(msg.sender , _walletAddress);
    }


    

   function getPatientInfo(string memory _patientAddress)
    public
    view
    returns (
        string memory fullName,
        string memory gender,
        uint age,
        uint weight,
        uint height,
        string memory bloodType,
        string memory allergies,
        string memory password
    )
    {
    IPatientRecords.Patient storage patient = patients[_patientAddress];
    require(patient.isRegistered, "Patient not registered");
    return (
        patient.fullName,
        patient.gender,
        patient.age,
        patient.weight,
        patient.height,
        patient.bloodType,
        patient.allergies,
        patient.password
    );
    }

    function updatePatientDetails(
        string memory _fullName,
        string memory _gender,
        uint _age,
        uint _weight,
        uint _height,
        string memory _bloodType,
        string memory _allergies,
        string memory _patientAddress
    ) public onlyRegisteredPatient(_patientAddress){
       IPatientRecords.Patient storage patient = patients[_patientAddress];
        patient.fullName = _fullName;
        patient.gender = _gender;
        patient.age = _age;
        patient.weight = _weight;
        patient.height = _height;
        patient.bloodType = _bloodType;
        patient.allergies = _allergies;
        
    }
    

    function addMedicalRecord(
        string memory _patientAddress,
        string memory _ipfsHash
    ) public {
        IPatientRecords.Patient storage patient = patients[_patientAddress];
        require(
            patient.isRegistered,
            "Not authorized to add medical record"
        );
        
        
        patient.recordHashes.push(_ipfsHash);

        emit RecordAdded(msg.sender, _ipfsHash);
    }
    
    function getPatientRecords(string memory _patientAddress) 
    public 
    view 
    returns (string[] memory) 
    {
        IPatientRecords.Patient storage patient = patients[_patientAddress];
         require(
            patient.isRegistered,
            "Not authorized to add medical record"
        );
        
        
        return patient.recordHashes;
    }


}


