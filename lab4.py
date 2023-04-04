'''
Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

#this function take parametr for user, and printing in a descending pattern
def num (num1):
    for i in range(0, num1 + 1):
        for j in range(num1 - i, 0, -1):
            print(j, end=' ')
        print()

#read from user
num2 = int(input(" Enter the number : "))

#calling the function
num(num2)