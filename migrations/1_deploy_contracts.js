const AuditContract = artifacts.require("AuditContract");
const DoctorContract = artifacts.require("DoctorContract");
const PatientContract = artifacts.require("PatientContract");

module.exports = function (deployer) {
    deployer.deploy(AuditContract).then(() => {
        return deployer.deploy(DoctorContract, AuditContract.address);
    }).then(() => {
        return deployer.deploy(PatientContract, DoctorContract.address, AuditContract.address);
    });
};
