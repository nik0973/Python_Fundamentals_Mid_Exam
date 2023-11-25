current_price = 0
while True:
    price = input()
    if price == "special" or price == "regular":
        break
    if float(price) == 0 or float(price) < 0:
        print("Invalid price!")
    else:
        current_price += float(price)
total_price = current_price * 1.2
taxes = current_price * 0.2
if price == "special":
    total_price = total_price * 0.9
if current_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {current_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")