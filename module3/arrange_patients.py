def arrange_patients(l: list) -> int:
    total_per_patient = 0
    actual_total = 0    
    l.sort()

    for num in l:
        actual_total += total_per_patient
        total_per_patient += num
    
    return actual_total

    


print(arrange_patients([15, 10, 20]))