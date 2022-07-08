#Lenny Ramroop
#Carly's Clippers - Python project
#This mini Python project demonstrates the use of loops!

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
total_revenue = 0

for i in prices:
  total_price += i

average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

new_prices = [num - 5 for num in prices]
print(new_prices)

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

average_daily_revenue = total_revenue / 7

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

print(total_revenue)
print(average_daily_revenue)
print(cuts_under_30)