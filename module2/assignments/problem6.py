def pisano():
    prev, curr = 0, 1
    arr = [0, 1]

    while True:
        prev, curr = curr, (prev + curr) % 10
        if prev == 0 and curr == 1:
            arr.pop()
            break
        arr.append(curr)

    return arr

def sqr_of_feb():
    n = int(input())
    pis = pisano()
    feb_of_n = pis[n % len(pis)]
    feb_of_n_minus_one = pis[(n-1) % len(pis)]
    sum_of_sqr = feb_of_n ** 2 + feb_of_n * feb_of_n_minus_one
    return (sum_of_sqr % 10)

print(sqr_of_feb())

