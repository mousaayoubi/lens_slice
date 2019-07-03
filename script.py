#Create toppings list
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#Create prices list
prices = [2, 6, 1, 3, 2, 7, 2]

#Length of toppings
num_pizzas = len(toppings)

print("We sell "+str(num_pizzas)+" different kinds of pizza!")

#Combine price list with toppings list
pizzas = list(zip(prices, toppings))

#Sort pizzas
pizzas.sort()
print(pizzas)

#Cheapest pizza
cheapest_pizza = pizzas[0]

#Most expensive pizza
priciest_pizza = pizzas[-1]

#Three cheapest pizza
three_cheapest = pizzas[:3]
print(three_cheapest)

#Two dollar slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)