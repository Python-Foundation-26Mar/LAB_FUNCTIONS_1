def function_1(number:int):
    '''this is a function given a number it will print an inverse pyramid of numbers'''
    numbers_string = ""
    for s1 in range(number, 0, -1):
        for s2 in range(s1, 0, -1):
            numbers_string += f" {s2}"
        print(numbers_string)
        numbers_string = ""
        


function_1(6)
print(function_1.__doc__)