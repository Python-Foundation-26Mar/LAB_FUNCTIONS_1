## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
def down (num:int):
    '''This function counts down from a geven number to 1 '''
    print("\n")

    for number in range(1,num+1):
        print(num-number+1, end="  ")
    if num > 1:
        down(num-1)

down(5) 
print("\n")
print(down.__doc__) 