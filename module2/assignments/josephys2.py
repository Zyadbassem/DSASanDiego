def josephus(n, k):
   return (josephus(n-1, k) + k - 1) % n + 1 if n > 1 else 1


print(josephus(8, 3))