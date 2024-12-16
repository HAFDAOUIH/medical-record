// SPDX-License-Identifier: MIT

pragma solidity ^0.8.19;

import "./IPatientRecords.sol";

contract DoctorContract {
    using IPatientRecords for IPatientRecords.Doctor;

    mapping(string => IPatientRecords.Doctor) public doctors;
    address public auditContractAddress;

    event DoctorRegistered(address indexed doctorAddress, string name);
    event DoctorUpdated(address indexed doctorAddress);

    constructor(address _auditContractAddress) {
        auditContractAddress = _auditContractAddress;
    }

    modifier onlyRegisteredDoctor(string memory _walletAddress) {
        require(doctors[_walletAddress].isRegistered, "Not a registered doctor");
        _;
    }

    function registerDoctor(
        string memory _name,
        string memory _speciality,
        string memory _licenseNumber,
        string memory _contactInfo,
        string memory _password,
        string memory _walletAddress
       
    ) public {
        require(!doctors[_walletAddress].isRegistered, "Doctor already registered");

        doctors[_walletAddress] = IPatientRecords.Doctor({
            isRegistered: true,
            name: _name,
            speciality: _speciality,
            licenseNumber: _licenseNumber,
            contactInfo: _contactInfo,
            password: _password,
            walletAddress : _walletAddress
           
        });

        emit DoctorRegistered(msg.sender, _name);
    }

    function updateDoctorInfo(
        string memory _name,
        string memory _speciality,
        string memory _licenseNumber,
        string memory _contactInfo,
        string memory _walletAddress
        
    ) public onlyRegisteredDoctor(_walletAddress) {
        IPatientRecords.Doctor storage doctor = doctors[_walletAddress];
        doctor.name = _name;
        doctor.speciality = _speciality;
        doctor.licenseNumber = _licenseNumber;
        doctor.contactInfo = _contactInfo;
        

        emit DoctorUpdated(msg.sender);
    }

    function isDoctorRegistered(string memory _walletAddress) public view returns (bool) {
        return doctors[_walletAddress].isRegistered;
    }

    function getDoctorInfo(string memory _walletAddress)
    public
    view
    returns (string memory name, string memory speciality, string memory licenseNumber, string memory contactInfo,string memory password)
    {
        
        IPatientRecords.Doctor storage doctor = doctors[_walletAddress];
        require(doctor.isRegistered, "Doctor not registered");
        return (doctor.name, doctor.speciality, doctor.licenseNumber, doctor.contactInfo,doctor.password);
    }
}
