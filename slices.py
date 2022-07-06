#Lenny Ramroop
#Program - Len's Slice
#Created on Codecademy

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

num_two_dollar_slices = prices.count(2)
print('Number of two dollar slices: ' + str(num_two_dollar_slices))

num_pizzas = len(toppings)
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()
pizza_and_prices.insert(4, [2.5, 'peppers'])

three_cheapest = pizza_and_prices[:3]

print('The three cheapest pizzas are: ' + str(three_cheapest))
print('The cheapest pizza is: ' + str(cheapest_pizza))
print('The pizzas we  have available: ' + str(pizza_and_prices))