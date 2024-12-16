const HDWalletProvider = require('@truffle/hdwallet-provider');

module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",    // Ganache runs on localhost
      port: 8545,           // Ganache's default RPC server port
      network_id: "*",    // Network ID for Ganache
      gas: 6721975,          // Gas limit for deploying contracts (same as in Ganache)
      gasPrice: 20000000000, // Gas price in wei (20 gwei) from: "0x50E673c2478bfd59579AE0EFC3B17FF370D67f98", // (Optional) Make sure this is set to the address you want to deploy from.
    },
  },

  compilers: {
    solc: {
      version: "0.8.19",     // Ensure this matches your contract's Solidity version
    },
  },
};
