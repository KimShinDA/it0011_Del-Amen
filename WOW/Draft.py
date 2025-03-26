# Import library: tkinter
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext # Importing necessary modules

"""
    This program is a simple record management system that allows users to sign-up, view records, search for records, and exit the program.
    The program is implemented using the Tkinter library in Python.
    The program is divided into six classes that handle different functionalities:
        1. RecordChecker: Handles record-related operations such as counting existing records and checking if records exist.
        2. SignUpForm: Handles the sign-up process.
        3. ViewRecords: Handles viewing of records.
        4. SearchRecord: Handles searching for records.
        5. ConfirmExit: Handles the exit confirmation.
        6. RecordLogsGUI: Main GUI class that integrates all functionalities.

    Take note that the records are stored in a text file named "records.txt".
"""

# Handles record-related operations such as counting existing records and checking if records exist.
class RecordChecker:
    
    # Initialize the file name
    def __init__(self, file_name="records.txt"):
        self.file_name = file_name

    # Counts the number of existing records in the file
    def count_existing_records(self):
        try:
            with open(self.file_name, "r") as file:
                content = file.read().strip()
            return content.count("Record #")
        except FileNotFoundError:
            return 0

    # Checks if records exist in the file
    def records_exist(self):
        return self.count_existing_records() > 0

