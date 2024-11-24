// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

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
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier onlyAuthorized() {
        require(authorizedContracts[msg.sender], "Not authorized to log");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function authorizeContract(address contractAddress) public onlyAdmin {
        authorizedContracts[contractAddress] = true;
        emit ContractAuthorized(contractAddress);
    }

    function logAction(
        address actor,
        address subject,
        string memory action
    ) public onlyAuthorized {
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