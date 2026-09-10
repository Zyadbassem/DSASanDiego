import math 
#Fibonacci Numbers
def feb_calc(n: int):
    arr = [0, 1]
    for num in range(2, n+1):
        arr.append(arr[num-1] + arr[num-2])
    print(arr)

    return arr[n]


print(feb_calc(5))