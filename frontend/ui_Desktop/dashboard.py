import customtkinter as ctk
from tkinter import ttk


class AuditLogApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Audit Log Viewer")
        self.geometry("800x600")
        self.configure(bg="gray90")

        # Header
        self.header_label = ctk.CTkLabel(self, text="Audit Logs", font=("Arial", 24, "bold"))
        self.header_label.pack(pady=20)

        # Log Display Frame
        self.log_frame = ctk.CTkFrame(self)
        self.log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Use ttk.Treeview for the table
        self.tree = ttk.Treeview(
            self.log_frame,
            columns=("Actor", "Subject", "Action", "Timestamp"),
            show="headings",
        )
        self.tree.heading("Actor", text="Actor")
        self.tree.heading("Subject", text="Subject")
        self.tree.heading("Action", text="Action")
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.pack(fill="both", expand=True)

        # Add scrollbars for the Treeview
        scrollbar_y = ctk.CTkScrollbar(self.log_frame, orientation="vertical", command=self.tree.yview)
        scrollbar_y.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar_y.set)

        # Fetch Button
        self.fetch_button = ctk.CTkButton(self, text="Fetch Logs", command=self.fetch_logs)
        self.fetch_button.pack(pady=20)

    def fetch_logs(self):
        # Placeholder for fetching logic
        # Replace this with the Web3 code to fetch logs
        print("Fetching logs... (Implement fetch logic here)")
        # Example of inserting dummy data
        self.tree.insert("", "end", values=("0xActorAddress", "0xSubjectAddress", "Sample Action", "2024-12-16 12:00:00"))


# Run the application
if __name__ == "__main__":
    app = AuditLogApp()
    app.mainloop()
