def count_value_frequency(test_dict, value_to_check):
    # Count the frequency of the specified value in the dictionary
    frequency = sum(1 for v in test_dict.values() if v == value_to_check)
    return frequency

# Example dictionary
test_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1
}

# Value to check
value_to_check = 1

# Get the frequency of the value
frequency = count_value_frequency(test_dict, value_to_check)

print(f"The frequency of the value {value_to_check} in the dictionary is: {frequency}")