def celebration_groups(children: list):
    children.sort()
    curr_lowest = children[0]
    output = []
    curr_group = [curr_lowest]

    for child in children[1:]:
        if child - 2 <= curr_lowest:
            curr_group.append(child)
        else:
            output.append(curr_group)
            curr_lowest = child
            curr_group = [curr_lowest]
    
    output.append(curr_group)
    return output
        

print(celebration_groups([2, 4, 1, 5, 3, 9, 4, 10]))
# 1 -> 3
# 4 -> 6
# 7 -> 9
