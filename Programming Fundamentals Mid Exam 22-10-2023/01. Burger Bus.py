number_of_cities = int(input())
total_profit = 0

for cities in range(1, number_of_cities +1):
    city = input()
    earned_money = float(input())
    if cities % 5 == 0:
        earned_money -= earned_money * 0.1
    expenses = float(input())
    if cities % 3 == 0 and cities % 5 != 0:
        expenses *= 1.5
    profit_from_city = earned_money - expenses
    total_profit += profit_from_city
    print(f"In {city} Burger Bus earned {profit_from_city:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")


