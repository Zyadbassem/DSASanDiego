def divider(arr: list):
    half = len(arr) // 2
    left = arr[0:half]
    right = arr[half:]

    return  left, right

def poly_multi_dac(a: list, b: list, n):
    holder_list = [0 for _ in range(2*n - 1)]
    if n == 1:
        return [a[0] * b[0]]

    A0, A1 = divider(a)
    B0, B1 = divider(b)

    z0 = poly_multi_dac(A0, B0, n//2)
    z1 = poly_multi_dac(A0, B1, n//2)
    z2 = poly_multi_dac(A1, B0, n//2)
    z3 = poly_multi_dac(A1, B1, n//2)

    for i in range(len(z0)):
        holder_list[i] += z0[i]

    for j in range(n//2, n//2 + len(z1)):
        holder_list[j] += z1[j-n//2]
        holder_list[j] += z2[j-n//2]

    for l in range(n, len(holder_list)):
        holder_list[l] += z3[l-n] if z3[l-n] else 0

    return  holder_list


print(poly_multi_dac([1, 2], [3, 4], 2))
# Expected: [3, 10, 8]

print(poly_multi_dac([1, 2, 3, 4], [1, 1, 1, 1], 4))
# Expected: [1, 3, 6, 10, 9, 7, 4]





'''
    A(x) = A0(x) + A1(x)x^n
    
    A(x) * B(x) =
'''

