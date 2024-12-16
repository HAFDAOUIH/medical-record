import customtkinter
from PIL import Image, ImageTk

# Initialize the app
customtkinter.set_appearance_mode("Light")  # Modes: "System", "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Create the main application window
app = customtkinter.CTk()
app.geometry("600x600")
app.title("Hospital Management System")

# Load a hospital logo or use a placeholder (Optional)
try:
    hospital_logo = Image.open(r"C:\Users\Hanane\Desktop\medical-record\frontend\img\hospitalLogo.png")  # Replace with your logo file
    hospital_logo = hospital_logo.resize((120, 120), Image.Resampling.LANCZOS)
    logo_image = ImageTk.PhotoImage(hospital_logo)
except FileNotFoundError:
    logo_image = None

# Define button callbacks
def register_admin():
    print("Register Admin button clicked")

def log_in():
    print("Log In button clicked")

# Add a header with a logo (if available)
header_frame = customtkinter.CTkFrame(app, fg_color="lightblue", corner_radius=0)
header_frame.pack(fill="x")

if logo_image:
    logo_label = customtkinter.CTkLabel(header_frame, image=logo_image, text="")
    logo_label.pack(side="left", padx=10, pady=10)

header_text = customtkinter.CTkLabel(header_frame, text="Hospital Management System", 
                                     font=("Arial", 24, "bold"), text_color="darkblue")
header_text.pack(side="left", padx=20)

# Create a main frame for buttons
main_frame = customtkinter.CTkFrame(app)
main_frame.pack(pady=50, padx=20, fill="both", expand=True)

welcome_label = customtkinter.CTkLabel(main_frame, text="Welcome! Please choose an option below:", 
                                       font=("Arial", 18), text_color="black")
welcome_label.pack(pady=20)

# Add Register Admin button
register_button = customtkinter.CTkButton(main_frame, text="Register Admin", 
                                          command=register_admin, 
                                          font=("Arial", 16), 
                                          fg_color="royalblue", 
                                          hover_color="skyblue", 
                                          width=200, height=50)
register_button.pack(pady=10)

# Add Log In button
login_button = customtkinter.CTkButton(main_frame, text="Log In", 
                                       command=log_in, 
                                       font=("Arial", 16), 
                                       fg_color="dodgerblue", 
                                       hover_color="lightblue", 
                                       width=200, height=50)
login_button.pack(pady=10)

# Add footer
footer_frame = customtkinter.CTkFrame(app, fg_color="lightgray", corner_radius=0)
footer_frame.pack(fill="x", side="bottom")

footer_text = customtkinter.CTkLabel(footer_frame, text="© 2024 Hospital Management System", 
                                     font=("Arial", 12), text_color="gray")
footer_text.pack(pady=5)

# Run the application
app.mainloop()
