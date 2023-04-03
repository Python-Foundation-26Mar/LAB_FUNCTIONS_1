'''
a function that takes 1 parameter of type int
'''
def number(n:int):
 
 for r in range(1,n):
    for c in range(1,r+1):
        print(c,end=" ")
    print("")    

print(number(6))

print(number.__doc__)