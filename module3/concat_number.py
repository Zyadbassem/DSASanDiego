def concat_numbers(numbers: list):
    sorted_nums = sorted(numbers, reverse=True)
    concated = 0

    for num in sorted_nums:
        concated *= 10
        concated += num

    return concated


print(concat_numbers([2, 4, 8, 2, 9]))