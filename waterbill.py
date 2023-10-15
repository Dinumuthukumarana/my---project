# Constants
BASE_CHARGE = 20  # Base charge for water service
COST_PER_GALLON = 0.01  # Cost per gallon of water used

# Input from the user
usage_in_gallons = float(input("Enter the usage in gallons: "))

# Calculating the bill
water_charge = BASE_CHARGE + (usage_in_gallons * COST_PER_GALLON)

# Output
print(f"The water bill is: ${water_charge:.2f}")
