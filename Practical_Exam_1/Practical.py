# Words to exclude
excluding_words = ["and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"]
 
# Get user input
statement = input("Enter a string statement\n:")
 
# Process words
words = statement.split()
word_count = {}
 
for word in words:
    clean_word = ""
    for char in word:
        if char.isalnum():  # Keep only letters and numbers
            clean_word += char
    lower_clean_word = clean_word.lower()
    if lower_clean_word and lower_clean_word not in excluding_words:
        if clean_word in word_count:
            word_count[clean_word] += 1
        else:
            word_count[clean_word] = 1
 
# Separate words by case
lowercase_words = []
uppercase_words = []
 
for word in word_count:
    if word[0].islower():
        lowercase_words.append(word)
    else:
        uppercase_words.append(word)
 
lowercase_words.sort()
uppercase_words.sort()
 
# Find the longest word for alignment
max_length = 0
for word in word_count:
    if len(word) > max_length:
        max_length = len(word)
 
# Print results
print("\nWord Frequency Count:\n" + "=" * (max_length + 20))
for word in lowercase_words + uppercase_words:
    spaces = " " * (max_length - len(word) + 2)
    print(word + spaces + "- " + str(word_count[word]))
print("=" * (max_length + 20))
 
# Print total filtered words
total_words = sum(word_count.values())
print("Total words filtered: ", total_words)