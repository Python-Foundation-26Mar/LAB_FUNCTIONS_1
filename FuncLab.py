def pattren_numbers(num:int):
    '''A function to print a pattren of numbers in descending order'''
    for n in range (0,num+1):
        for p in range (num-n,0,-1):
            print(p, end="")
        print ("")
            
pattren_numbers(20)

                           
    
