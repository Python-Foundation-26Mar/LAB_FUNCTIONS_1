


def printer(a : int):
    for x in range( a, 0, -1):
        for n in range(x, 0 ,-1):
            print(n , end =" ")
        print(" ")

a = int (input("enter a number "))
printer(a)
