def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, (n%m))

def runner():
    arr = input().split(' ')
    arr = [int(x) for x in arr]

    n = arr[0]
    m = arr[1]

    return gcd(n, m)


print(runner())
print(67.0 * 1634.0)
