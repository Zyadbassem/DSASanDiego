def main():
    arr = []
    num = 0
    while num != -10:
        num = int(input('Enter a number (-10 to end): '))
        if num != -10:
            arr.append(num)

    target = int(input('Enter a target: '))
    print(solve(arr, target))



    

def solve(arr:list, target:int):
    holder = dict()
    for i in range(len(arr)):
        current = arr[i]
        wanted = target / current

        if wanted in holder:
            return (holder[wanted], i)
        else:
            holder[current] = i

    return (-1, -1)

main()