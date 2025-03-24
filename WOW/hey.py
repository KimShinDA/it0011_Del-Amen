# Importing the necessary libraries
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Class lang for the Record logs pero w/ GUI na
class RecordLogsGUI:
    def __init__(self, root, file_name="records.txt"):
        self.root = root # root is for the main window
        self.root.title("Record Management System") # Title of the main window
        self.root.geometry("420x300") # Size lang, koket lang
        self.records_inputs = file_name 

        # Main Frame
        self.frame = tk.Frame(root, padx=20, pady=20, bg="#f8f9fa")
        self.frame.pack(expand=True, fill="both")

        # Title Label
        self.label = tk.Label(self.frame, text="Record Management System", font=("Arial", 14, "bold"), bg="#f8f9fa")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Button Styling ; parang CSS lang 'yan sha kaya medyo ez 
        button_style = {"width": 20, "height": 2, "font": ("Arial", 10), "fg": "white"}
        self.btn_signup = tk.Button(self.frame, text="Sign-up", command=self.sign_up, bg="#4CAF50", **button_style)
        self.btn_view = tk.Button(self.frame, text="View All Records", command=self.view_records, bg="#2196F3", **button_style)
        self.btn_search = tk.Button(self.frame, text="Search Record", command=self.search_record, bg="#FF9800", **button_style)
        self.btn_exit = tk.Button(self.frame, text="Exit", command=root.quit, bg="#F44336", **button_style)

        # Button Layout ; para maayos lang 'yung pagkakaayos ng buttons
        self.btn_signup.grid(row=1, column=0, pady=5, padx=5)
        self.btn_view.grid(row=1, column=1, pady=5, padx=5)
        self.btn_search.grid(row=2, column=0, pady=5, padx=5)
        self.btn_exit.grid(row=2, column=1, pady=5, padx=5)

    # Function to count existing records
    # Same lang sa previous code ; no changes
    def count_existing_records(self):
        try:
            with open(self.records_inputs, "r") as file:
                content = file.read().strip()
            return content.count("Record #")
        except FileNotFoundError:
            return 0

    # Function to check if records exist
    # No changes din sa previous code
    def records_exist(self):
        return self.count_existing_records() > 0

    # Function to sign-up 
    # Mostly dito na yung mga nagbago
    def sign_up(self):
        signup_window = tk.Toplevel(self.root) # Toplevel para may sariling window
        signup_window.title("Sign-Up Form")
        signup_window.geometry("350x350")
        signup_window.configure(bg="#ffffff")

        # parang forms lang 'to sa HTML
        fields = ["First Name", "Middle Name", "Last Name", "Birthday (MM-DD-YYYY)", "Gender (M/F)"]
        entries = {} # para sa mga entries

        # Loop through the fields
        for field in fields:
            tk.Label(signup_window, text=field+":", bg="#ffffff").pack()
            entries[field] = tk.Entry(signup_window)
            entries[field].pack()

        # Function to validate birthday (FORMAT + VALID DATE)
        def validate_birthday(birthday):
            if len(birthday) != 10 or birthday[2] != '-' or birthday[5] != '-':
                return False

            month, day, year = birthday.split('-')

            if not (month.isdigit() and day.isdigit() and year.isdigit()):
                return False

            month, day, year = int(month), int(day), int(year)

            if year < 1900 or year > 2025:
                return False
            
            # Check valid month
            if month < 1 or month > 12:
                return False

            # Days per month (assuming no leap year check for simplicity)
            days_in_month = {
                1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
            }

            if day < 1 or day > days_in_month[month]:
                return False

            return True

        # Function to save the record
        # New function siya to save the record
        def save_record():
            # Get the data from the entries
            data = {field: entries[field].get().strip() for field in fields}

            if not data["First Name"] or not data["Last Name"]:
                messagebox.showerror("Error", "First and Last Name are required.") # Parang alert lang siya pero naging window style
                return

            if not validate_birthday(data["Birthday (MM-DD-YYYY)"]):
                messagebox.showerror("Error", "Invalid Birthday. Use MM-DD-YYYY and enter a real date.")
                return

            gender = data["Gender (M/F)"].upper()
            if gender not in ("M", "F"):
                messagebox.showerror("Error", "Gender must be 'M' for Male or 'F' for Female.")
                return

            gender_full = "Male" if gender == "M" else "Female"

            # Generate unique ID, same lang sa previous code ; no changes
            record_number = self.count_existing_records() + 1
            unique_id = "2025" + str(record_number).zfill(5)

            with open(self.records_inputs, "a") as file:
                file.write(f"\nRecord #{record_number}\n")
                file.write(f"ID: {unique_id}\n")
                file.write(f"Name: {data['First Name']} {data['Middle Name']} {data['Last Name']}\n")
                file.write(f"Birthday: {data['Birthday (MM-DD-YYYY)']}\n")
                file.write(f"Gender: {gender_full}\n")

            messagebox.showinfo("Success", f"Record saved!\nID: {unique_id}") # Alert for successful saving
            signup_window.destroy() # Close the window

        tk.Button(signup_window, text="Save Record", command=save_record, bg="#4CAF50", fg="white").pack(pady=10)

    # Function to view records
    def view_records(self):
        if not self.records_exist():
            messagebox.showwarning("No Records", "No records found. Please sign-up first.")
            return

        view_window = tk.Toplevel(self.root)
        view_window.title("View Records")
        view_window.geometry("450x400")

        text_area = scrolledtext.ScrolledText(view_window, width=50, height=20)
        text_area.pack(padx=10, pady=10)

        with open(self.records_inputs, "r") as file:
            text_area.insert(tk.END, file.read().strip())

        text_area.config(state=tk.DISABLED)

    # Function to search records
    def search_record(self):
        if not self.records_exist():
            messagebox.showwarning("No Records", "No records found. Please sign-up first.")
            return

        search_window = tk.Toplevel(self.root)
        search_window.title("Search Record")
        search_window.geometry("400x300")

        tk.Label(search_window, text="Enter ID to search:", font=("Arial", 10)).pack(pady=5)
        search_entry = tk.Entry(search_window, width=30)
        search_entry.pack()

        result_text = scrolledtext.ScrolledText(search_window, width=50, height=10)
        result_text.pack(padx=10, pady=10)

        def perform_search():
            search_id = search_entry.get().strip()
            if not search_id:
                messagebox.showerror("Error", "Please enter an ID to search.")
                return

            try:
                with open(self.records_inputs, "r") as file:
                    records = file.readlines()

                found_records = []
                for i in range(len(records)):
                    if "ID:" in records[i]:
                        record_id = records[i].strip().split(": ")[1]
                        if search_id == record_id:
                            found_records.append("".join(records[i - 1 : i + 4]))
                            break

                result_text.config(state=tk.NORMAL)
                result_text.delete(1.0, tk.END)

                if found_records:
                    result_text.insert(tk.END, "\n\n".join(found_records))
                else:
                    result_text.insert(tk.END, "No matching record found.")

                result_text.config(state=tk.DISABLED)

            except FileNotFoundError:
                messagebox.showwarning("No Records", "No available records at the moment.")

        tk.Button(search_window, text="Search", command=perform_search, bg="#2196F3", fg="white").pack(pady=10)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = RecordLogsGUI(root)  # Pass the main window to the class
    root.mainloop() # Run the main loop