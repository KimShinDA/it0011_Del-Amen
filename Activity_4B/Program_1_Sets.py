# Define sets A, B, and C
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'l', 'b', 'c', 'm', 'o', 'h'}
C = {'f', 'd', 'c', 'h', 'j', 'k', 'i'}

# Calculate the number of elements in each set
num_elements_a = len(A)
num_elements_b = len(B)

# Total number of elements in sets A and B 
total_elements_a_b = num_elements_a + num_elements_b

# Elements unique to B, excluding those present in A or C
unique_elements_b = B - (A | C)

# Elements unique to C, excluding those in A
unique_elements_c = C - A

# Elements that are common in A and C
common_elements_a_c = A & C

# Elements in B that are also found in either A or C
common_elements_b_ac = B & (C | A)

# Elements that are common in A and C but not in B
common_elements_ac_not_b = (A & C) - B

# Elements that are common in all three sets A, B, and C
common_elements_a_b_c = A & B & C

# Unique elements in B, excluding those in A and C
unique_elements_b = B - A - C



# Print Sets of Elements
print("Set A:", A)
print("\nSet B:", B)
print("\nSet C:", C)

# Print results
print("\na. Total number of elements in A and B:", total_elements_a_b)
print("b. Number of unique elements in B (excluding those in A and C):", len(unique_elements_b))

print("\nc. Show the following using set operations")
print("i. Unique elements in C that are not in A:", unique_elements_c)
print("ii. Common elements between A and C:", common_elements_a_c)
print("iii. Common elements in B that also appear in A or C:", common_elements_b_ac)
print("iv. Common elements in A and C, but not in B:", common_elements_ac_not_b)
print("v. Common elements in A, B, and C:", common_elements_a_b_c)
print("vi. Unique elements in B (excluding A and C):", unique_elements_b)
