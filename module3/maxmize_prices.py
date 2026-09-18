def maxmize_prices(num: int):
   total = 0
   nums = []
   for i in range(1, num):
       next_total = total + i + i + 1
       if next_total > num:
           nums.append((num - total))
           break
       else:
           total += i
           nums.append(i)

   return nums

def main():
    num = int(input())
    nums = maxmize_prices(num)
    print(len(nums))
    for n in nums:
        print(n, end=' ')
    print('')


main()