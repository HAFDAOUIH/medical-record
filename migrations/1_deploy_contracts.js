const AdminContract = artifacts.require("AdminContract");
const AuditContract = artifacts.require("AuditContract");
const DoctorContract = artifacts.require("DoctorContract");
const PatientContract = artifacts.require("PatientContract");

module.exports = function (deployer) {
  // Deploy the AuditContract
  deployer.deploy(AuditContract, {
    gas: 6721975, // Increase the gas limit if needed
    gasPrice: 20000000000, // Increase gas price if needed
  })
  .then(() => {
    // Deploy the AdminContract after AuditContract
    return deployer.deploy(AdminContract);
  })
  .then(() => {
    // Deploy the DoctorContract, passing the AuditContract address
    return deployer.deploy(DoctorContract, AuditContract.address);
  })
  .then(() => {
    // Deploy the PatientContract, passing the DoctorContract and AuditContract addresses
    return deployer.deploy(PatientContract, DoctorContract.address, AuditContract.address);
  });
};
