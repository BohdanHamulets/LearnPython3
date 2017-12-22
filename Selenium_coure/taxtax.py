def calculate_tax(amount):
    if int(amount) > 200000:
        return amount * 0.25
    elif int(amount) > 500000:
        return int(amount) * 0.3
    elif int(amount) > 1000000:
        return int(amount) * 0.5
    else:
        return int(amount) * 0.1

print(calculate_tax(201000.99))

bla = "string"

bla.upper()