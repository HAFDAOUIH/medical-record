// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;


contract AdminContract {

    // Admin Struct
    struct Admin {
        bool isRegistered;
        string name;
        string walletAddress;  // The wallet address of the admin (string)
        string hashPassword;
    }

    // Mapping to store admin data, using walletAddress (string) as the key
    mapping(string => Admin) public admins; // Map walletAddress (string) to Admin struct

    // Events
    event AdminAdded(string indexed walletAddress, string name);
    event AdminUpdated(string indexed walletAddress);

    // Modifier to check if the sender is a registered admin
    modifier onlyAdmin(string memory _walletAddress) {
        require(admins[_walletAddress].isRegistered, "Not a registered admin");
        _;
    }

    // Function to add a new admin, using walletAddress as the key
    function addAdmin(
        string memory _name,
        string memory _walletAddress,  // Wallet address (string)
        string memory _hashPassword
    ) public {
        require(!admins[_walletAddress].isRegistered, "Admin already registered");

        Admin memory newAdmin = Admin({
            isRegistered: true,
            name: _name,
            walletAddress: _walletAddress,
            hashPassword: _hashPassword
        });

        admins[_walletAddress] = newAdmin;  // Store the admin using walletAddress as the key

        emit AdminAdded(_walletAddress, _name);
    }

    // Function to update existing admin information, by walletAddress (string)
    function updateAdmin(
        string memory _walletAddress,  // Wallet address (string)
        string memory _name,
        string memory _hashPassword
    ) public onlyAdmin(_walletAddress) {
       
        Admin storage admin = admins[_walletAddress];
        
        // Ensure the admin exists before updating
        require(admin.isRegistered, "Admin with this wallet address not found");

        // Update admin details
        admin.name = _name;
        admin.hashPassword = _hashPassword;

        // Emit the update event
        emit AdminUpdated(_walletAddress);
    }

    // Function to retrieve admin information by walletAddress (string)
    function getAdminInfoByWallet(string memory _walletAddress)
        public
        view
        returns (
            string memory name,
            string memory walletAddress,
            string memory hashPassword
        )
    {
        Admin storage admin = admins[_walletAddress];
        require(admin.isRegistered, "Admin with this wallet address not found");

        return (admin.name, admin.walletAddress, admin.hashPassword);
    }

    // Function to check if an admin is registered
    function isAdminRegistered(string memory _walletAddress) public view returns (bool) {
        return admins[_walletAddress].isRegistered;
    }
}
