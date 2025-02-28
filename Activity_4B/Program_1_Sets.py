# Define sets A, B, and C
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'l', 'b', 'c', 'm', 'o', 'h'}
C = {'f', 'd', 'c', 'h', 'j', 'k', 'i'}

# Total number of unique elements in sets A and B (Union)
totalElementsAB = len(A | B)  # Union of A and B

# Elements unique to B, excluding those present in A or C
uniqueElementsB = B - (A | C)

# Elements unique to C, excluding those in A
uniqueElementsC = C - A

# Elements that are common in A and C
commonElementsAC = A & C

# Elements in B that are also found in either A or C
commonElementsBAC = B & (C | A)

# Elements that are common in A and C but not in B
commonElementsACNotB = (A & C) - B

# Elements that are common in all three sets A, B, and C
commonElementsABC = A & B & C

# Unique elements in B, excluding those in A and C
uniqueElementsB = B - A - C

# Print Sets of Elements
print("Set A:", A)
print("\nSet B:", B)
print("\nSet C:", C)

# Print results
print("\na. Total number of elements in A and B:", totalElementsAB)  # Now should be 10
print("b. Number of unique elements in B (excluding those in A and C):", len(uniqueElementsB))

print("\nc. Show the following using set operations")
print("i. Unique elements in C that are not in A:", uniqueElementsC)
print("ii. Common elements between A and C:", commonElementsAC)
print("iii. Common elements in B that also appear in A or C:", commonElementsBAC)
print("iv. Common elements in A and C, but not in B:", commonElementsACNotB)
print("v. Common elements in A, B, and C:", commonElementsABC)
print("vi. Unique elements in B (excluding A and C):", uniqueElementsB)
