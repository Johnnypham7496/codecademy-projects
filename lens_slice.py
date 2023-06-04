# You work at Len’s Slice, a new pizza joint in the neighborhood. 
# You are going to use your knowledge of Python lists to organize some of your sales data.

# my code below:
toppings = ['pepperoni', 'pineapple', 'cheese', 'sasuage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
number_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

pizza_and_prices = [
  [2, 'pepperoni'], 
  [6, 'pineapple'], 
  [1, 'cheese'],
  [3, 'sausage'],
  [2, 'olives'],
  [7, 'anchovies'],
  [2, 'mushrooms']
]


pizza_and_prices.sort()
print(pizza_and_prices)
print()
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
print()


priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
print()


pizza_and_prices.pop(-1)
pizza_and_prices.insert(4, [2.5, 'peppers'])
print(pizza_and_prices)
print()


three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)