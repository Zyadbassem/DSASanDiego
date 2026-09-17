def coins(money: float):
    money *= 100
    quarter, dime, nickel, penny = 25, 10, 5, 1
    
    num_of_coins = 0
    while money > 0:
        money -= quarter if money >= quarter else dime if money >= dime else nickel if money >= nickel else penny
        num_of_coins += 1

    return num_of_coins



print(coins(1.3))