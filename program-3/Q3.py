# Electricity Bill Generator

# Accept consumer details
consumer_name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")

previous_reading = float(input("Enter Previous Meter Reading (kWh): "))
current_reading = float(input("Enter Current Meter Reading (kWh): "))
cost_per_unit = float(input("Enter Cost per Unit (₹): "))

# Calculate total units consumed
units_consumed = current_reading - previous_reading

# Calculate energy charge
energy_charge = units_consumed * cost_per_unit

# Calculate electricity duty (5% of energy charge)
electricity_duty = 0.05 * energy_charge

# Fixed meter charge
fixed_charge = 100

# Calculate net bill amount
net_bill = energy_charge + electricity_duty + fixed_charge

# Display the electricity bill
print("\n============================================")
print("          ELECTRICITY BILL")
print("============================================")
print(f"Consumer Name       : {consumer_name}")
print(f"Consumer ID         : {consumer_id}")
print(f"Previous Reading    : {previous_reading:.2f} kWh")
print(f"Current Reading     : {current_reading:.2f} kWh")
print(f"Units Consumed      : {units_consumed:.2f} kWh")
print(f"Cost Per Unit       : ₹{cost_per_unit:.2f}")
print("--------------------------------------------")
print(f"Energy Charge       : ₹{energy_charge:.2f}")
print(f"Electricity Duty    : ₹{electricity_duty:.2f}")
print(f"Fixed Meter Charge  : ₹{fixed_charge:.2f}")
print("--------------------------------------------")
print(f"NET BILL AMOUNT     : ₹{net_bill:.2f}")
print("============================================")
