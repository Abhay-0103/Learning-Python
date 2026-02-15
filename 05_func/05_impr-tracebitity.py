def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


order = [100, 150, 200]

for price in order:
    final_amout = add_vat(price, 20)
    print(f"Final amount for price {price} is {final_amout}")