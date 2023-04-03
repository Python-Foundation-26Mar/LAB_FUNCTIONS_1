
def countdown (num:int):
    """This function counts down from a geven number to 1 and then counts down from a (geven number - 1) to 1 and so on"""
    print("\n")
    for number in range(1,num+1):
        print(num-number+1, end="  ")
    if num > 1:
        countdown(num-1)

countdown(5)   

