items = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# print(items[1:-1:2])

emp = []

for i in range(1,len(items)-1,2):
    emp.append(items[i])

print(emp)


