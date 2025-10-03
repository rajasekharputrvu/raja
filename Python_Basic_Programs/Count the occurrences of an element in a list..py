from collections import Counter

# Sample list
my_list = [2, 3, 2, 3, 3, 4, 5, 3]

# Count each element
counter = Counter(my_list)
print(counter)

# Print the results
for element, count in counter.items():
    print(f"{element} appears {count} times")








