rows = 1
while rows <= 7:
    if rows != 2 and rows != 4:  
        col = 1
        while col <= rows:
            print(rows, end="")
            col += 1
        print("\n")
    rows += 1