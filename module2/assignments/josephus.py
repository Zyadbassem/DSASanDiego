def josephus(n, k):
  arr = []
  for i in range(0, n):
    arr.append(1)
  killed = 0
  current = 0

  print(arr)
  
  while killed < (len(arr) - 1):
    # is current 1
    while arr[current] == 0:
      current = current + 1 if current < (len(arr) - 1) else 0

    #current is 1
    skips = k - 1
    killing = current
    while skips > 0 or arr[killing] == 0:
      if arr[killing] == 1:
        skips -= 1
      killing = killing + 1 if killing < (len(arr) - 1) else 0

    arr[killing] = 0
    current = killing
    killed += 1
    
 

  return arr.index(1)
