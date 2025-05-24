cost = 50
amount_inserted = 0

valid_coins = [25, 10, 5]
while amount_inserted < cost:
    print(f"Amount Due: {cost - amount_inserted}")
    coin = int(input("Insert Coin: "))
    if coin in valid_coins:
        amount_inserted += coin
    else:

        pass

change = amount_inserted - cost
print(f"Change Owed: {change}")
