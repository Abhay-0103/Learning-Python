def calaculate_bill(cups, price_per_cup):
    return cups * price_per_cup


total_bill = calaculate_bill(5, 12)
print(f"Total bill: {total_bill}")


print("Order for tovkae : " , calaculate_bill(2, 50))