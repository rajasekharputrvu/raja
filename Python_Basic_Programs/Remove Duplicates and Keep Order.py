my_list = [1, 2, 2, 3, 4, 3, 5]

lis = []
for i in my_list:
    if i not in lis:
        lis.append(i)

print(lis)

