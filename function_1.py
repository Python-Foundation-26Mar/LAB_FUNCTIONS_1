

def countdown(x:int):

    
    '''This function counts down from a geven number to 1 and then counts down from a (geven number - 1) to 1 and so on'''

    print("\n")

    for number in range(1,x+1):
          print(x-number+1, end ="  ")
    if x > 1:
         countdown(x-1)


countdown(5)

print("\n\n",countdown.__doc__)

