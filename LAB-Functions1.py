def pyramid_num(num:int):
   
    '''A function print a pyramid'''
    print(pyramid_num.__doc__)

    for i in range (0,num+1):
        for y in range (num-i,0,-1):
            print(y, end=" ")
        print ("")
            
pyramid_num(5)
