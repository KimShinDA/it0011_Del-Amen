for rows in range(1, 6):  
    print(' ' * (5 - rows), end='') 
    for col in range(1, rows + 1):  
        print(col, end='')  
    print()  