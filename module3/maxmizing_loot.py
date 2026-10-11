def maxmizing_loot(weights: list, values: list, W: float):
    value_per_one = []

    for value, weight in zip(values, weights):
        value_per_one.append({'value': (value/weight), 'amount': weight})
    
    sorted_values = sorted(value_per_one, key=lambda curr: curr['value'], reverse=True)
    
    total_weight = 0
    total_value = 0

    for v in sorted_values:
        if total_weight + v['amount'] <= W:
            total_weight += v['amount']
            total_value += (v['amount'] * v['value'])
        else:
            remaining = W - total_weight
            total_value += (remaining * v['value'])
            break

    

    return total_value
        


def main():
    weights = []
    values = []

    f_line = [int(x) for x in input().split(' ')]
    n_of_lines = f_line[0]
    max_c = f_line[1]

    for i in range(0, n_of_lines):
        curr_line =  [int(x) for x in input().split(' ')]
        values.append(curr_line[0])
        weights.append(curr_line[1])
    
    print(maxmizing_loot(weights, values, max_c))
        


main()