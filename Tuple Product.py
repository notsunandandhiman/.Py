def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

# Example tuple
numbers_tuple = (2, 3, 4, 5)

# Calculate the product
result = calculate_product(numbers_tuple)

# Print the result
print(f"The product of the numbers in the tuple {numbers_tuple} is: {result}")