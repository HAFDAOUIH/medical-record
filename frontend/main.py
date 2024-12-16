import hashlib
import os
import re
import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from web3 import Web3
from tkinter import messagebox
import json
import contractAdresses as CA
from tkinter import filedialog
import webbrowser 
import ipfshttpclient


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Role Selection Page")
        
        
        self.root.geometry('1200x650')
        self.root.configure(fg_color='#E1EBEE')  

        # frames
        self.frame1 = ctk.CTkFrame(self.root, fg_color="#E1EBEE")
        self.frame2 = ctk.CTkFrame(self.root, fg_color="#E1EBEE")
        self.frame3 = ctk.CTkFrame(self.root, fg_color="#E1EBEE")
        self.frame4 = ctk.CTkFrame(self.root, fg_color="#E1EBEE")
        self.frame5 = ctk.CTkFrame(self.root, fg_color="#E1EBEE")
        self.frame6 = ctk.CTkFrame(self.root, fg_color="#E1EBEE")
        self.frame7 = ctk.CTkFrame(self.root, fg_color="#E1EBEE")
        self.frame8 = ctk.CTkFrame(self.root, fg_color="#E1EBEE")

        self.image_admin = Image.open(r"C:\Users\Hanane\Desktop\medical-record\frontend\img\equipement-utilisateur.png")
        self.image_admin = self.image_admin.resize((100, 100))  
        self.photo_admin = ctk.CTkImage(self.image_admin, size=(100, 100))

        self.image_doctor = Image.open(r"C:\Users\Hanane\Desktop\medical-record\frontend\img\doctor.png")
        self.image_doctor = self.image_doctor.resize((100, 100)) 
        self.photo_doctor = ctk.CTkImage(self.image_doctor, size=(100, 100))

        self.image_patient = Image.open(r"C:\Users\Hanane\Desktop\medical-record\frontend\img\patient.png")
        self.image_patient = self.image_patient.resize((100, 100))  
        self.photo_patient = ctk.CTkImage(self.image_patient, size=(100, 100))

        
        try:
            self.image_hospital = Image.open(r"C:\Users\Hanane\Desktop\medical-record\frontend\img\hospitalLogo.png")
            self.image_hospital = self.image_hospital.resize((120, 120)) 
            self.logo_image = ctk.CTkImage(self.image_hospital, size=(120, 120))  
        except FileNotFoundError:
            self.logo_image = None

        self.main_frame = ctk.CTkFrame(self.root, fg_color="#E1EBEE") 
        self.main_frame.pack(fill='both',expand=True)

        #header

        header_frame = ctk.CTkFrame(self.main_frame, fg_color="#B6D0E2", corner_radius=0)
        header_frame.pack(fill="x")


        if self.logo_image:
            logo_label = ctk.CTkLabel(header_frame, image=self.logo_image, text="")  
            logo_label.pack(side="left", padx=10, pady=10)

        header_text = ctk.CTkLabel(header_frame, text="Hospital Management System", 
                                font=("Arial", 24, "bold"), text_color="darkblue")
        header_text.pack(side="left", padx=250)
     
        
        self.button_frame = ctk.CTkFrame(self.main_frame, fg_color="#E1EBEE")  
        self.button_frame.pack(pady=150)
        
        self.label_admin = ctk.CTkLabel(self.button_frame, image=self.photo_admin, fg_color="#E1EBEE", text="")  
        self.label_admin.pack(side="left", padx=0)  
        self.button_admin = ctk.CTkButton(self.button_frame, text="Admin", command=self.show_frame1, fg_color="#E1EBEE", text_color="black", font=("Arial", 30, "bold"))
        self.button_admin.pack(side="left", padx=30)

        self.label_doctor = ctk.CTkLabel(self.button_frame, image=self.photo_doctor, fg_color="#E1EBEE", text="") 
        self.label_doctor.pack(side="left", padx=20)
        self.button_doctor = ctk.CTkButton(self.button_frame, text="Doctor", command=self.show_frame2, fg_color="#E1EBEE", text_color="black", font=("Arial", 30, "bold"))
        self.button_doctor.pack(side="left", padx=30)

        self.label_patient = ctk.CTkLabel(self.button_frame, image=self.photo_patient, fg_color="#E1EBEE", text="") 
        self.label_patient.pack(side="left", padx=20)
        self.button_patient = ctk.CTkButton(self.button_frame, text="Patient", command=self.show_frame3, fg_color="#E1EBEE", text_color="black", font=("Arial", 30, "bold"))
        self.button_patient.pack(side="left", padx=30)

        # Footer
        footer_frame1 = ctk.CTkFrame(self.main_frame, fg_color="#E1EBEE", corner_radius=0)
        footer_frame1.pack(fill="x", side="bottom")

        footer_text1 = ctk.CTkLabel(footer_frame1, text="© 2024 Hospital Management System", 
                                            font=("Arial", 12), text_color="gray")
        footer_text1.pack(pady=5)

        #Frame4



        def show_signup_admin():
            print("Register Admin button clicked")
            self.frame4.pack_forget()  
            self.frame8.pack(fill='both', expand=True)

            my_image = ctk.CTkImage(light_image=Image.open(r"C:\Users\Hanane\Desktop\medical-record\frontend\img\medicine-uniform-healthcare-medical-workers-day-concept.jpg"),
                        size=(550, 650)) 

        
            image_label = ctk.CTkLabel(self.frame8, image=my_image, text="")
            image_label.grid(row=0, column=0, padx=50, sticky="ns") 

            frame = ctk.CTkFrame(master=self.frame8, fg_color='#E1EBEE', width=400, height=200)
            frame.grid(row=0, column=1, sticky="nsew", padx=(0, 120))


            frame.columnconfigure(0, weight=1)
            sing_up_label = ctk.CTkLabel(
            frame, 
            text="Regester Admin", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
             )
            sing_up_label.grid(row=0, column=0, columnspan=2, padx=(20,70), pady=(100,30), sticky="w")

            label_wallet_address = ctk.CTkLabel(
                frame, 
                text="Wallet Address:", 
                fg_color="#E1EBEE", 
                font=("Arial", 18, "bold"),
                text_color="black"
            )
            label_wallet_address.grid(row=1, column=0, padx=30, pady=20, sticky="w")
            
            entry_wallet_address = ctk.CTkEntry(
                frame, 
                width=300, 
                font=("Arial", 16)
            )
            entry_wallet_address.grid(row=1, column=1, padx=10, pady=10)

            label_full_name = ctk.CTkLabel(
                frame, 
                text="Full Name:", 
                fg_color="#E1EBEE", 
                font=("Arial", 18, "bold"),
                text_color="black"
            )
            label_full_name.grid(row=2, column=0, padx=30, pady=20, sticky="w")
            
            entry_full_name = ctk.CTkEntry(
                frame, 
                width=300, 
                font=("Arial", 16)
            )
            entry_full_name.grid(row=2, column=1, padx=10, pady=10)

            
            label_password = ctk.CTkLabel(
                frame, 
                text="Password : ",
                fg_color="#E1EBEE", 
                font=("Arial", 18, "bold"),
                text_color="black"
            )
            label_password.grid(row=3, column=0, padx=30, pady=20, sticky="w")
            
            entry_password= ctk.CTkEntry(
                frame, 
                width=300, 
                font=("Arial", 16),
                show="•"
            )
            entry_password.grid(row=3, column=1, padx=10, pady=10)

            def register_admin( name, wallet_address, password):
                try:
            
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))  # Update with your RPC provider

                    # Smart contract details
                    contract_address = CA.admin_contract_adress 
                    ABI_PATH = 'build/contracts/AdminContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                    # Set up the contract
                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

                    # Get the account (using the first account)
                    account = wallet_address  

                    tx_hash = contract.functions.addAdmin(name, wallet_address, password).transact({
                            'from': account
                        })

                    w3.eth.wait_for_transaction_receipt(tx_hash)

                    print(f"Admin {name} successfully registered with wallet address {wallet_address}.")
                    messagebox.showinfo("Success", f"Admin successfully registered.")
                    self.frame8.pack_forget()  
                    self.frame1.pack(fill='both', expand=True)
                except Exception as e:
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")

            def button_event():
                print("Button pressed")
                admin_name = entry_full_name.get()
                wallet_address = entry_wallet_address.get()
                password = entry_password.get()
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                
                if not all([admin_name, wallet_address, password]):
                    messagebox.showerror("Error", "All fields are required.")
                else:
                    print("hh", admin_name, wallet_address, hashed_password)
                    register_admin( admin_name, wallet_address, hashed_password)

            

            button = ctk.CTkButton(frame, text="Submit",command=button_event)
            button.grid(row=4, column=1, padx=(170,0), pady=(20,20), sticky="w")



        def show_login_admin():
            print("Log In button clicked")
            self.frame4.pack_forget() 
            self.frame7.pack(fill='both', expand=True)
            my_image = ctk.CTkImage(light_image=Image.open(r"C:\Users\Hanane\Desktop\medical-record\frontend\img\medicine-uniform-healthcare-medical-workers-day-concept.jpg"),
                        size=(550, 650)) 

        
            image_label = ctk.CTkLabel(self.frame7, image=my_image, text="")
            image_label.grid(row=0, column=0, padx=50, sticky="ns") 

            frame = ctk.CTkFrame(master=self.frame7, fg_color='#E1EBEE', width=400, height=200)
            frame.grid(row=0, column=1, sticky="nsew", padx=(0, 120))


            frame.columnconfigure(0, weight=1)


            connect_wallet_label = ctk.CTkLabel(
                frame, 
                text="Log in", 
                font=("Arial", 30, "bold"), 
                fg_color="#E1EBEE", 
                text_color="black", 
                corner_radius=10
            )
            connect_wallet_label.grid(row=0, column=0, pady=(180, 10), sticky="w")

        
            wallet_address_label = ctk.CTkLabel(
                frame, 
                text="Wallet Address", 
                fg_color="#E1EBEE", 
                text_color="black", 
                corner_radius=10
            )
            wallet_address_label.grid(row=1, column=0, pady=(10, 5), sticky="w")

            wallet_address_entry = ctk.CTkEntry(
                frame, 
                placeholder_text="Enter your wallet address ", 
                width=300, 
                height=40, 
                corner_radius=10,
                fg_color="white", 
                text_color="black", 
                border_color="#E1EBEE"
            )
            wallet_address_entry.grid(row=2, column=0, pady=(10, 5), sticky="ew")

            password_label = ctk.CTkLabel(
                frame, 
                text="Password", 
                fg_color="#E1EBEE", 
                text_color="black", 
                corner_radius=10
            )
            password_label.grid(row=3, column=0, pady=(10, 5), sticky="w")

            password_entry = ctk.CTkEntry(
                frame, 
                placeholder_text="Enter your password ", 
                width=300, 
                height=40, 
                corner_radius=10,
                fg_color="white", 
                text_color="black", 
                border_color="#E1EBEE",
                show="•"
            )
            password_entry.grid(row=4, column=0, pady=(0, 20), sticky="ew")

            def loginn_admin( wallet_address, password):
                try:
            
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) 

                    contract_address = CA.admin_contract_adress 
                    ABI_PATH = 'build/contracts/AdminContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
                    
                    account = wallet_address  
                    
        
                    admin_name, retrieved_wallet_address, stored_hashed_password = contract.functions.getAdminInfoByWallet(account).call()
                    
                    provided_hashed_password = hashlib.sha256(password.encode()).hexdigest()

                    if provided_hashed_password == stored_hashed_password:
                        messagebox.showinfo("Login Successful", f"Welcome {admin_name}!")
                        self.frame7.pack_forget()  
                        self.frame1.pack(fill='both', expand=True)
                        print("new")
                    else:
                        messagebox.showerror("Login Failed", "Invalid password. Please try again.")
                

                
                except Exception as e:
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")

            def button_event():
                print("button pressed")
                
                wallet_address = wallet_address_entry.get()
                password = password_entry.get()

                if not all([wallet_address, password]):
                    messagebox.showerror("Error", "All fields are required.")
                else:
                   
                    loginn_admin( wallet_address, password)
                    



            submit_button = ctk.CTkButton(frame, text="Submit", command=button_event)
            submit_button.grid(row=5, column=0, pady=(10, 10), sticky="ew")

      


 
        header_frame2 = ctk.CTkFrame(self.frame4, fg_color="#B6D0E2", corner_radius=0)
        header_frame2.pack(fill="x")


        if self.logo_image:
            logo_label = ctk.CTkLabel(header_frame2, image=self.logo_image, text="")  
            logo_label.pack(side="left", padx=10, pady=10)

        header_text = ctk.CTkLabel(header_frame2, text="Hospital Management System", 
                                font=("Arial", 24, "bold"), text_color="darkblue")
        header_text.pack(side="left", padx=250)

        main_frame = ctk.CTkFrame(self.frame4,fg_color="#E1EBEE")
        main_frame.pack(pady=50, padx=20, fill="both", expand=True)

        welcome_label = ctk.CTkLabel(main_frame, text="Welcome! Please choose an option below:", 
                                            font=("Arial", 18), text_color="black")
        welcome_label.pack(pady=20)

        # Add Register Admin button
        register_button = ctk.CTkButton(main_frame, text="Register Admin",  
                                                font=("Arial", 16), 
                                                fg_color="dodgerblue", 
                                                hover_color="skyblue", 
                                                width=200, height=50,
                                                command=show_signup_admin)
        register_button.pack(pady=10)

        # Add Log In button
        login_button = ctk.CTkButton(main_frame, text="Log In",  
                                            font=("Arial", 16), 
                                            fg_color="dodgerblue", 
                                            hover_color="lightblue", 
                                            width=200, height=50,
                                            command=show_login_admin
                                            )
        login_button.pack(pady=10)

        footer_frame = ctk.CTkFrame(self.frame4, fg_color="#E1EBEE", corner_radius=0)
        footer_frame.pack(fill="x", side="bottom")

        footer_text = ctk.CTkLabel(footer_frame, text="© 2024 Hospital Management System", 
                                            font=("Arial", 12), text_color="gray")
        footer_text.pack(pady=5)

        #frame 5 : doctor log in

        my_image = ctk.CTkImage(light_image=Image.open(r"C:\Users\Hanane\Desktop\medical-record\frontend\img\medicine-uniform-healthcare-medical-workers-day-concept.jpg"),
                        size=(550, 650)) 

        
        image_label = ctk.CTkLabel(self.frame5, image=my_image, text="")
        image_label.grid(row=0, column=0, padx=50, sticky="ns") 

        frame = ctk.CTkFrame(master=self.frame5, fg_color='#E1EBEE', width=400, height=200)
        frame.grid(row=0, column=1, sticky="nsew", padx=(0, 120))


        frame.columnconfigure(0, weight=1)


        connect_wallet_label = ctk.CTkLabel(
            frame, 
            text="Log in", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        connect_wallet_label.grid(row=0, column=0, pady=(180, 10), sticky="w")

    
        wallet_address_label = ctk.CTkLabel(
            frame, 
            text="Wallet Address", 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        wallet_address_label.grid(row=1, column=0, pady=(10, 5), sticky="w")

        wallet_address_entry_doc = ctk.CTkEntry(
            frame, 
            placeholder_text="Enter your wallet address ", 
            width=300, 
            height=40, 
            corner_radius=10,
            fg_color="white", 
            text_color="black", 
            border_color="#E1EBEE"
        )
        wallet_address_entry_doc.grid(row=2, column=0, pady=(10, 5), sticky="ew")

        password_label = ctk.CTkLabel(
            frame, 
            text="Password", 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        password_label.grid(row=3, column=0, pady=(10, 5), sticky="w")

        password_entry_doc = ctk.CTkEntry(
            frame, 
            placeholder_text="Enter your password ", 
            width=300, 
            height=40, 
            corner_radius=10,
            fg_color="white", 
            text_color="black", 
            border_color="#E1EBEE",
            show="•"
        )
        password_entry_doc.grid(row=4, column=0, pady=(0, 20), sticky="ew")

        def loginn_doctor(wallet_address, password):
            try:
                w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
                print(CA.doctor_contract_adress)
                contract_address = CA.doctor_contract_adress
                ABI_PATH = 'build/contracts/DoctorContract.json'
                
                if not os.path.exists(ABI_PATH):
                    raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")
                
                with open(ABI_PATH, 'r') as abi_file:
                    contract_abi = json.load(abi_file)['abi']

                contract = w3.eth.contract(address=contract_address, abi=contract_abi)
                account = wallet_address
                
                # Call the contract to get doctor info
                result = contract.functions.getDoctorInfo(account).call()
                print(f"Doctor info: {result}")
                
                # Unpack the result tuple
                doctor_name, speciality, licenseNumber, contactInfo, stored_hashed_password = result

                # Hash the provided password and compare
                provided_hashed_password = hashlib.sha256(password.encode()).hexdigest()

                if provided_hashed_password == stored_hashed_password:
                    messagebox.showinfo("Login Successful", f"Welcome {doctor_name}!")
                    self.wallet_address_doctor = wallet_address
                    self.frame5.pack_forget()  
                    self.frame2.pack(fill='both', expand=True)
                    print("new",wallet_address)
                    
                else:
                    messagebox.showerror("Login Failed", "Invalid password. Please try again.")
            except Exception as e:
                messagebox.showerror("Error", f"Transaction failed: {str(e)}")
                print(str(e))

        def button_event():
            print("button pressed doctor")
            password_doc = password_entry_doc.get()
            wallet_address_doc = wallet_address_entry_doc.get()
            if not all([wallet_address_doc, password_doc]):
                messagebox.showerror("Error", "All fields are required.")
            else:
                   
                loginn_doctor( wallet_address_doc, password_doc)

        submit_button = ctk.CTkButton(frame, text="Submit", command=button_event)
        submit_button.grid(row=5, column=0, pady=(10, 10), sticky="ew")

      

        #frame 6 : patient log in
    
        my_image = ctk.CTkImage(light_image=Image.open(r"C:\Users\Hanane\Desktop\medical-record\frontend\img\medicine-uniform-healthcare-medical-workers-day-concept.jpg"),
                        size=(550, 650)) 

        
        image_label = ctk.CTkLabel(self.frame6, image=my_image, text="")
        image_label.grid(row=0, column=0, padx=50, sticky="ns") 

        frame = ctk.CTkFrame(master=self.frame6, fg_color='#E1EBEE', width=400, height=200)
        frame.grid(row=0, column=1, sticky="nsew", padx=(0, 120))


        frame.columnconfigure(0, weight=1)


        connect_wallet_label = ctk.CTkLabel(
            frame, 
            text="Log in", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        connect_wallet_label.grid(row=0, column=0, pady=(180, 10), sticky="w")

    
        wallet_address_label = ctk.CTkLabel(
            frame, 
            text="Wallet Address", 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        wallet_address_label.grid(row=1, column=0, pady=(10, 5), sticky="w")

        wallet_address_entry3 = ctk.CTkEntry(
            frame, 
            placeholder_text="Enter your wallet address ", 
            width=300, 
            height=40, 
            corner_radius=10,
            fg_color="white", 
            text_color="black", 
            border_color="#E1EBEE"
        )
        wallet_address_entry3.grid(row=2, column=0, pady=(10, 5), sticky="ew")

        password_label = ctk.CTkLabel(
            frame, 
            text="Password", 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        password_label.grid(row=3, column=0, pady=(10, 5), sticky="w")

        password_entry3 = ctk.CTkEntry(
            frame, 
            placeholder_text="Enter your password ", 
            width=300, 
            height=40, 
            corner_radius=10,
            fg_color="white", 
            text_color="black", 
            border_color="#E1EBEE",
            show="•"
        )
        password_entry3.grid(row=4, column=0, pady=(0, 20), sticky="ew")
        def loginn_patient(wallet_address, password):
            try:
                w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
                print(CA.doctor_contract_adress)
                contract_address = CA.patient_contract_adress
                ABI_PATH = 'build/contracts/PatientContract.json'
                
                if not os.path.exists(ABI_PATH):
                    raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")
                
                with open(ABI_PATH, 'r') as abi_file:
                    contract_abi = json.load(abi_file)['abi']

                contract = w3.eth.contract(address=contract_address, abi=contract_abi)
                account = wallet_address
                
                # Call the contract to get doctor info
                result = contract.functions.getPatientInfo(account).call()
                print(f"Doctor info: {result}")
                
                # Unpack the result tuple
                full_name,gender,age, weight,height,blood_type,allergies,stored_hashed_password = result

                # Hash the provided password and compare
                provided_hashed_password = hashlib.sha256(password.encode()).hexdigest()

                if provided_hashed_password == stored_hashed_password:
                    messagebox.showinfo("Login Successful", f"Welcome {full_name}!")
                    self.wallet_address_pateint = wallet_address
                    self.frame6.pack_forget()  
                    self.frame3.pack(fill='both', expand=True)
                    print("new",wallet_address)
                    
                else:
                    messagebox.showerror("Login Failed", "Invalid password. Please try again.")
            except Exception as e:
                messagebox.showerror("Error", f"Transaction failed: {str(e)}")
                print(str(e))
        def button_event():
            print("button pressed doctor")
            password_doc = password_entry3.get()
            wallet_address_pateint = wallet_address_entry3.get()

            if not all([wallet_address_pateint, password_doc]):
                messagebox.showerror("Error", "All fields are required.")
            else:
                   
                loginn_patient( wallet_address_pateint, password_doc)
                
           

        submit_button = ctk.CTkButton(frame, text="Submit", command=button_event)
        submit_button.grid(row=5, column=0, pady=(10, 10), sticky="ew")
        # Frame 1
        self.sidebar1 = ctk.CTkFrame(self.frame1, fg_color="#B6D0E2", width=600)
        self.sidebar1.grid(row=0, column=0, sticky="ns")

        self.sidebar_image_label = ctk.CTkLabel(self.sidebar1, image=self.photo_admin, fg_color="#B6D0E2", text="")
        self.sidebar_image_label.pack(pady=10)
        self.sidebar_text_label = ctk.CTkLabel(self.sidebar1, text="Admin Panel", fg_color="#B6D0E2", text_color="black", font=("Arial", 20, "bold"))
        self.sidebar_text_label.pack(pady=10)

        self.frame1.grid_rowconfigure(0, weight=1, minsize=650)

        self.button_sidebar1 = ctk.CTkButton(self.sidebar1, text="Register Doctor", fg_color="#B6D0E2", font=("Arial", 18, "bold"), text_color="black",command=self.register_doctor_form )
        self.button_sidebar1.pack(pady=25, padx=60)

        self.button_sidebar2 = ctk.CTkButton(self.sidebar1, text="Register Patient", fg_color="#B6D0E2", font=("Arial", 18, "bold"), text_color="black",command=self.register_patient_form)
        self.button_sidebar2.pack(pady=25, padx=60)

        self.button_sidebar3 = ctk.CTkButton(self.sidebar1, text="View Transactions", fg_color="#B6D0E2", font=("Arial", 18, "bold"), text_color="black",)
        self.button_sidebar3.pack(pady=25, padx=60)

        self.button_sidebar4 = ctk.CTkButton(self.sidebar1, text="Log Out", fg_color="#B6D0E2", font=("Arial", 18, "bold"), text_color="black", command=self.logout)
        self.button_sidebar4.pack(pady=25, padx=60)

        self.main_content1 = ctk.CTkFrame(self.frame1, fg_color="#E1EBEE")
        self.main_content1.grid(row=0, column=1, padx=20, pady=20)

       
        self.button_main_content1 = ctk.CTkButton(self.main_content1, text="Main Content Button", fg_color="#E1EBEE", text_color="black", font=("Arial", 20), command=self.logout)
        self.button_main_content1.pack(pady=20)

        # Frame 2
        self.sidebar2 = ctk.CTkFrame(self.frame2, fg_color="#B6D0E2", width=600)
        self.sidebar2.grid(row=0, column=0, sticky="ns")

        self.sidebar_image_label2 = ctk.CTkLabel(self.sidebar2, image=self.photo_doctor, fg_color="#B6D0E2", text="")
        self.sidebar_image_label2.pack(pady=10)
        self.sidebar_text_label2 = ctk.CTkLabel(self.sidebar2, text="Doctor Panel", fg_color="#B6D0E2", text_color="black", font=("Arial", 20, "bold"))
        self.sidebar_text_label2.pack(pady=10)

        self.frame2.grid_rowconfigure(0, weight=1, minsize=650)

        self.button_sidebar2_1 = ctk.CTkButton(self.sidebar2, text="View Profile", fg_color="#B6D0E2", text_color="black", font=("Arial", 18),command=self.View_profile_doctor)
        self.button_sidebar2_1.pack(pady=25, padx=60)

        self.button_sidebar2_2 = ctk.CTkButton(self.sidebar2, text="Edit Profile", fg_color="#B6D0E2", text_color="black", font=("Arial", 18),command=self.edit_profile_doctor)
        self.button_sidebar2_2.pack(pady=25, padx=60)

        self.button_sidebar2_3 = ctk.CTkButton(self.sidebar2, text="Patients", fg_color="#B6D0E2", text_color="black", font=("Arial", 18),command=self.View_patient)
        self.button_sidebar2_3.pack(pady=25, padx=60)

        self.button_sidebar2_4 = ctk.CTkButton(self.sidebar2, text="Log Out", fg_color="#B6D0E2", text_color="black", font=("Arial", 18), command=self.logout)
        self.button_sidebar2_4.pack(pady=25, padx=60)

        self.main_content2 = ctk.CTkFrame(self.frame2, fg_color="#E1EBEE")
        self.main_content2.grid(row=0, column=1, padx=20, pady=20)

        self.button_main_content2 = ctk.CTkButton(self.main_content2, text="", fg_color="#E1EBEE", text_color="black", font=("Arial", 20))
        self.button_main_content2.pack(pady=20)

        # Frame 3
        self.sidebar3 = ctk.CTkFrame(self.frame3, fg_color="#B6D0E2", width=600)
        self.sidebar3.grid(row=0, column=0, sticky="ns")

        self.sidebar_image_label3 = ctk.CTkLabel(self.sidebar3, image=self.photo_patient, fg_color="#B6D0E2", text="")
        self.sidebar_image_label3.pack(pady=10)
        self.sidebar_text_label3 = ctk.CTkLabel(self.sidebar3, text="Patient Panel", fg_color="#B6D0E2", text_color="black", font=("Arial", 20, "bold"))
        self.sidebar_text_label3.pack(pady=10)

        self.frame3.grid_rowconfigure(0, weight=1, minsize=650)

        self.button_sidebar3_1 = ctk.CTkButton(self.sidebar3, text="View Profile", fg_color="#B6D0E2", text_color="black", font=("Arial", 18),command=self.View_profile_Patient)
        self.button_sidebar3_1.pack(pady=25, padx=60)

        self.button_sidebar3_2 = ctk.CTkButton(self.sidebar3, text="Edit Profile", fg_color="#B6D0E2", text_color="black", font=("Arial", 18),command=self.Edit_patient_profile)
        self.button_sidebar3_2.pack(pady=25, padx=60)

        self.button_sidebar3_3 = ctk.CTkButton(self.sidebar3, text="Add Medical Record", fg_color="#B6D0E2", text_color="black", font=("Arial", 18),command=self.Add_patient_record)
        self.button_sidebar3_3.pack(pady=25, padx=60)

        self.button_sidebar3_4 = ctk.CTkButton(self.sidebar3, text="Log Out", fg_color="#B6D0E2", text_color="black", font=("Arial", 18), command=self.logout)
        self.button_sidebar3_4.pack(pady=25, padx=60)

        self.main_content3 = ctk.CTkFrame(self.frame3, fg_color="#E1EBEE")
        self.main_content3.grid(row=0, column=1, padx=20, pady=20)

        self.button_main_content3 = ctk.CTkButton(self.main_content3, text="Main Content Button", fg_color="#E1EBEE", text_color="black", font=("Arial", 20))
        self.button_main_content3.pack(pady=20)

    def show_frame1(self):
        self.main_frame.pack_forget()  # Hide the main frame
        self.frame4.pack(fill='both', expand=True) #frame4

    def show_frame2(self):
        self.main_frame.pack_forget()  # Hide the main frame
        self.frame5.pack(fill='both', expand=True)  # Show frame for Doctor, fill both dimensions

    def show_frame3(self):
        self.main_frame.pack_forget()  # Hide the main frame
        self.frame6.pack(fill='both', expand=True)

    def logout(self):
        # Hide all frames and show the root frame again (main_frame)
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.main_frame.pack(fill='both',expand=True)




    def register_doctor_form(self):
        
        for widget in self.main_content1.winfo_children():
            widget.destroy()


        sing_up_label = ctk.CTkLabel(
            self.main_content1, 
            text="Regester Doctor", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        sing_up_label.grid(row=0, column=0, columnspan=2, padx=(20,70), pady=(30), sticky="w")

        label_wallet_address = ctk.CTkLabel(
            self.main_content1, 
            text="Wallet Address:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_wallet_address.grid(row=1, column=0, padx=30, pady=20, sticky="w")
        
        entry_wallet_address = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_wallet_address.grid(row=1, column=1, padx=10, pady=10)

        label_full_name = ctk.CTkLabel(
            self.main_content1, 
            text="Full Name:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_full_name.grid(row=2, column=0, padx=30, pady=20, sticky="w")
        
        entry_full_name = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_full_name.grid(row=2, column=1, padx=10, pady=10)

        

        label_Speciality= ctk.CTkLabel(
            self.main_content1, 
            text="Speciality :", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_Speciality.grid(row=3, column=0, padx=30, pady=20, sticky="w")
        
        entry_Speciality = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_Speciality.grid(row=3, column=1, padx=10, pady=10)

        label_LicenseNumber = ctk.CTkLabel(
            self.main_content1, 
            text="License Number:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_LicenseNumber.grid(row=4, column=0, padx=30, pady=20, sticky="w")
        
        entry_LicenseNumber = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_LicenseNumber.grid(row=4, column=1, padx=10, pady=10)

        label_ContactInfo = ctk.CTkLabel(
            self.main_content1, 
            text="Contact :", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_ContactInfo.grid(row=5, column=0, padx=30, pady=20, sticky="w")
        
        entry_ContactInfo = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_ContactInfo.grid(row=5, column=1, padx=10, pady=10)

        label_password = ctk.CTkLabel(
            self.main_content1, 
            text="Password : ",
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_password.grid(row=6, column=0, padx=30, pady=20, sticky="w")
        
        entry_password= ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16),
            show="•"
        )
        entry_password.grid(row=6, column=1, padx=10, pady=10)
        def register_Docter_contract( wallet_address_doctor,doctor_name,Speciality,licenseNumber,contact,hashed_password):
                try:
            
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) # Update with your RPC provider

                    # Smart contract details
                    contract_address = CA.doctor_contract_adress
                    ABI_PATH = 'build/contracts/DoctorContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                    # Set up the contract
                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

                    
                    account = wallet_address_doctor  

                    tx_hash = contract.functions.registerDoctor(doctor_name,Speciality,licenseNumber,contact,hashed_password,wallet_address_doctor).transact({
                            'from': account
                        })

                    w3.eth.wait_for_transaction_receipt(tx_hash)

                    print(f"Doctor successfully registered .")
                    entry_wallet_address.delete(0, 'end')
                    entry_full_name.delete(0, 'end')
                    entry_Speciality.delete(0, 'end')
                    entry_LicenseNumber.delete(0, 'end')
                    entry_ContactInfo.delete(0, 'end')
                    entry_password.delete(0, 'end')
                    messagebox.showinfo("Success", f"Doctor successfully registered.")
                    
                except Exception as e:
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")
        def button_event():
            print("Button pressed")
            global wallet_address_doctor
            wallet_address_doctor = entry_wallet_address.get()
            doctor_name = entry_full_name.get()
            Speciality = entry_Speciality.get()
            licenseNumber = entry_LicenseNumber.get()
            contact = entry_ContactInfo.get()
            password = entry_password.get()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            

            if not all([wallet_address_doctor,doctor_name,Speciality,licenseNumber,contact,hashed_password]):
                messagebox.showerror("Error", "All fields are required.")
            else:
                register_Docter_contract(wallet_address_doctor,doctor_name,Speciality,licenseNumber,contact,hashed_password)
                

        button = ctk.CTkButton(self.main_content1, text="Submit",command=button_event)
        button.grid(row=7, column=1, padx=(170,0), pady=(20,20), sticky="w")



    def register_patient_form(self):

        for widget in self.main_content1.winfo_children():
            widget.destroy()

       
        sing_up_label = ctk.CTkLabel(
            self.main_content1, 
            text="Register Patient", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        sing_up_label.grid(row=0, column=0, columnspan=2, padx=(20, 70), pady=(10), sticky="w")

        label_wallet_address = ctk.CTkLabel(
            self.main_content1, 
            text="Wallet Address:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_wallet_address.grid(row=1, column=0, padx=30, pady=10, sticky="w")
        
        entry_wallet_address = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_wallet_address.grid(row=1, column=1, padx=10, pady=10)


        label_full_name = ctk.CTkLabel(
            self.main_content1, 
            text="Full Name:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_full_name.grid(row=2, column=0, padx=30, pady=10, sticky="w")
        
        entry_full_name = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_full_name.grid(row=2, column=1, padx=10, pady=10)

        
        label_gender = ctk.CTkLabel(
            self.main_content1, 
            text="Gender:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_gender.grid(row=3, column=0, padx=30, pady=10, sticky="w")
        
        combobox = ctk.CTkComboBox(
            self.main_content1, 
            values=["Male", "Female"],
            fg_color="white",
            text_color="black",
            dropdown_fg_color="white",
            border_color="grey",
            dropdown_text_color="black",
            button_color="grey",
            dropdown_hover_color="#1877F2",
            button_hover_color="#1877F2"
        )
        combobox.set("Female")
        combobox.grid(row=3, column=1, padx=(10), pady=(5,5), sticky="ew")

        label_age = ctk.CTkLabel(
            self.main_content1, 
            text="Age:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_age.grid(row=4, column=0, padx=30, pady=10, sticky="w")
        
        entry_age = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_age.grid(row=4, column=1, padx=10, pady=10)

        label_weight = ctk.CTkLabel(
            self.main_content1, 
            text="Weight (kg):", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_weight.grid(row=5, column=0, padx=30, pady=10, sticky="w")
        
        entry_weight = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_weight.grid(row=5, column=1, padx=10, pady=10)

        label_height = ctk.CTkLabel(
            self.main_content1, 
            text="Height (cm):", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_height.grid(row=6, column=0, padx=30, pady=10, sticky="w")
        
        entry_height = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_height.grid(row=6, column=1, padx=10, pady=10)


        label_blood_type = ctk.CTkLabel(
            self.main_content1, 
            text="Blood Type:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_blood_type.grid(row=7, column=0, padx=30, pady=10, sticky="w")
        
        entry_blood_type = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_blood_type.grid(row=7, column=1, padx=10, pady=10)

        label_allergies = ctk.CTkLabel(
            self.main_content1, 
            text="Allergies:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_allergies.grid(row=8, column=0, padx=30, pady=10, sticky="w")
        
        entry_allergies = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16)
        )
        entry_allergies.grid(row=8, column=1, padx=10, pady=10)


        label_password = ctk.CTkLabel(
            self.main_content1, 
            text="Password:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
            
        )
        label_password.grid(row=9, column=0, padx=30, pady=10, sticky="w")
        
        entry_password = ctk.CTkEntry(
            self.main_content1, 
            width=300, 
            font=("Arial", 16), 
            show="•"
        )
        entry_password.grid(row=9, column=1, padx=10, pady=10)

        def register_Patient_contract( wallet_address,full_name,gender,age, weight,height,blood_type,allergies,hashed_password):
                try:
            
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) # Update with your RPC provider

                    # Smart contract details
                    contract_address = CA.patient_contract_adress
                    ABI_PATH = 'build/contracts/PatientContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                 
                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

                    encryptionKey="1"
                    account = wallet_address  

                    tx_hash = contract.functions.registerPatient(full_name,gender,age, weight,height,blood_type,allergies,wallet_address,hashed_password,encryptionKey).transact({
                            'from': account
                        })

                    w3.eth.wait_for_transaction_receipt(tx_hash)

                    print(f"Patient successfully registered .")
                    entry_wallet_address.delete(0, 'end')
                    entry_full_name.delete(0, 'end')
                    entry_age.delete(0, 'end')
                    entry_weight.delete(0, 'end')
                    entry_height.delete(0, 'end')
                    entry_blood_type.delete(0, 'end')
                    entry_allergies.delete(0, 'end')
                    entry_password.delete(0, 'end')
                    combobox.set("")
                    
                    messagebox.showinfo("Success", f"Patient successfully registered.")
                    
                except Exception as e:
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")
        def button_event():

            print("Form submitted")
            wallet_address = entry_wallet_address.get()
            full_name = entry_full_name.get()
            gender = combobox.get()
            age = entry_age.get()
            try:
                age = int(age)
            except ValueError:
                messagebox.showerror("Error","Invalid age input, please enter a valid number.")
                return
            weight = entry_weight.get()
            try:
                weight = int(weight)
            except ValueError:
                messagebox.showerror("Error","Invalid weight input, please enter a valid number.")
                return
            height = entry_height.get()
            try:
                height = int(height)
            except ValueError:
                messagebox.showerror("Error","Invalid height input, please enter a valid number.")
                return
            blood_type = entry_blood_type.get()
            allergies = entry_allergies.get()
            password = entry_password.get()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if not all([wallet_address,full_name,gender,age, weight,height,blood_type,allergies,hashed_password]):
                messagebox.showerror("Error", "All fields are required.")
            else:
                register_Patient_contract(wallet_address,full_name,gender,age, weight,height,blood_type,allergies,hashed_password)
                print(wallet_address,full_name,gender,age, weight,height,blood_type,allergies,hashed_password)

        button = ctk.CTkButton(self.main_content1, text="Submit", command=button_event)
        button.grid(row=10, column=1, padx=(170, 0), pady=(10), sticky="w")

            

    def View_profile_doctor(self):
            
            for widget in self.main_content2.winfo_children():
                widget.destroy()
            
            try:
            
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) # Update with your RPC provider

                    # Smart contract details
                    contract_address = CA.doctor_contract_adress
                    ABI_PATH = 'build/contracts/DoctorContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                    # Set up the contract
                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

                    
                    account = self.wallet_address_doctor  

                    result = contract.functions.getDoctorInfo(account).call()
                    print(f"Doctor info: {result}")
                
               
                    doctor_name, speciality, licenseNumber, contactInfo, stored_hashed_password = result

                    
            except Exception as e:
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")


            sing_up_label = ctk.CTkLabel(
                self.main_content2, 
                text="Profil", 
                font=("Arial", 30, "bold"), 
                fg_color="#E1EBEE", 
                text_color="black", 
                corner_radius=10
            )
            sing_up_label.grid(row=0, column=0, columnspan=2, padx=(20,70), pady=(30), sticky="w")

            
            label_full_name = ctk.CTkLabel(
            self.main_content2, 
            text="Full Name:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
            )
            label_full_name.grid(row=1, column=0, padx=30, pady=20, sticky="w")
            
            label_full_name2 = ctk.CTkLabel(
            self.main_content2, 
            text= doctor_name, 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
            )
            label_full_name2.grid(row=1, column=1, padx=30, pady=20, sticky="w")

            label_Speciality= ctk.CTkLabel(
                self.main_content2, 
                text="Speciality :", 
                fg_color="#E1EBEE", 
                font=("Arial", 18, "bold"),
                text_color="black"
            )
            label_Speciality.grid(row=2, column=0, padx=30, pady=20, sticky="w")
            
            label_Speciality1= ctk.CTkLabel(
                self.main_content2, 
                text=speciality, 
                fg_color="#E1EBEE", 
                font=("Arial", 18, "bold"),
                text_color="black"
            )
            label_Speciality1.grid(row=2, column=1, padx=30, pady=20, sticky="w")
            
            label_LicenseNumber = ctk.CTkLabel(
                self.main_content2, 
                text="License Number:", 
                fg_color="#E1EBEE", 
                font=("Arial", 18, "bold"),
                text_color="black"
            )
            label_LicenseNumber.grid(row=3, column=0, padx=30, pady=20, sticky="w")
            
            label_LicenseNumber = ctk.CTkLabel(
                self.main_content2, 
                text=licenseNumber, 
                fg_color="#E1EBEE", 
                font=("Arial", 18, "bold"),
                text_color="black"
            )
            label_LicenseNumber.grid(row=3, column=1, padx=30, pady=20, sticky="w")

            label_ContactInfo = ctk.CTkLabel(
                self.main_content2, 
                text="Contact :", 
                fg_color="#E1EBEE", 
                font=("Arial", 18, "bold"),
                text_color="black"
            )
            label_ContactInfo.grid(row=4, column=0, padx=30, pady=20, sticky="w")
            label_ContactInfo1 = ctk.CTkLabel(
                self.main_content2, 
                text=contactInfo, 
                fg_color="#E1EBEE", 
                font=("Arial", 18, "bold"),
                text_color="black"
            )
            label_ContactInfo1.grid(row=4, column=1, padx=30, pady=20, sticky="w")
        
        
    def edit_profile_doctor(self):
        for widget in self.main_content2.winfo_children():
                widget.destroy()
            
        try:
            
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) # Update with your RPC provider

                    # Smart contract details
                    contract_address = CA.doctor_contract_adress
                    ABI_PATH = 'build/contracts/DoctorContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                    # Set up the contract
                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

                    
                    account = self.wallet_address_doctor  

                    result = contract.functions.getDoctorInfo(account).call()
                    print(f"Doctor info: {result}")
                
               
                    doctor_name, speciality, licenseNumber, contactInfo, stored_hashed_password = result

                    
        except Exception as e:
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")
        
        sing_up_label = ctk.CTkLabel(
            self.main_content2, 
            text="Edit Profile", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        sing_up_label.grid(row=0, column=0, columnspan=2, padx=(20,70), pady=(30), sticky="w")

        

        full_name_var = ctk.StringVar()
        speciality_var = ctk.StringVar()
        license_number_var = ctk.StringVar()
        contact_info_var = ctk.StringVar()

        
        full_name_var.set(doctor_name)
        speciality_var.set(speciality)
        license_number_var.set(licenseNumber)
        contact_info_var.set(contactInfo)

        
        label_full_name = ctk.CTkLabel(
            self.main_content2,  
            text="Full Name:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_full_name.grid(row=2, column=0, padx=30, pady=20, sticky="w")

        entry_full_name = ctk.CTkEntry(
            self.main_content2,  
            width=300, 
            font=("Arial", 16),
            textvariable=full_name_var  
        )
        entry_full_name.grid(row=2, column=1, padx=10, pady=10)

        label_Speciality = ctk.CTkLabel(
            self.main_content2,  
            text="Speciality:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_Speciality.grid(row=3, column=0, padx=30, pady=20, sticky="w")

        entry_Speciality = ctk.CTkEntry(
            self.main_content2,  
            width=300, 
            font=("Arial", 16),
            textvariable=speciality_var  
        )
        entry_Speciality.grid(row=3, column=1, padx=10, pady=10)

        label_LicenseNumber = ctk.CTkLabel(
            self.main_content2,  
            text="License Number:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_LicenseNumber.grid(row=4, column=0, padx=30, pady=20, sticky="w")

        entry_LicenseNumber = ctk.CTkEntry(
            self.main_content2, 
            width=300, 
            font=("Arial", 16),
            textvariable=license_number_var  
        )
        entry_LicenseNumber.grid(row=4, column=1, padx=10, pady=10)

        label_ContactInfo = ctk.CTkLabel(
            self.main_content2,  
            text="Contact:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_ContactInfo.grid(row=5, column=0, padx=30, pady=20, sticky="w")

        entry_ContactInfo = ctk.CTkEntry(
            self.main_content2,  
            width=300, 
            font=("Arial", 16),
            textvariable=contact_info_var  
        )
        entry_ContactInfo.grid(row=5, column=1, padx=10, pady=10)

        def button_event():

            doctor_name = entry_full_name.get()
            Speciality = entry_Speciality.get()
            licenseNumber = entry_LicenseNumber.get()
            contact = entry_ContactInfo.get()
            try:
            
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) # Update with your RPC provider

                    # Smart contract details
                    contract_address = CA.doctor_contract_adress
                    ABI_PATH = 'build/contracts/DoctorContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                    # Set up the contract
                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

                    
                    account = self.wallet_address_doctor  

                    tx_hash = contract.functions.updateDoctorInfo(doctor_name,Speciality,licenseNumber,contact,account).transact({
                            'from': account
                        })

                    w3.eth.wait_for_transaction_receipt(tx_hash)
                    messagebox.showinfo("Success", f"Profile successfully updated.")
                    self.View_profile_doctor()

                    
            except Exception as e:
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")
        submit_button = ctk.CTkButton(self.main_content2, text="Submit", command=button_event)
        submit_button.grid(row=6, column=0, pady=(10, 10), sticky="ew")

    def View_profile_Patient(self):
       
        for widget in self.main_content3.winfo_children():
            widget.destroy()

        try:
            
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) 
                    contract_address = CA.patient_contract_adress
                    ABI_PATH = 'build/contracts/PatientContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                 
                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
                    account = self.wallet_address_pateint
                    result = contract.functions.getPatientInfo(account).call()
                    print(f"Doctor info: {result}")
                
                    # Unpack the result tuple
                    full_name,gender,age, weight,height,blood_type,allergies,stored_hashed_password = result

                    
                    
                    
                    
        except Exception as e:
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")
      

        sing_up_label = ctk.CTkLabel(
            self.main_content3, 
            text="Profil", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        sing_up_label.grid(row=0, column=0, columnspan=2, padx=(20,70), pady=(30), sticky="w")
        

        label_full_name = ctk.CTkLabel(
            self.main_content3,  
            text="Full Name:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_full_name.grid(row=1, column=0, padx=30, pady=10, sticky="w")
        
        elabel_full_name1 = ctk.CTkLabel(
            self.main_content3,  
            text=full_name, 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        elabel_full_name1.grid(row=1, column=1, padx=30, pady=10, sticky="w")

        
        label_gender = ctk.CTkLabel(
            self.main_content3, 
            text="Gender:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_gender.grid(row=2, column=0, padx=30, pady=10, sticky="w")
        
        label_gender1 = ctk.CTkLabel(
            self.main_content3, 
            text=gender, 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_gender1.grid(row=2, column=1, padx=30, pady=10, sticky="w")
        
        label_age = ctk.CTkLabel(
            self.main_content3, 
            text="Age:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_age.grid(row=3, column=0, padx=30, pady=10, sticky="w")
        
        label_age1 = ctk.CTkLabel(
            self.main_content3, 
            text= age, 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_age1.grid(row=3, column=1, padx=30, pady=10, sticky="w")

        label_weight = ctk.CTkLabel(
            self.main_content3, 
            text="Weight (kg):", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_weight.grid(row=4, column=0, padx=30, pady=10, sticky="w")
        
        label_weight1 = ctk.CTkLabel(
            self.main_content3, 
            text= weight, 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_weight1.grid(row=4, column=1, padx=30, pady=10, sticky="w")

        label_height = ctk.CTkLabel(
            self.main_content3,
            text="Height (cm):", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_height.grid(row=5, column=0, padx=30, pady=10, sticky="w")
        
        label_height1 = ctk.CTkLabel(
            self.main_content3,
            text=height, 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_height1.grid(row=5, column=1, padx=30, pady=10, sticky="w")

        label_blood_type = ctk.CTkLabel(
            self.main_content3,
            text="Blood Type:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_blood_type.grid(row=6, column=0, padx=30, pady=10, sticky="w")
        
        label_blood_type1 = ctk.CTkLabel(
            self.main_content3,
            text=blood_type, 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_blood_type1.grid(row=6, column=1, padx=30, pady=10, sticky="w")
        
        label_allergies = ctk.CTkLabel(
            self.main_content3,
            text="Allergies:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_allergies.grid(row=7, column=0, padx=30, pady=10, sticky="w")
        
        label_allergies1 = ctk.CTkLabel(
            self.main_content3,
            text=allergies, 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_allergies1.grid(row=7, column=1, padx=30, pady=10, sticky="w")
        

        
        




    def Edit_patient_profile(self):

        for widget in self.main_content3.winfo_children():
            widget.destroy()
        print("patientprofile")
        
        try:   
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) 
                    contract_address = CA.patient_contract_adress
                    ABI_PATH = 'build/contracts/PatientContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                 
                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)
                    account = self.wallet_address_pateint
                    result = contract.functions.getPatientInfo(account).call()
                    print(f"Doctor info: {result}")
                
                    full_name,gender,age, weight,height,blood_type,allergies,stored_hashed_password = result
         
        except Exception as e:
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")
      
       
        
        sing_up_label = ctk.CTkLabel(
            self.main_content3, 
            text="Update profil", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        sing_up_label.grid(row=0, column=0, columnspan=2, padx=(20, 70), pady=(10), sticky="w")

        
        # Define StringVar variables for all input fields
        full_name_var = ctk.StringVar()
        gender_var = ctk.StringVar()
        age_var = ctk.StringVar()
        weight_var = ctk.StringVar()
        height_var = ctk.StringVar()
        blood_type_var = ctk.StringVar()
        allergies_var = ctk.StringVar()

        full_name_var.set(full_name)
        gender_var.set(gender)
        age_var.set(age)
        weight_var.set(weight)
        height_var.set(height)
        blood_type_var.set(blood_type)
        allergies_var.set(allergies)


        # Full Name
        label_full_name = ctk.CTkLabel(
            self.main_content3, 
            text="Full Name:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_full_name.grid(row=2, column=0, padx=30, pady=10, sticky="w")

        entry_full_name = ctk.CTkEntry(
            self.main_content3, 
            width=300, 
            font=("Arial", 16),
            textvariable=full_name_var  # Bind to full_name_var
        )
        entry_full_name.grid(row=2, column=1, padx=10, pady=10)

        # Gender
        label_gender = ctk.CTkLabel(
            self.main_content3,
            text="Gender:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_gender.grid(row=3, column=0, padx=30, pady=10, sticky="w")

        combobox = ctk.CTkComboBox(
            self.main_content3, 
            values=["Male", "Female"],
            fg_color="white",
            text_color="black",
            dropdown_fg_color="white",
            border_color="grey",
            dropdown_text_color="black",
            button_color="grey",
            dropdown_hover_color="#1877F2",
            button_hover_color="#1877F2",
            variable=gender_var  # Bind to gender_var
        )
        combobox.set("Female")
        combobox.grid(row=3, column=1, padx=(10), pady=(5,5), sticky="ew")

        # Age
        label_age = ctk.CTkLabel(
            self.main_content3, 
            text="Age:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_age.grid(row=4, column=0, padx=30, pady=10, sticky="w")

        entry_age = ctk.CTkEntry(
            self.main_content3,
            width=300, 
            font=("Arial", 16),
            textvariable=age_var  # Bind to age_var
        )
        entry_age.grid(row=4, column=1, padx=10, pady=10)

        # Weight
        label_weight = ctk.CTkLabel(
            self.main_content3, 
            text="Weight (kg):", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_weight.grid(row=5, column=0, padx=30, pady=10, sticky="w")

        entry_weight = ctk.CTkEntry(
            self.main_content3, 
            width=300, 
            font=("Arial", 16),
            textvariable=weight_var  # Bind to weight_var
        )
        entry_weight.grid(row=5, column=1, padx=10, pady=10)

        # Height
        label_height = ctk.CTkLabel(
            self.main_content3,
            text="Height (cm):", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_height.grid(row=6, column=0, padx=30, pady=10, sticky="w")

        entry_height = ctk.CTkEntry(
            self.main_content3, 
            width=300, 
            font=("Arial", 16),
            textvariable=height_var  # Bind to height_var
        )
        entry_height.grid(row=6, column=1, padx=10, pady=10)

        # Blood Type
        label_blood_type = ctk.CTkLabel(
            self.main_content3,
            text="Blood Type:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_blood_type.grid(row=7, column=0, padx=30, pady=10, sticky="w")

        entry_blood_type = ctk.CTkEntry(
            self.main_content3,
            width=300, 
            font=("Arial", 16),
            textvariable=blood_type_var  # Bind to blood_type_var
        )
        entry_blood_type.grid(row=7, column=1, padx=10, pady=10)

        # Allergies
        label_allergies = ctk.CTkLabel(
            self.main_content3, 
            text="Allergies:", 
            fg_color="#E1EBEE", 
            font=("Arial", 18, "bold"),
            text_color="black"
        )
        label_allergies.grid(row=8, column=0, padx=30, pady=10, sticky="w")

        entry_allergies = ctk.CTkEntry(
            self.main_content3, 
            width=300, 
            font=("Arial", 16),
            textvariable=allergies_var  # Bind to allergies_var
        )
        entry_allergies.grid(row=8, column=1, padx=10, pady=10)



        
        def edit_Patient( full_name,gender,age, weight,height,blood_type,allergies):
                try:
            
                    w3 = Web3(Web3.HTTPProvider('http://localhost:8545')) # Update with your RPC provider

                    # Smart contract details
                    contract_address = CA.patient_contract_adress
                    ABI_PATH = 'build/contracts/PatientContract.json'
                    if not os.path.exists(ABI_PATH):
                        raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                    with open(ABI_PATH, 'r') as abi_file:
                        contract_abi = json.load(abi_file)['abi']
                    

                 
                    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

                    account = self.wallet_address_pateint

                    tx_hash = contract.functions.updatePatientDetails(full_name,gender,age, weight,height,blood_type,allergies,account).transact({
                            'from': account
                        })

                    w3.eth.wait_for_transaction_receipt(tx_hash)

                    print(f"Patient successfully updated .")
                   
                    
                    messagebox.showinfo("Success", f"Profil successfully updated.")
                    self.View_profile_Patient()
                except Exception as e:
                    
                    messagebox.showerror("Error", f"Transaction failed: {str(e)}")
        def button_event():

            print("Form submitted")
            
            full_name = entry_full_name.get()
            gender = combobox.get()
            age = entry_age.get()
            try:
                age = int(age)
            except ValueError:
                messagebox.showerror("Error","Invalid age input, please enter a valid number.")
                return
            weight = entry_weight.get()
            try:
                weight = int(weight)
            except ValueError:
                messagebox.showerror("Error","Invalid weight input, please enter a valid number.")
                return
            height = entry_height.get()
            try:
                height = int(height)
            except ValueError:
                messagebox.showerror("Error","Invalid height input, please enter a valid number.")
                return
            blood_type = entry_blood_type.get()
            allergies = entry_allergies.get()
           
            if not all([full_name,gender,age, weight,height,blood_type,allergies]):
                messagebox.showerror("Error", "All fields are required.")
            else:
                edit_Patient(full_name,gender,age, weight,height,blood_type,allergies)
                print(full_name,gender,age, weight,height,blood_type,allergies)

        button = ctk.CTkButton(self.main_content3, text="Submit", command=button_event)
        button.grid(row=10, column=1, padx=(170, 0), pady=(10), sticky="w")


        
    


    def Add_patient_record(self):
        # Clear existing widgets
        for widget in self.main_content3.winfo_children():
            widget.destroy()

        # Title Label
        sing_up_label = ctk.CTkLabel(
            self.main_content3, 
            text="Add Medical Record", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        sing_up_label.grid(row=0, column=0, columnspan=2, padx=(20,70), pady=(30), sticky="w")

        # Variable to store file path
        self.file_path_var = ctk.StringVar()

        # Select File Button
        def select_file():
            file_path = filedialog.askopenfilename(
                title="Select Medical Record",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
            )
            if file_path:
                self.file_path_var.set(file_path)
                file_label.configure(text=f"Selected: {file_path.split('/')[-1]}")

        select_file_button = ctk.CTkButton(
            self.main_content3,
            text="Select File",
            command=select_file,
            font=("Arial", 16),
            fg_color="#1877F2",
            text_color="white"
        )
        select_file_button.grid(row=1, column=0, padx=(20, 10), pady=(10), sticky="w")

        # File Label
        file_label = ctk.CTkLabel(
            self.main_content3,
            text="No file selected",
            font=("Arial", 16),
            text_color="black"
        )
        file_label.grid(row=1, column=1, padx=(10, 20), pady=(10), sticky="w")

    
        def upload_to_ipfs(file_path):
            try:
                # Check if the file exists before proceeding
                if not os.path.isfile(file_path):
                    print(f"Error: File {file_path} does not exist.")
                    return None

                # Read the file content and upload to local IPFS node
                with open(file_path, "rb") as f:
                    response = requests.post("http://127.0.0.1:5001/api/v0/add", files={"file": f})

                    # Check if the request was successful
                    response.raise_for_status()

                    # Get the IPFS hash from the response
                    ipfs_hash = response.json().get("Hash")
                    if ipfs_hash:
                        print(f"Uploaded to IPFS: {ipfs_hash}")
                    else:
                        print("Error: IPFS Hash not found in the response.")
                        return None
                contract_address = CA.patient_contract_adress
                ABI_PATH = 'build/contracts/PatientContract.json'
                # Check if ABI file exists
                if not os.path.exists(ABI_PATH):
                    raise FileNotFoundError(f"ABI file not found at {ABI_PATH}. Ensure the file exists.")

                # Load contract ABI
                with open(ABI_PATH, 'r') as abi_file:
                    contract_abi = json.load(abi_file)['abi']

                wallet_address = self.wallet_address_pateint
                contract = w3.eth.contract(address=contract_address, abi=contract_abi)

                # Prepare the transaction to add medical record
                tx_hash = contract.functions.addMedicalRecord(wallet_address, ipfs_hash).transact({
                    'from': wallet_address
                })

                # Wait for the transaction receipt
                w3.eth.wait_for_transaction_receipt(tx_hash)

                # Fetch patient records after the transaction
                result = contract.functions.getPatientRecords(wallet_address, wallet_address).call()
                print(f"Record info: {result}")

                return ipfs_hash

            except requests.exceptions.RequestException as e:
                print(f"Error uploading to IPFS: {e}")
                return None
            except FileNotFoundError as e:
                print(f"Error: {e}")
                return None
            except Exception as e:
                print(f"An error occurred: {e}")
                return None

        def upload_file():
            file_path = self.file_path_var.get()
            if not file_path:
                error_label.configure(text="Please select a file!")
                return

            # Upload file to IPFS
            ipfs_hash = upload_to_ipfs(file_path)
            if ipfs_hash:
                success_label.configure(text=f"Uploaded to IPFS: {ipfs_hash}")
                download_button.configure(state="normal")
                self.ipfs_hash = ipfs_hash  # Save IPFS hash
            else:
                error_label.configure(text="Failed to upload to IPFS")

        upload_button = ctk.CTkButton(
            self.main_content3,
            text="Upload to IPFS",
            command=upload_file,
            font=("Arial", 16),
            fg_color="#1877F2",
            text_color="white"
        )
        upload_button.grid(row=2, column=0, padx=(20, 10), pady=(10), sticky="w")

        # Success/Error Labels
        success_label = ctk.CTkLabel(
            self.main_content3,
            text="",
            font=("Arial", 16),
            text_color="green"
        )
        success_label.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(10), sticky="w")

        error_label = ctk.CTkLabel(
            self.main_content3,
            text="",
            font=("Arial", 16),
            text_color="red"
        )
        error_label.grid(row=4, column=0, columnspan=2, padx=(20, 20), pady=(10), sticky="w")

        def open_in_browser():
            if hasattr(self, 'ipfs_hash'):

                url = f"http://127.0.0.1:8080/ipfs/{self.ipfs_hash}"
                webbrowser.open(url)

        download_button = ctk.CTkButton(
            self.main_content3,
            text="View File",
            command=open_in_browser,
            font=("Arial", 16),
            fg_color="#1877F2",
            text_color="white",
            state="disabled"  
        )
        download_button.grid(row=5, column=0, padx=(20, 10), pady=(10), sticky="w")


    def View_patient(self):
        # Clear the main content area
        for widget in self.main_content3.winfo_children():
            widget.destroy()

        # Add a form for Register Doctor

        sing_up_label = ctk.CTkLabel(
            self.main_content3, 
            text="Patient's Record", 
            font=("Arial", 30, "bold"), 
            fg_color="#E1EBEE", 
            text_color="black", 
            corner_radius=10
        )
        sing_up_label.grid(row=0, column=0, columnspan=2, padx=(20,70), pady=(30), sticky="w")


root = ctk.CTk()
app = App(root)
root.mainloop()
