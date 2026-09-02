def main():
    arr = []
    num = 0
    while num != -10:
        num = int(input('Enter a number (-10 to end): '))
        if num != -10:
            arr.append(num)

    
    maxNums = [-1, -1]
    for num in arr:
        if num > maxNums[0]:
            maxNums[1] = maxNums[0]
            maxNums[0] = num
        elif num > maxNums[1]:
            maxNums[1] = num

    print(maxNums[0] * maxNums[1])

main()