// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract AuditContract {
    struct AuditLog {
        address actor;
        address subject;
        string action;
        uint256 timestamp;
    }

    AuditLog[] public auditLogs;
    mapping(address => bool) public authorizedContracts;
    address public admin;

    event LogAdded(address indexed actor, address indexed subject, string action);
    event ContractAuthorized(address indexed contractAddress);

    modifier onlyAdmin() {
        require(msg.sender == admin, "Error: Only admin can perform this action");
        _;
    }

    modifier onlyAuthorized() {
        require(authorizedContracts[msg.sender], "Error: Not authorized to log this action");
        _;
    }

    // Explicit constructor with validation
    constructor() {
        admin = msg.sender;  // Set the admin to the deployer's address
        require(admin != address(0), "Error: Invalid admin address");  // Ensure valid admin address
    }

    function authorizeContract(address contractAddress) public onlyAdmin {
        require(contractAddress != address(0), "Error: Invalid contract address");
        authorizedContracts[contractAddress] = true;
        emit ContractAuthorized(contractAddress);
    }

    function logAction(
        address actor,
        address subject,
        string memory action
    ) public onlyAuthorized {
        require(actor != address(0), "Error: Invalid actor address");
        require(subject != address(0), "Error: Invalid subject address");
        require(bytes(action).length > 0, "Error: Action cannot be empty");

        auditLogs.push(AuditLog({
            actor: actor,
            subject: subject,
            action: action,
            timestamp: block.timestamp
        }));
        emit LogAdded(actor, subject, action);
    }

    function getAuditLogs() public view returns (AuditLog[] memory) {
        return auditLogs;
    }
}
