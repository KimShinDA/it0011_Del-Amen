class Record_Logs:
    def __init__(self, file_name="records.txt"): # forda class parang bongga
        self.records_inputs = file_name

    # Function to count existing records
    def count_existing_records(self):
        try:
            with open(self.records_inputs, "r") as file:
                content = file.read().strip()
            return content.count("Record #")  # Count occurrences of "Record #" to determine the next record number
        except FileNotFoundError:
            return 0  # If file doesn't exist, start at Record #1

    # Function to sign-up a new record
    def sign_up(self):
        print("\n---------- SIGN-UP FORM ----------")
        try:
            first_name = input("Enter First Name: ").strip()
            middle_name = input("Enter Middle Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            birthday = input("Enter Birthday (MM/DD/YYYY): ").strip()
            gender = input("Enter Gender (M/F): ").strip().upper()

            if not first_name or not last_name or not birthday or gender not in ("M", "F"):
                print("Error: Invalid input. All fields are required.")
                return

            record_number = self.count_existing_records() + 1
            unique_id = "2025" + str(record_number).zfill(5)

            with open(self.records_data, "a") as file:
                file.write(f"\nRecord #{record_number}\n")
                file.write(f"ID: {unique_id}\n")
                file.write(f"Name: {first_name} {middle_name} {last_name}\n")
                file.write(f"Birthday: {birthday}\n")
                file.write(f"Gender: {gender}\n")
                print(f"\nUnique ID: {unique_id}")

            print("Record successfully saved!")
        except Exception as e:
            print(f"Error: {e}")

    # Function to view all records
    def view_records(self):
        print("\n---------- VIEW ALL RECORDS ----------")
        try:
            with open(self.records_inputs, "r") as file:
                records = file.read().strip()

            if not records:
                print("No records found. Please sign-up first.")
                return

            print(records)  # Display records exactly as stored
        except FileNotFoundError:
            print("No available records at the moment.")
        except Exception as e:
            print(f"Error: {e}")

    # Function to search a record
    def search_record(self):
        print("\n---------- SEARCH RECORD ----------")
        try:
            file = open(self.records_inputs, "r")
            records = file.readlines()
            file.close()

            search_name = input("Enter First Name or Last Name to search: ").strip().lower()
            found = False

            for i in range(len(records)):
                if "Name:" in records[i]:
                    name = records[i].strip().split(": ")[1]
                    if search_name in name.lower():
                        print("\n".join(records[i - 1 : i + 3]))  # Print the full record (4 lines: Record #, Name, Birthday, Gender)
                        found = True

            if not found:
                print("No matching record found. Please sign-up first or check if the ID is correct.")

        except FileNotFoundError:
            print("No available records at the moment.")
        except Exception as e:
            print(f"Error: {e}")

# Main Menu
def main(): # The main function para sa pinaka nilalamang logic
    logs = Record_Logs()
    while True:
        print("\n----------------- MAIN MENU -----------------")
        print("   [1] Sign-up       [2] View all records")
        print("   [3] Search record [4] Exit")
        print("---------------------------------------------")

        try:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                logs.sign_up()
            elif choice == "2":
                logs.view_records()
            elif choice == "3":
                logs.search_record()
            elif choice == "4":
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__": 
    main() # Calls the main function only if the script is run as the main program
