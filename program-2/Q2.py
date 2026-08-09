# Mathematical Calculator using Built-in Functions and Math Module

import math

# Accept a floating-point number
num = float(input("Enter a floating-point number: "))

# Perform mathematical operations
square = num ** 2
cube = num ** 3
square_root = math.sqrt(num)
ceiling_value = math.ceil(num)
floor_value = math.floor(num)
absolute_value = abs(num)
variable_type = type(num)
memory_address = id(num)

# Display the results
print("\n========== MATHEMATICAL CALCULATOR ==========")
print(f"Number         : {num}")
print(f"Square         : {square}")
print(f"Cube           : {cube}")
print(f"Square Root    : {square_root:.2f}")
print(f"Ceiling Value  : {ceiling_value}")
print(f"Floor Value    : {floor_value}")
print(f"Absolute Value : {absolute_value}")
print(f"Type           : {variable_type}")
print(f"Memory Address : {memory_address}")
