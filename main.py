
def numbers (number:int):
    ''' this is function to print inverse pyramid of numbers'''
    n = ""
    for i in range(number,0,-1) :
        for j in range(i,0,-1):
            n += f" {j}"
        print(n)
        n=""
    
numbers(5)
print(numbers.__doc__)