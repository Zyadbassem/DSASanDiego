def selection_sort(a: list):
    for i in range(len(a) - 1):
        curr_min = i
        for j in range(i+1, len(a)):
            if a[curr_min] > a[j]:
                curr_min = j
        a[curr_min], a[i] = a[i], a[curr_min]

    return a

print(selection_sort([3, 1, 5, 2, 0]))
