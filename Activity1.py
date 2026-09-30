# PART 1: Define a function with no arguments to greet the customer
def greet_customer():
    print("Welcome to the lemonade stand!")
    print("Fresh lemonade just for you!")

    # PART 2: Call the Greet_Customer function
greet_customer()

#part 3: ask for the price per cup and the number of cups sold
price_per_cup = float(input("Enter the price per cup: "))
cups_sold = int(input("Enter the number of cups sold: "))

# PART 4: Define a function that takes arguments and returns the total cost
def calculate_total_cost(price, cups):
    total_cost = price * cups
    return total_cost

# PART 5: Call calculate_total and store the value it returns
total_cost = calculate_total_cost(price_per_cup, cups_sold)

# PART 6: use a built-in function to round the total, then print it
total_cost_rounded = round(total_cost, 2)
print("total cost:", total_cost_rounded)

# PART 7: ask how much money the customer paid
amount_paid = float(input("Enter the amount paid by the customer: "))

# PART 8: Define a function that takes arguments and returns the change due
def calculate_change(amount_paid, total_cost):
    change = amount_paid - total_cost
    return change