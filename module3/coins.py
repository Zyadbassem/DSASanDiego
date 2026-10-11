def coins(money: float):
    dime, nickel, penny =  10, 5, 1
    num_of_coins = 0
    while money > 0:
        money -=  dime if money >= dime else nickel if money >= nickel else penny
        num_of_coins += 1

    return num_of_coins



print(coins(28))