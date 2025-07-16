# Prompt the user to enter numbers separated by commas
numbers_input = input("Enter numbers separated by commas:\n")

# Split the input string into a list of strings
numbers_input = numbers_input.split(',')

# Show the type of the original input
print(type(numbers_input))

# Convert each string to an integer
numbers_input = [int(num.strip()) for num in numbers_input]

# Print the list of integers
print(numbers_input)







