def pisano():
    arr = [0, 1]
    prev , curr = 0, 1
    while True:
        prev, curr = curr, (prev + curr) % 10
        if prev == 0 and curr == 1:
            arr.pop()
            break
        arr.append(curr)
    return arr

def las_dig_of_sum_fib():
    n = int(input())
    pis = pisano()
    wanted = (n+2) % len(pis)
    return (pis[wanted] - 1) % 10

print(las_dig_of_sum_fib())        




