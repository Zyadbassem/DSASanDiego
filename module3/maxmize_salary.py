def max_salary(a: list):
    a.sort(reverse=True)
    num = 0
    for n in a:
        num *= 10
        num += n
    
    return num

def main():
    count = input()
    nums = [ int(x) for x in list(input().replace(' ', ''))]
    print(max_salary(nums))

main()