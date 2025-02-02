file_name = "secretMessage.txt"

# Save secret message
file = open(file_name, "w", encoding="utf-16")
file.write(input("Enter your secret message: "))
file.close()

print(f"Message saved to '{file_name}'.")

# Read message if user chooses
if input("Read the secret message? (yes/no): ").strip().lower() == "yes":
    file = open(file_name, "r", encoding="utf-16")
    print("Decoded Message:", file.read())
    file.close()
else:
    print("Message remains secret!")
