hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for p in prices:
  total_price += p
print(total_price, "\n")

average_price = total_price / len(prices)
print(f"Average Haircut Price: \n{average_price:.2f}", "\n")

new_prices = [p - 5 for p in prices]
print(new_prices, "\n")

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])
print(f"Total Revenue: {total_revenue}", "\n")

average_daily_revenue = total_revenue / 7
print(average_daily_revenue, "\n")

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]
print(cuts_under_30)