# Handles the sign-up process.
class SignUpForm:
    
    # Initialize the root and record manager
    def __init__(self, root, record_manager):
        self.root = root
        self.record_manager = record_manager

    # Opens the sign-up window
    def open_signup_window(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign-Up Form")
        signup_window.geometry("500x500")
        signup_window.configure(bg="#ffffff")
        signup_window.resizable(False, False)

        # Header Frame
        header_frame = tk.Frame(signup_window, bg="#2ecc71")
        header_frame.pack(fill="x", pady=(0, 20))

        # Header Label
        tk.Label(
            header_frame, 
            text="Sign-Up Form", 
            font=("Arial", 16, "bold"), 
            bg="#2ecc71", 
            fg="white",
            padx=20,
            pady=10
        ).pack()

        # Form Frame
        form_frame = tk.Frame(signup_window, bg="#ffffff")
        form_frame.pack(padx=30, pady=30)

        # Form Fields (Text Fields)
        fields = ["First Name", "Middle Name", "Last Name"]
        entries = {}

        # Create form fields
        for i, field in enumerate(fields):
            tk.Label(
                form_frame, 
                text=field + ":", 
                bg="#ffffff",
                font=("Arial", 10),
                anchor="w"
            ).grid(row=i, column=0, pady=5, sticky="w")
            
            entries[field] = tk.Entry(
                form_frame, 
                font=("Arial", 10),
                bd=1,
                relief=tk.SOLID,
                highlightthickness=1,
                highlightbackground="#bdc3c7",
                highlightcolor="#3498db"
            )
            entries[field].grid(row=i, column=1, pady=5, ipady=5, sticky="ew")
            
        # Birthday Field
        birthday_row = len(fields)

        tk.Label(
            form_frame, 
            text="Birthday:", 
            bg="#ffffff",
            font=("Arial", 10),
            anchor="w"
        ).grid(row=birthday_row, column=0, pady=5, sticky="w")

        birthday_frame = tk.Frame(form_frame, bg="#ffffff")
        birthday_frame.grid(row=birthday_row, column=1, pady=5, sticky="w")

        # Month Dropdown
        months = [""] + [f"{i:02d}" for i in range(1, 13)]
        month_var = tk.StringVar(value="")
        month_menu = ttk.Combobox(birthday_frame, textvariable=month_var, values=months, width=5, state="readonly")
        month_menu.pack(side="left", padx=2)

        # Day Dropdown
        days = [""] + [f"{i:02d}" for i in range(1, 32)]
        day_var = tk.StringVar(value="")
        day_menu = ttk.Combobox(birthday_frame, textvariable=day_var, values=days, width=5, state="readonly")
        day_menu.pack(side="left", padx=2)

        # Year Dropdown
        years = [""] + [str(y) for y in range(1900, 2026)]
        year_var = tk.StringVar(value="")
        year_menu = ttk.Combobox(birthday_frame, textvariable=year_var, values=years, width=6, state="readonly")
        year_menu.pack(side="left", padx=2)

        # Store dropdowns in entries dictionary
        entries["Birthday"] = (month_var, day_var, year_var)

        # Gender Field
        gender_row = birthday_row + 1

        tk.Label(
            form_frame, 
            text="Gender:", 
            bg="#ffffff",
            font=("Arial", 10),
            anchor="w"
        ).grid(row=gender_row, column=0, pady=5, sticky="w")

        gender_frame = tk.Frame(form_frame, bg="#ffffff")
        gender_frame.grid(row=gender_row, column=1, pady=5, sticky="w")

        gender_var = tk.StringVar(value="0")  

        tk.Radiobutton(
            gender_frame,
            text="Male",
            variable=gender_var,
            value="M",
            bg="#ffffff",
            font=("Arial", 10)
        ).pack(side="left", padx=(0, 10))

        tk.Radiobutton(
            gender_frame,
            text="Female",
            variable=gender_var,
            value="F",
            bg="#ffffff",
            font=("Arial", 10)
        ).pack(side="left")

        entries["Gender"] = gender_var

        # Save Record Function
        def save_record():
            data = {field: entries[field].get().strip() for field in fields} # Get form data
            data["Gender"] = gender_var.get() 

            # Validate birthday field
            if "Birthday" in entries:
                month_var, day_var, year_var = entries["Birthday"]
                data["Birthday"] = f"{month_var.get()}-{day_var.get()}-{year_var.get()}"
            else:
                messagebox.showerror("Error", "Birthday field is missing!")
                return

            # Validate form fields
            # Note that Middle Name is optional as it can be empty
            if not data["First Name"] or not data["Last Name"]:
                messagebox.showerror("Error", "First and Last Name are required.")
                return
            
            # Gender validation
            gender = data["Gender"].upper()
            gender_full = "Male" if gender == "M" else "Female"
            
            record_number = self.record_manager.count_existing_records() + 1 # Get record number
            unique_id = "2025" + str(record_number).zfill(5) # Generate unique ID starting with 2025 and padded with zeros to 5 digits

            # Save record to file
            with open(self.record_manager.file_name, "a") as file:
                file.write(f"\nRecord #{record_number}\n")
                file.write(f"ID: {unique_id}\n")
                file.write(f"Name: {data['First Name']} {data['Middle Name']} {data['Last Name']}\n")
                file.write(f"Birthday: {data['Birthday']}\n") 
                file.write(f"Gender: {gender_full}\n")

            messagebox.showinfo("Success", f"Record saved!\nID: {unique_id}")
            signup_window.destroy()

        # Button Frame
        button_frame = tk.Frame(signup_window, bg="#ffffff")
        button_frame.pack(pady=20)

        # Save and Cancel Buttons
        save_button = tk.Button(
            button_frame, 
            text="Save Record", 
            command=save_record, 
            bg="#2ecc71", 
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5,
            relief=tk.RAISED,  
            highlightthickness=0,
            bd=1,  
            highlightbackground="#cccccc", 
            highlightcolor="#333333"
        )
        save_button.pack(side="left", padx=10)

        cancel_button = tk.Button(
            button_frame, 
            text="Cancel", 
            command=signup_window.destroy, 
            bg="#95a5a6", 
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5,
            relief=tk.RAISED,  
            highlightthickness=0,
            bd=1,  
            highlightbackground="#cccccc", 
            highlightcolor="#333333"
        )
        cancel_button.pack(side="left", padx=10)

        # Hover Effects for Buttons 
        save_button.bind("<Enter>", lambda e: save_button.config(bg="#27ae60"))
        save_button.bind("<Leave>", lambda e: save_button.config(bg="#2ecc71"))
        cancel_button.bind("<Enter>", lambda e: cancel_button.config(bg="#7f8c8d"))
        cancel_button.bind("<Leave>", lambda e: cancel_button.config(bg="#95a5a6"))

# Handles viewing of records.
class ViewRecords:
    
    # Initialize the root and record manager
    def __init__(self, root, record_manager):
        self.root = root
        self.record_manager = record_manager

    # Opens the view window
    def open_view_window(self):
        if not self.record_manager.records_exist():
            messagebox.showwarning("No Records", "No records found. Please sign-up first.")
            return

        view_window = tk.Toplevel(self.root)
        view_window.title("View Records")
        view_window.geometry("700x600")
        view_window.configure(bg="#ffffff")

        # Header Frame
        header_frame = tk.Frame(view_window, bg="#3498db")
        header_frame.pack(fill="x")

        # Header Label
        tk.Label(
            header_frame, 
            text="All Records", 
            font=("Arial", 14, "bold"), 
            bg="#3498db", 
            fg="white",
            padx=20,
            pady=10
        ).pack()

        # Text Frame
        text_frame = tk.Frame(view_window, bg="#ffffff")
        text_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Text Area
        text_area = scrolledtext.ScrolledText(
            text_frame, 
            width=80, 
            height=25,
            font=("Consolas", 10),
            wrap=tk.WORD,
            bd=1,
            relief=tk.SOLID
        )
        text_area.pack(expand=True, fill="both")

        # Load records to text area
        with open(self.record_manager.file_name, "r") as file:
            text_area.insert(tk.END, file.read().strip())

        text_area.config(state=tk.DISABLED) # Disable editing

# Handles searching for records.
class SearchRecord:
    
    # Initialize the root and record manager
    def __init__(self, root, record_manager):
        self.root = root
        self.record_manager = record_manager

    # Opens the search window
    def open_search_window(self):
        if not self.record_manager.records_exist():
            messagebox.showwarning("No Records", "No records found. Please sign-up first.")
            return

        search_window = tk.Toplevel(self.root)
        search_window.title("Search Record")
        search_window.geometry("500x400")
        search_window.configure(bg="#ffffff")
        search_window.resizable(False, False)

        # Header Frame
        header_frame = tk.Frame(search_window, bg="#f39c12")
        header_frame.pack(fill="x")

        # Header Label
        tk.Label(
            header_frame, 
            text="Search Record", 
            font=("Arial", 14, "bold"), 
            bg="#f39c12", 
            fg="white",
            padx=20,
            pady=10
        ).pack()

        search_frame = tk.Frame(search_window, bg="#ffffff")
        search_frame.pack(pady=20, padx=30)

        tk.Label(
            search_frame, 
            text="Enter ID to search:", 
            font=("Arial", 10),
            bg="#ffffff"
        ).grid(row=0, column=0, sticky="w")

        # Search Entry
        search_entry = tk.Entry(
            search_frame, 
            width=30,
            font=("Arial", 10),
            bd=1,
            relief=tk.SOLID
        )
        search_entry.grid(row=1, column=0, pady=5, sticky="ew")

        # Search Button
        search_button = tk.Button(
            search_frame, 
            text="Search", 
            command=lambda: self.perform_search(search_entry, result_text),
            bg="#f39c12", 
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5,
            relief=tk.RAISED,  
            highlightthickness=0,
            bd=1,  
            highlightbackground="#cccccc", 
            highlightcolor="#333333"
        )
        search_button.grid(row=1, column=1, padx=10)

        # Result Frame
        result_frame = tk.Frame(search_window, bg="#ffffff")
        result_frame.pack(expand=True, fill="both", padx=30, pady=(0, 20))

        # Result Text Area
        result_text = scrolledtext.ScrolledText(
            result_frame, 
            width=60, 
            height=10,
            font=("Consolas", 10),
            wrap=tk.WORD,
            bd=1,
            relief=tk.SOLID
        )
        result_text.pack(expand=True, fill="both")

        # Hover Effects for Search Button
        search_button.bind("<Enter>", lambda e: search_button.config(bg="#e67e22"))
        search_button.bind("<Leave>", lambda e: search_button.config(bg="#f39c12"))

    # Perform search operation
    def perform_search(self, search_entry, result_text):
        search_id = search_entry.get().strip() # Get search ID
        if not search_id:
            messagebox.showerror("Error", "Please enter an ID to search.")
            return
        
        # Error handling for file operations
        # If an error occurs, show an error message
        # Otherwise, search for the record with the given ID
        try:
            with open(self.record_manager.file_name, "r") as file:
                records = file.read()
            
            found = False
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            
            for record in records.split("Record #"):
                if search_id in record:
                    result_text.insert(tk.END, f"Record #{record.strip()}\n\n")
                    found = True
                    
            if not found:
                result_text.insert(tk.END, f"No records found with ID: {search_id}")
                
            result_text.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Handles the exit confirmation.
class ConfirmExit:
    
    # Initialize the root
    def __init__(self, root):
        self.root = root

    # Confirm exit function
    def confirm_exit(self):
        response = messagebox.askyesno("Exit Confirmation", "Do you want to exit the program?")
        if response:  
            messagebox.showinfo("Goodbye!", "Thank you for using our program!")
            self.root.quit()

# Main GUI class that integrates all functionalities.
class RecordLogsGUI:
    
    # Initialize the root and create instances of other classes
    def __init__(self, root):
        self.root = root
        self.root.title("Record Management System")
        self.root.geometry("420x300")
        self.root.configure(bg="#f0f2f5")

        # Initialize other classes
        self.record_manager = RecordChecker()
        self.sign_up = SignUpForm(self.root, self.record_manager)
        self.view_records = ViewRecords(self.root, self.record_manager)
        self.search_record = SearchRecord(self.root, self.record_manager)
        self.confirm_exit = ConfirmExit(self.root)

        # Main Frame
        self.main_frame = tk.Frame(root, bg="#f0f2f5", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")

        # Header Section 
        self.header_frame = tk.Frame(self.main_frame, bg="#f0f2f5")
        self.header_frame.pack(fill="x", pady=(0, 20))

        self.label = tk.Label(
            self.header_frame, 
            text="Record Management System", 
            font=("Arial", 20, "bold"), 
            bg="#f0f2f5", 
            fg="#2c3e50"
        )
        self.label.pack(side="left")

        ttk.Separator(self.main_frame, orient="horizontal").pack(fill="x", pady=5)

        # Button Frame
        self.button_frame = tk.Frame(self.main_frame, bg="#f0f2f5")
        self.button_frame.pack(pady=20)

        # Button Style 
        button_style = {
            "font": ("Arial", 12, "bold"),
            "bd": 0,
            "width": 15,
            "height": 2,
            "compound": "center",
            "relief": tk.RAISED,  
            "highlightthickness": 0,
            "bd": 1,  
            "highlightbackground": "#cccccc", 
            "highlightcolor": "#333333"  
        }

        # Create buttons grid 
        self.btn_signup = tk.Button(
            self.button_frame, 
            text="Sign-up", 
            command=self.sign_up.open_signup_window, 
            bg="#2ecc71", 
            fg="white",
            **button_style
        )
        self.btn_view = tk.Button(
            self.button_frame, 
            text="View All Records", 
            command=self.view_records.open_view_window, 
            bg="#3498db", 
            fg="white",
            **button_style
        )
        self.btn_search = tk.Button(
            self.button_frame, 
            text="Search Record", 
            command=self.search_record.open_search_window, 
            bg="#f39c12", 
            fg="white",
            **button_style
        )
        self.btn_exit = tk.Button(
            self.button_frame, 
            text="Exit", 
            command=self.confirm_exit.confirm_exit,
            bg="#e74c3c", 
            fg="white",
            **button_style
        )

        # Button Layout
        self.btn_signup.grid(row=1, column=0, pady=5, padx=5)
        self.btn_view.grid(row=1, column=1, pady=5, padx=5)
        self.btn_search.grid(row=2, column=0, pady=5, padx=5)
        self.btn_exit.grid(row=2, column=1, pady=5, padx=5)

        # Hover Effects
        def on_enter(e, button, hover_color):
            button['background'] = hover_color
            button['relief'] = tk.SUNKEN

        def on_leave(e, button, original_color):
            button['background'] = original_color
            button['relief'] = tk.RAISED

        # Bind hover effects
        self.btn_signup.bind("<Enter>", lambda e: on_enter(e, self.btn_signup, "#27ae60"))
        self.btn_signup.bind("<Leave>", lambda e: on_leave(e, self.btn_signup, "#2ecc71"))
        self.btn_view.bind("<Enter>", lambda e: on_enter(e, self.btn_view, "#2980b9"))
        self.btn_view.bind("<Leave>", lambda e: on_leave(e, self.btn_view, "#3498db"))
        self.btn_search.bind("<Enter>", lambda e: on_enter(e, self.btn_search, "#e67e22"))
        self.btn_search.bind("<Leave>", lambda e: on_leave(e, self.btn_search, "#f39c12"))
        self.btn_exit.bind("<Enter>", lambda e: on_enter(e, self.btn_exit, "#c0392b"))
        self.btn_exit.bind("<Leave>", lambda e: on_leave(e, self.btn_exit, "#e74c3c"))

# Main function
# Create the root window and the RecordLogsGUI instance
if __name__ == "__main__":
    root = tk.Tk()
    app = RecordLogsGUI(root)
    root.mainloop()