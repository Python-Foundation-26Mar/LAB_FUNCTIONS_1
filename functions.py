num=int(input("enter the number"))

def numbers (num :int):
    for i in range(num):
        for j in range(num-i-1,-1,-1):
           print(j+1,end=" ")
        print(" ")


numbers(num)
