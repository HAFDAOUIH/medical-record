
## Project Title  
**Decentralized Medical Record Management Using Blockchain Technology**

## Overview  
This project is a decentralized application (DApp) designed for secure and efficient medical record management using **Ethereum blockchain** and **InterPlanetary File System (IPFS)**. By leveraging **smart contracts** built with Solidity and a Python-based graphical user interface, the system ensures **confidentiality**, **integrity**, **traceability**, and **access control** of medical records while decentralizing healthcare management.

The project eliminates reliance on centralized servers, enhancing security, transparency, and resilience against cyberattacks. Patients have complete control over their medical data, granting and revoking access to doctors securely.

---

## Key Features  

1. **Role-Based Access Control**  
   - Admin, Doctor, and Patient functionalities with dedicated interfaces.  
   - Patients can manage their records, while doctors are authorized to view only with patient consent.  

2. **Medical Record Management**  
   - Upload medical records securely to **IPFS** (InterPlanetary File System).  
   - Store IPFS hashes on the Ethereum blockchain for immutability and verification.  

3. **Smart Contracts**  
   - Developed in Solidity for Ethereum. Contracts handle:  
     - Patient registration and profile management.  
     - Doctor registration and access permissions.  
     - Audit logging for system transparency.  

4. **Graphical User Interface**  
   - Python-based GUI using `customtkinter` for role-specific functionalities:  
     - Admin Panel for managing doctors and patients.  
     - Doctor Panel for viewing patient records.  
     - Patient Panel for uploading records, managing access, and updating profiles.

5. **Decentralized Storage**  
   - Medical records are stored on IPFS, ensuring no single point of failure.  
   - Blockchain transactions log IPFS file hashes for security and integrity.  

6. **Security & Privacy**  
   - Blockchain immutability ensures records cannot be altered.  
   - Access to records is controlled using cryptographic permissions.

---

## System Architecture  

The architecture consists of:  

- **Frontend**: Python-based GUI (`customtkinter`) for multi-role access.  
- **Backend**: Web3.py for Ethereum smart contract integration.  
- **Storage**: IPFS for decentralized storage of medical records.  
- **Blockchain**: Ganache for local Ethereum blockchain deployment.  

---

## Components  

1. **Smart Contracts**  
   - **PatientContract**: Handles patient registration, medical record storage, and access control.  
   - **DoctorContract**: Manages doctor registration and permissions.  
   - **AuditContract**: Logs all interactions for traceability.  

2. **Frontend (Python)**  
   - Interfaces for Admin, Doctor, and Patient roles.  
   - Functionalities include:  
     - Registering users.  
     - Uploading and viewing records.  
     - Granting and revoking access.  
     - Audit log display.  

3. **IPFS Integration**  
   - Records are uploaded to IPFS, and the resulting file hashes are stored on the blockchain for verification.  

4. **Blockchain Interaction**  
   - Smart contracts deployed locally on Ganache.  
   - Web3.py facilitates communication between the Python GUI and Ethereum blockchain.  

---

## Functionalities  

### **Admin Role**  
- Register doctors and patients.  
- Manage user roles and permissions.  
- View all transactions.  

### **Doctor Role**  
- View patient records only with granted access.  

### **Patient Role**  
- Register and update profiles.  
- Upload medical records to IPFS.  
- Grant or revoke access to doctors.  

---

## Installation  

### Prerequisites  
- Node.js and npm  
- Python 3.x  
- Ganache (Ethereum local blockchain)  
- Truffle (for deploying smart contracts)  
- IPFS local node  

### Steps  

1. **Clone the Repository**  
   ```  
   git clone https://github.com/HAFDAOUIH/medical-record.git  
   cd medical-record  
   ```  

2. **Install Dependencies**  
   - **Backend**:  
     ```  
     npm install -g truffle  
     truffle compile  
     truffle migrate  
     ```  
   - **Frontend**:  
     Install required Python libraries:  
     ```  
     pip install web3 customtkinter ipfshttpclient  
     ```  

3. **Run Ganache**  
   Start a local blockchain instance using Ganache.  

4. **Start IPFS Node**  
   Run the IPFS daemon:  
   ```  
   ipfs daemon  
   ```  

5. **Run the Application**  
   Execute the Python script:  
   ```  
   python main.py  
   ```  

---

## Screenshots  

1. **Login Interface**  
   - Wallet-based authentication for Admin, Doctor, and Patient.  

2. **Admin Panel**  
   - Register doctors and patients.  
   - Manage transactions.  

3. **Doctor Panel**  
   - View patient records granted by patients.  

4. **Patient Panel**  
   - Upload records to IPFS.  
   - Grant/revoke doctor access.  

5. **Audit Trail**  
   - Log all user actions on the blockchain for transparency.  

---

## Future Enhancements  

1. Integration of Zero-Knowledge Proofs (ZK-SNARKs) for improved privacy.  
2. MetaMask desktop plugin for seamless transaction signing.  
3. Interoperability with other blockchain platforms.  
4. Enhanced UI/UX for greater user accessibility.  

---

## References  

1. Ethereum Documentation: [https://ethereum.org](https://ethereum.org)  
2. IPFS Documentation: [https://ipfs.io](https://ipfs.io)  
3. Web3.py: [https://web3py.readthedocs.io](https://web3py.readthedocs.io)  
4. Ganache: [https://trufflesuite.com/ganache](https://trufflesuite.com/ganache)  
5. Related Projects:  
   - [IBM Medical Blockchain](https://github.com/IBM/Medical-Blockchain)  
   - [Med-Chain](https://github.com/JeffreytheCoder/med-chain)  
   - [Decentralized Medical Records](https://github.com/jayateertha043/Decentralized-Medical-Records)  

---  

## Contact  

This was a group project made by:
Hamza HAFDAOUI
Hanane ZAOUI
Salma AMGAROU
