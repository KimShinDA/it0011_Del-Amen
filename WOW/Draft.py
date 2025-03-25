import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class RecordLogsGUI:
    def __init__(self, root, file_name="records.txt"):
        self.root = root
        self.root.title("Record Management System")
        self.root.geometry("420x300")
        self.root.configure(bg="#f0f2f5")
        self.records_inputs = file_name

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
            command=self.sign_up, 
            bg="#2ecc71", 
            fg="white",
            **button_style
        )
        self.btn_view = tk.Button(
            self.button_frame, 
            text="View All Records", 
            command=self.view_records, 
            bg="#3498db", 
            fg="white",
            **button_style
        )
        self.btn_search = tk.Button(
            self.button_frame, 
            text="Search Record", 
            command=self.search_record, 
            bg="#f39c12", 
            fg="white",
            **button_style
        )
        self.btn_exit = tk.Button(
            self.button_frame, 
            text="Exit", 
            command=root.quit, 
            bg="#e74c3c", 
            fg="white",
            **button_style
        )

        # Button Layout - nilagay ko ulit yung code mo te para same format yan sila
        self.btn_signup.grid(row=1, column=0, pady=5, padx=5)
        self.btn_view.grid(row=1, column=1, pady=5, padx=5)
        self.btn_search.grid(row=2, column=0, pady=5, padx=5)
        self.btn_exit.grid(row=2, column=1, pady=5, padx=5)

        # Hover Effects para lang masaya. Mas mahaba lang here kasi may on enter and leave pang nalalaman eme
        def on_enter(e, button, hover_color):
            button['background'] = hover_color
            button['relief'] = tk.SUNKEN

        def on_leave(e, button, original_color):
            button['background'] = original_color
            button['relief'] = tk.RAISED

        # dagdag lang din na hover kasi ulit ulit lang color na lang and name papalitan
        self.btn_signup.bind("<Enter>", lambda e: on_enter(e, self.btn_signup, "#27ae60"))
        self.btn_signup.bind("<Leave>", lambda e: on_leave(e, self.btn_signup, "#2ecc71"))
        self.btn_view.bind("<Enter>", lambda e: on_enter(e, self.btn_view, "#2980b9"))
        self.btn_view.bind("<Leave>", lambda e: on_leave(e, self.btn_view, "#3498db"))
        self.btn_search.bind("<Enter>", lambda e: on_enter(e, self.btn_search, "#e67e22"))
        self.btn_search.bind("<Leave>", lambda e: on_leave(e, self.btn_search, "#f39c12"))
        self.btn_exit.bind("<Enter>", lambda e: on_enter(e, self.btn_exit, "#c0392b"))
        self.btn_exit.bind("<Leave>", lambda e: on_leave(e, self.btn_exit, "#e74c3c"))
        
        
    # nothing change
    def count_existing_records(self):
        try:
            with open(self.records_inputs, "r") as file:
                content = file.read().strip()
            return content.count("Record #")
        except FileNotFoundError:
            return 0

    def records_exist(self):
        return self.count_existing_records() > 0

    def sign_up(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign-Up Form")
        signup_window.geometry("500x500")
        signup_window.configure(bg="#ffffff")
        signup_window.resizable(False, False)

        # Header kasi why not, dagdag aesthetic 
        header_frame = tk.Frame(signup_window, bg="#3498db")
        header_frame.pack(fill="x", pady=(0, 20))

        tk.Label(
            header_frame, 
            text="Sign-Up Form", 
            font=("Arial", 16, "bold"), 
            bg="#3498db", 
            fg="white",
            padx=20,
            pady=10
        ).pack()

        # Form Frame para maganda
        form_frame = tk.Frame(signup_window, bg="#ffffff")
        form_frame.pack(padx=30, pady=30)

        fields = ["First Name", "Middle Name", "Last Name", "Birthday (MM-DD-YYYY)"]
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(
                form_frame, 
                text=field+":", 
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
            
        tk.Label(
            form_frame, 
            text="Gender:", 
            bg="#ffffff",
            font=("Arial", 10),
            anchor="w"
        ).grid(row=len(fields), column=0, pady=5, sticky="w")

        gender_frame = tk.Frame(form_frame, bg="#ffffff")
        gender_frame.grid(row=len(fields), column=1, pady=5, sticky="w")

        # Variable lang pang-hold gender selection
        gender_var = tk.StringVar(value="F")  # DEFAULT LANG SA FEMALE KASI BABAE GUMAWA NUNG CODE 

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

        entries["Gender"] = gender_var

        def validate_birthday(birthday):
            if len(birthday) != 10 or birthday[2] != '-' or birthday[5] != '-':
                return False

            month, day, year = birthday.split('-')

            if not (month.isdigit() and day.isdigit() and year.isdigit()):
                return False

            month, day, year = int(month), int(day), int(year)

            if year < 1900 or year > 2025:
                return False
            
            if month < 1 or month > 12:
                return False

            days_in_month = {
                1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
            }

            if day < 1 or day > days_in_month[month]:
                return False

            return True
        # itu te nananalig akong gets mo na sya kasi galing yan sayo
        def save_record():
            data = {field: entries[field].get().strip() for field in fields}
            data["Gender"] = gender_var.get()

            if not data["First Name"] or not data["Last Name"]:
                messagebox.showerror("Error", "First and Last Name are required.")
                return

            if not validate_birthday(data["Birthday (MM-DD-YYYY)"]):
                messagebox.showerror("Error", "Invalid Birthday. Use MM-DD-YYYY and enter a real date.")
                return

            gender = data["Gender"].upper()
            if gender not in ("M", "F"):
                messagebox.showerror("Error", "Gender must be 'M' for Male or 'F' for Female.")
                return

            gender_full = "Male" if gender == "M" else "Female"

            record_number = self.count_existing_records() + 1
            unique_id = "2025" + str(record_number).zfill(5)

            with open(self.records_inputs, "a") as file:
                file.write(f"\nRecord #{record_number}\n")
                file.write(f"ID: {unique_id}\n")
                file.write(f"Name: {data['First Name']} {data['Middle Name']} {data['Last Name']}\n")
                file.write(f"Birthday: {data['Birthday (MM-DD-YYYY)']}\n")
                file.write(f"Gender: {gender_full}\n")

            messagebox.showinfo("Success", f"Record saved!\nID: {unique_id}")
            signup_window.destroy()

        # Button Frame
        button_frame = tk.Frame(signup_window, bg="#ffffff")
        button_frame.pack(pady=20)

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

        #para ma-prevent ang mga pagkakamali
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

        save_button.bind("<Enter>", lambda e: save_button.config(bg="#27ae60"))
        save_button.bind("<Leave>", lambda e: save_button.config(bg="#2ecc71"))
        cancel_button.bind("<Enter>", lambda e: cancel_button.config(bg="#7f8c8d"))
        cancel_button.bind("<Leave>", lambda e: cancel_button.config(bg="#95a5a6"))

    #tapos ulit ulit na lang
    def view_records(self):
        if not self.records_exist():
            messagebox.showwarning("No Records", "No records found. Please sign-up first.")
            return

        view_window = tk.Toplevel(self.root)
        view_window.title("View Records")
        view_window.geometry("700x600")
        view_window.configure(bg="#ffffff")

        header_frame = tk.Frame(view_window, bg="#3498db")
        header_frame.pack(fill="x")

        tk.Label(
            header_frame, 
            text="All Records", 
            font=("Arial", 14, "bold"), 
            bg="#3498db", 
            fg="white",
            padx=20,
            pady=10
        ).pack()

        text_frame = tk.Frame(view_window, bg="#ffffff")
        text_frame.pack(expand=True, fill="both", padx=20, pady=20)

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

        with open(self.records_inputs, "r") as file:
            text_area.insert(tk.END, file.read().strip())

        text_area.config(state=tk.DISABLED)

    def search_record(self):
        if not self.records_exist():
            messagebox.showwarning("No Records", "No records found. Please sign-up first.")
            return

        search_window = tk.Toplevel(self.root)
        search_window.title("Search Record")
        search_window.geometry("500x400")
        search_window.configure(bg="#ffffff")
        search_window.resizable(False, False)

        header_frame = tk.Frame(search_window, bg="#f39c12")
        header_frame.pack(fill="x")

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

        search_entry = tk.Entry(
            search_frame, 
            width=30,
            font=("Arial", 10),
            bd=1,
            relief=tk.SOLID
        )
        search_entry.grid(row=1, column=0, pady=5, sticky="ew")

        search_button = tk.Button(
            search_frame, 
            text="Search", 
            command=lambda: self.perform_search(search_entry, result_text),
            bg="#f39c12", 
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5,
            relief = tk.RAISED,  
            highlightthickness = 0,
            bd = 1,  
            highlightbackground ="#cccccc", 
            highlightcolor = "#333333"
        )
        search_button.grid(row=1, column=1, padx=10)

        result_frame = tk.Frame(search_window, bg="#ffffff")
        result_frame.pack(expand=True, fill="both", padx=30, pady=(0, 20))

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

        search_button.bind("<Enter>", lambda e: search_button.config(bg="#e67e22"))
        search_button.bind("<Leave>", lambda e: search_button.config(bg="#f39c12"))

    def perform_search(self, search_entry, result_text):
        search_id = search_entry.get().strip()
        if not search_id:
            messagebox.showerror("Error", "Please enter an ID to search.")
            return
        
        try:
            with open(self.records_inputs, "r") as file:
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

if __name__ == "__main__":
    root = tk.Tk()
    app = RecordLogsGUI(root)
    root.mainloop()