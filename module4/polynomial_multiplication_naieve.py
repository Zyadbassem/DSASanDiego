def poly_multiplication(n, a, b):
    holder = [0 for _ in range(n * 2 - 1)]

    for k in range(len(holder)):
       curr = 0
       s = max(k-n+1, 0)
       e = min(n, k+1)
       for i in range(s, e):
           curr += a[i]*b[k-i]

       holder[k] = curr

    return holder


a = [2, 2]
b = [4, 3]
print(poly_multiplication(4,[1, 4, 3, 2], [2, 3, 4, 2]))
'''
(2x + 2) * (3x + 4)
6x^2 + 8x + 6x + 8 -> 6x^2 + 14x + 8
  a2   a1   a0    b2   b1    b0
(x^2 + 2x + 2) * (x^2 + 3x + 4)
x^4 + 5x^3 + 12x^2 + 14x + 8


a0*b0
a1b0 + a0*b1
a2b0 + a0b2 + a1b1
a2b1 + b2b1
a2b2

'''

