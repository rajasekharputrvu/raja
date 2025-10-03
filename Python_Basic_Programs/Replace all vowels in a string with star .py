string = "RajsekharPutrevu Cheemalavalasa Village"
vowels = "aeiouAEIOU"
result = ""

for i in string:
    if i in vowels:
        result += '*'
    else:
        result += i

print(result)

