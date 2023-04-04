5#function that takes 1 parameter of type int , then it prints out the result

def d (num:int):
    '''This is function counts d from a geven number to 1... '''
    print("\n")

    for i in range(1,num+1):
        print(num-i+1, end="  ")
    if num > 1:
        d(num-1)

d(6) 
print("\n")
print(d.__doc__) 

