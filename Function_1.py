

# Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

def func1(number):
    ''' This is the function that solve the lab reqirements '''
    while number > 0:
        for z in range(number,0,-1):
            print(z)

        number = number -1


func1(6)
print(func1.__doc__)