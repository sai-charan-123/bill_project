# Define the cost of the HP laptop
HP_LAPTOP_COST = 50000

# Define the tax rates
SGST = 10 / 100
CGST = 10 / 100

# Print the header
print("------- We are selling HP Laptop --------")
print("------- Each costs ₹", HP_LAPTOP_COST, "---------------")

# Get the number of items required
required_items = int(input("No. of required items: "))

# Apply discount based on quantity
if 2 <= required_items <= 5:
    discount = 5 / 100
elif 5 <= required_items <= 10:
    discount = 10 / 100
elif 11 <= required_items <= 20:
    discount = 18 / 100
elif 21 <= required_items <= 40:
    discount = 24 / 100
elif required_items >= 41:
    discount = 33 / 100
else:
    discount = 2 / 100

# Calculations
HP_total_cost = required_items * HP_LAPTOP_COST
HP_SGST = HP_total_cost * SGST
HP_CGST = HP_total_cost * CGST
HP_discount_amount = HP_total_cost * discount

# Calculate the total cost
total_cost = HP_total_cost + HP_SGST + HP_CGST - HP_discount_amount

# Output
print("------------ Billing Summary --------------------")
print(" Total Laptop Cost : ₹", HP_total_cost)
print(" SGST (10%) : ₹", HP_SGST)
print(" CGST (10%) : ₹", HP_CGST)
print(" Discount Applied (", discount * 100, "%) : ₹", HP_discount_amount)
print("-------------------------------------------------")
print(" Total Payable Amount : ₹", total_cost)
print("-------------------------------------------------")
print(".<.<.< THANK YOU AND VISIT AGAIN >.>.>.")