def gcd(n1: int, n2: int):
    while n2 != 0:
        current = n1 % n2
        n1 = n2
        n2 = current
    return n1

print(gcd(848925, 2343242))