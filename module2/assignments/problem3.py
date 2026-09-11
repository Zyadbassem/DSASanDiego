def pisano(m):
    arr = [0, 1]
    prev, curr = 0, 1
    while True:
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            arr.pop() 
            return arr
        arr.append(curr)

def last_fib_mod():
    input_arr = input().split(' ')
    int_input_arr = [int(x) for x in input_arr]

    n = int_input_arr[0]
    m = int_input_arr[1]

    pis = pisano(m)
    place = n % len(pis)

    return pis[place]





print(last_fib_mod())

