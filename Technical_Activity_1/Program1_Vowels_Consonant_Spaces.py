vowels = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
consonants = 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'

vowelsCount = 0
consonantsCount = 0
spaceCount = 0
othersCount = 0

stringInput = input("Enter any string: ")

stringInputLower = stringInput.lower()

for char in stringInputLower:
        if char in vowels:
            vowelsCount += 1
        elif char in consonants:
            consonantsCount += 1
        elif char == " ":
            spaceCount += 1
        else:
            othersCount += 1
            
            
result = f"""=======================================================
| String: {stringInput} |
=======================================================
|  Vowels     : {vowelsCount}         |
|  Consonants : {consonantsCount}        |
|  Spaces     : {spaceCount}         |
|  Others     : {othersCount}         |
=======================================================
"""
print(result)
    


    
