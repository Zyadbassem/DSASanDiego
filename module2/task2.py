def gcd(n1: int, n2: int):
    if n2 == 0:
        return n1
    nPrime = n1 % n2
    return gcd(n2, nPrime)

#print(gcd(848925, 2343242))

# gcd(2343242, 848925)
# gcd(848925, 645392)
# gcd(645392, 203533)
# gcd(203533, 34793)
# gcd(34793, 29568)
# gcd(29568, 5225)
# gcd(5225, 3443)
# gcd(3443, 1782)
# gcd(1782, 1661)
# gcd(1661, 121)
# gcd(121, 88)
# gcd(88, 33)
# gcd(33, 22)
# gcd(22, 11)
# gcd(11, 0)