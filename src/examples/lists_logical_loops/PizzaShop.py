# Make an application that keeps building a pizza order until the person says quit
# Create lists with common yes & no responses
yes = ['y', 'yes', 'yeah', 'please', 'okay', 'absolutely']
no = ['n', 'no', 'nope', 'never', 'please no']
done = ['all done', 'quit', 'nothing', 'no more', 'stop', 'no', 'none', 'done']

# Create list of available toppings for a pizza
toppings = ['pepperoni', 'mushrooms', 'extra cheese', 'sausage', 'bacon', 'anchovies', 'peppers', 'olives', 'sardines',
            'anchovies', 'steak', 'broccoli', 'chicken', 'pineapple']

order = []

plainPizza = input("welcome to Boz's pizza, let's start your pizza order do you want a plain pizza?")
# If the person says that want a cheese pizza, place the order and end the script
if plainPizza in yes:
    print("Okay your cheese pizza will be right up!")

# If the person says they don't want a chese pizza, go through this loop to collect topping orders
elif plainPizza in no:
    n = 0
    # Limit a pizza to just 5 orders
    while n < 5:
        # Have a specific message for the first order
        if n == 0:
            topping = input("Okay, let's get some toppings. What would you like?")
        else:
            topping = input("anything else?")
        # check to see if the topping is in the list of toppings
        if topping in toppings:
            # check to see if the person has already added this topping to the pizza
            if topping in order:
                print("You already added that to your pizza")
            else:
                print(f"Okay, adding {topping}")
                order.append(topping)
                n += 1
        # check to see if the person gave an indication they are done adding toppings to the pizza
        elif topping in done:
            print("okay, let's get that order together")
            break
        else:
            print("Sorry I don't think we have that as a topping")

if order:
    print("So that's a pizza with", end=" ")
    for item in order:
        # this silly check is to see if we're on the last item in the list, if so, we don't put a comma after it and
        # remain grammatically correct
        if item == order[-1]:
            print(f"{item}", end=" ")
        else:
            print(f"{item}, and", end=" ")
