def last_of_sum_fib():
    n = int(input())
    arr = [0] * (n+1)
    arr[1] = 1
    result = 1
    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]
        result+=arr[i]
    
    return result

print(last_of_sum_fib())




