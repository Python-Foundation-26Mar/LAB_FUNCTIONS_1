n=int (input("Enter the number here :"))
''' A function that takes a single parameter of type int, and then prints the result formatted as numbers in a triangle.  '''
for i in range(n):
    for j in range(n-i-1,-1,-1):
        print(j+1,end=" ")
    print()
