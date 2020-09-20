# Make a list of sandwiches that can be ordered with a quanity, have a random flow of orders until exhausted
from random import choice

# Create a list of sandwiches that are available, with a quantity for each
sandwiches = {'turkey': 5, 'blt': 5, 'meatball': 5, 'veggie': 5, 'italian': 5}

print("The deli is open & taking orders!")
n = 0
missedOrders = 0
# loop through this process, as long as there is at least one sandwich still available
while n < sum(list(sandwiches.values())):
    order = choice(list(sandwiches.keys()))
    if sandwiches[order] > 0:
        print(f"Order for {order}")
        sandwiches[order] -= 1
    else:
        print(f"We're all out of {order}")
        missedOrders += 1

print(f"The deli is closed. We missed {missedOrders} orders")
