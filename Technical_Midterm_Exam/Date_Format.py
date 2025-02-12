months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

date_str = input("Enter the date (mm/dd/yyyy): ")
month, day, year = date_str.split('/')
month_name = months[int(month) - 1]
print("Date Output:", f"{month_name} {int(day)}, {year}")