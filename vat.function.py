def calculate_price_with_vat(price, vat):
    return price * ((100 + vat) / 100)

print(calculate_price_with_vat(500,20))

