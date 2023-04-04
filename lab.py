def count_down(n:int):

    print("\n")
    for number in range(1,n+1):
        print(n-number+1,end=" ")
    if n >0:
        count_down(n-1)

count_down(5)