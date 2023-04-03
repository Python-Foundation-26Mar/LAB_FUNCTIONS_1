## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

r = int (input("enter a number "))


def printer(r : int):
    for x in range( r, 0, -1):
        for n in range(x, 0 ,-1):
            print(n , end =" ")
        print(" ")


printer(r)
