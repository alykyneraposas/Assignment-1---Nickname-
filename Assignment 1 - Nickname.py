str1 = "ALY"
print_A = [[" " for i in range (5)] for j in range (6)]
print_L = [[" " for i in range (5)] for j in range (6)]
print_Y = [[" " for i in range (5)] for j in range (6)]

#code for A
for row in range(6):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or row==2 or (row==0 and(col!=0 and col!=4)):
            print_A[row][col]= "*"

#code for L
for row in range(6):
    for col in range(5):
        if col==0 or row==5:
            print_L[row][col]= "*"

#code for Y
for row in range(6):
    for col in range(5):
        if (col==3 or row>2) or (row==col and col<3) or (row==col and col<3) or(row==0 and col==5):
            print_Y[row][col]= "*"
            
for i in range(6):
    for j in range(5):
        print(print_A[i][j],end="")
    print(end="  ")
    for j in range(5):
        print(print_L[i][j],end="")
    print(end="  ")
    for j in range(5):
        print(print_Y[i][j],end="")
    print()

            
