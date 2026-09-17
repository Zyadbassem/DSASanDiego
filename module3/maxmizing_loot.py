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
        



        


print(maxmizing_loot([5, 4, 3], [30, 28, 24], 9))
