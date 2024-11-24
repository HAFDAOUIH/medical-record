// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./IPatientRecords.sol";

contract DoctorContract {
    using IPatientRecords for IPatientRecords.Doctor;

    mapping(address => IPatientRecords.Doctor) public doctors;
    address public auditContractAddress;

    event DoctorRegistered(address indexed doctorAddress, string name);
    event DoctorUpdated(address indexed doctorAddress);

    constructor(address _auditContractAddress) {
        auditContractAddress = _auditContractAddress;
    }

    modifier onlyRegisteredDoctor() {
        require(doctors[msg.sender].isRegistered, "Not a registered doctor");
        _;
    }

    function registerDoctor(
        string memory _name,
        string memory _speciality,
        string memory _encryptionKey
    ) public {
        require(!doctors[msg.sender].isRegistered, "Doctor already registered");

        doctors[msg.sender] = IPatientRecords.Doctor({
            isRegistered: true,
            name: _name,
            speciality: _speciality,
            encryptionKey: _encryptionKey
        });

        emit DoctorRegistered(msg.sender, _name);
    }

    function updateDoctorInfo(
        string memory _name,
        string memory _speciality,
        string memory _encryptionKey
    ) public onlyRegisteredDoctor {
        IPatientRecords.Doctor storage doctor = doctors[msg.sender];
        doctor.name = _name;
        doctor.speciality = _speciality;
        doctor.encryptionKey = _encryptionKey;

        emit DoctorUpdated(msg.sender);
    }

    function isDoctorRegistered(address doctorAddress) public view returns (bool) {
        return doctors[doctorAddress].isRegistered;
    }

    function getDoctorInfo(address doctorAddress)
    public
    view
    returns (string memory name, string memory speciality)
    {
        require(doctors[doctorAddress].isRegistered, "Doctor not registered");
        IPatientRecords.Doctor storage doctor = doctors[doctorAddress];
        return (doctor.name, doctor.speciality);
    }
}
