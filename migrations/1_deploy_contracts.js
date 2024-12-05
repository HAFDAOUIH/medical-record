const AuditContract = artifacts.require("AuditContract");
const DoctorContract = artifacts.require("DoctorContract");
const PatientContract = artifacts.require("PatientContract");

module.exports = function (deployer) {
    deployer.deploy(AuditContract, {
      gas: 6721975, // you can increase the gas here if needed
      gasPrice: 20000000000, // Increase gas price if needed
    }).then(() => {
      return deployer.deploy(DoctorContract, AuditContract.address);
    }).then(() => {
      return deployer.deploy(PatientContract, DoctorContract.address, AuditContract.address);
    });
  };
  