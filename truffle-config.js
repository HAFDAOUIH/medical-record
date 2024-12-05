const HDWalletProvider = require('@truffle/hdwallet-provider');

module.exports = {
  networks: {
    // Local Ganache network
    development: {
      host: "127.0.0.1",      // Localhost (Ganache runs on localhost)
      port: 7545,             // Ganache's default port
      network_id: "*",        // Match any network id (use "*" to connect to any network)
      gas: 6721975,           // Gas limit for deploying contracts
      gasPrice: 20000000000   // Gas price in wei (20 gwei)
    }
  },

  compilers: {
    solc: {
      version: "0.8.21",      // Solidity version for compiling contracts
    }
  }
};
