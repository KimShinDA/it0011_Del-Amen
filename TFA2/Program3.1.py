firstName = input("\nEnter First Name: ")
lastName = input("\nEnter Last Name: ")
age = input("\nEnter Age: ")

fullName = firstName + ' ' + lastName

sliceName = firstName[:3]

message = "Hello, {fName}! Welcome. You are {Age}  years old".format(fName = sliceName, Age=age)


print("Full name: ", fullName)
print("Sliced name: ", sliceName)
print("Greeting Message: ", message)




