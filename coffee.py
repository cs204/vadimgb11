def main():
    price = 50
    amount_due = price

    while amount_due > 0:
        print(f"Нужная сумма: {amount_due}")
        coin = get_coin()
        if coin != -1:
            amount_due -= coin

    change_owed = abs(amount_due)
    print(f"Ваша сдача: {change_owed}")

def get_coin():
    coin = int(input("Вставьте монету: "))
    match coin:
        case 50 | 20 | 10 | 5:
            return coin
        case _:
            return -1

main()
