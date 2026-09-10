def main():
    arr = []
    num = 0
    input()
    arr = list(map(int, input().split(' ')))

    
    maxNums = [-1, -1]
    for num in arr:
        if num > maxNums[0]:
            maxNums[1] = maxNums[0]
            maxNums[0] = num
        elif num > maxNums[1]:
            maxNums[1] = num

    print(maxNums[0] * maxNums[1])

main()