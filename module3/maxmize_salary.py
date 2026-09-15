def max_salary(a: list):
    a.sort(reverse=True)
    num = 0
    for n in a:
        num *= 10
        num += n
    
    return num

print(max_salary([4, 2, 9, 5]))

