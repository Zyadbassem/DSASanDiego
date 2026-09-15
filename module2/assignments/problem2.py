def pisano(m=10):
    arr = [0, 1]
    prev, curr = 0, 1
    while True:
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            arr.pop() 
            return arr
        arr.append(curr)

def last_fib_mod():
    n = int(input())

    pis = pisano()
    place = n % len(pis)

    return pis[place]


print(last_fib_mod())

