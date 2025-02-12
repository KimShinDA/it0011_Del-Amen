file = open('numbers.txt', 'r')
line_number = 1

for line in file:
    numbers = line.strip().split(',')
    numbers = [num for num in numbers if num.strip()]  
    total_sum = sum(int(num) for num in numbers)
    
    sum_str = str(total_sum)
    if sum_str == sum_str[::-1]:
        result = "Palindrome"
    else:
        result = "Not a palindrome"

    output_numbers = ""
    for num in numbers:
        output_numbers += num + ","
    output_numbers = output_numbers[:-1]

    print(f"Line {line_number}: {output_numbers} (sum {total_sum}) - {result}")
    
    line_number += 1

file.close()