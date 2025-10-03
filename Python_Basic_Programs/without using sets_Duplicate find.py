list1 = [1, 2, 2, 3, 4]
list2 = [2, 2, 3, 5]

emp = []
for i in list1:
    if i in list2:
        emp.append(i)
print(emp)


