# input = "Python is cool"

# vowels = "aeiouAEIOU"

# emprty = ""

# for i in input:
#     if i in vowels:
#         emprty += "*"
#     else:
#         emprty +=i


# print(emprty)

input = "Python is cool"

vowels = "aeiouAEIOU"

empty = ""

for i in input:
    if i not in vowels:
        empty += '*'
    else:
        empty += i
print(empty)

