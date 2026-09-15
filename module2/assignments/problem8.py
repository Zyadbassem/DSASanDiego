def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, (n%m))

def runner():
    arr = input().split(' ')
    arr = [int(x) for x in arr]

    n = arr[0]
    m = arr[1]

    greatest_div = gcd(n, m)

    return int((n * m) / greatest_div)


print(runner())
