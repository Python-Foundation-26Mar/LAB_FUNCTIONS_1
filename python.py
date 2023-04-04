
def hierarchical_pattern(num:int):
    ''' This is a function that will print an inverse pyramid of numbers provided a number'''
    numbers_string = ""
    for z in range(num, 0, -1):
        for y in range(z, 0, -1):
            numbers_string += f" {y}"
        print(numbers_string)
        numbers_string = ""
        

hierarchical_pattern(7)
print(hierarchical_pattern.__doc__)


