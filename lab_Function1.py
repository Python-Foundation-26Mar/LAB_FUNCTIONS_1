

def my_function(x:int):
    for j in range (x,0,-1):
        for i in range(0,j):
            print(i,end = " ")
        print(" ")
x=7
my_function(x)

"This is a function that takes an int parameter ,and then prints the digit pattern using an inverted pyramid"