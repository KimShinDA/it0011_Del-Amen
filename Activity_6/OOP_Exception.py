class Item:
    """Class representing an item with an ID, name, description, and price."""
    
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self):
        return f"ID: {self.item_id}\nName: {self.name}\nDescription: {self.description}\nPrice (₱): {self.price:.2f}\n"

class ItemCon:
    """Class for managing CRUD operations on items using file handling."""
    FILE_NAME = "items_info.txt"
    
    def __init__(self):
        self.items = []
        self.load_items()
    
    def load_items(self):
        """Loads items from the file."""
        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 4):  # Read in blocks of 4 lines
                    try:
                        item_id = int(lines[i].split(":")[1].strip())
                        name = lines[i + 1].split(":")[1].strip()
                        description = lines[i + 2].split(":")[1].strip()
                        price = float(lines[i + 3].split(":")[1].strip().replace("₱", ""))
                        self.items.append(Item(item_id, name, description, price))
                    except (IndexError, ValueError):
                        continue  # Skip invalid lines
        except FileNotFoundError:
            open(self.FILE_NAME, "w", encoding="utf-8").close()

    def save_items(self):
        """Saves items to the file using UTF-8 encoding."""
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            for item in self.items:
                file.write(str(item) + "\n")

    def create_item(self, name, description, price):
        """Creates and stores an item in the file."""
        try:
            price = float(price)  # Ensure price is a valid float
        except ValueError:
            print("=== Invalid price format. Please enter a valid number. ===")
            return

        item_id = len(self.items) + 1
        item = Item(item_id, name, description, price)
        self.items.append(item)
        self.save_items()

        print("=== Item added successfully! ===")

    def read_items(self):
        """Displays all items in a formatted list."""
        print("\n=== Item List ===")
        if not self.items:
            print("No items available.")
            return

        for item in self.items:
            print(item)
            print("=" * 40)

    def update_item(self, item_id, name, description, price):
        """Updates an existing item."""
        if not self.items:
            print("=== No items available. ===")
            return

        for item in self.items:
            if item.item_id == item_id:
                if name.strip():
                    item.name = name
                if description.strip():
                    item.description = description
                if price.strip():
                    try:
                        item.price = float(price)
                    except ValueError:
                        print("=== Invalid price format. ===")
                        return

                self.save_items()
                print("=== Item updated successfully! ===")
                return

        print("=== Item not found. ===")

    def delete_item(self, item_id):
        """Deletes an item by ID."""
        if not self.items:
            print("=== No items available. ===")
            return

        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                self.save_items()
                print("=== Item deleted successfully! ===")
                return

        print("=== Item not found. ===")

# Simple CLI for testing
def main():
    con = ItemCon()
    
    while True:
        print("\n====================================")
        print("      ITEM MANAGEMENT SYSTEM")
        print("====================================")
        print("[1] Add Item")
        print("[2] View Items")
        print("[3] Update Item")
        print("[4] Delete Item")
        print("[5] Exit")
        print("====================================")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            description = input("Enter item description: ").strip()
            price = input("Enter item price: ").strip()

            con.create_item(name, description, price)

        elif choice == "2":
            con.read_items()

        elif choice == "3":
            if not con.items:
                print("=== No items available. ===")
                continue
            try:
                item_id = int(input("Enter item ID to update: ").strip())
                name = input("Enter new name (press enter to keep current): ").strip()
                description = input("Enter new description (press enter to keep current): ").strip()
                price = input("Enter new price (press enter to keep current): ").strip()

                con.update_item(item_id, name, description, price)
            except ValueError:
                print("=== Invalid input. ===")

        elif choice == "4":
            if not con.items:
                print("=== No items available. ===")
                continue
            try:
                item_id = int(input("Enter item ID to delete: ").strip())
                con.delete_item(item_id)
            except ValueError:
                print("=== Invalid ID format. ===")

        elif choice == "5":
            print("=== Exiting... Goodbye! ===")
            break

        else:
            print("=== Invalid option. Try again. ===")

if __name__ == "__main__":
    main()
