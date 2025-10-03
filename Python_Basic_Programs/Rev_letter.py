items = ['a', 'b', 'c', 'd', 'e']

emp = []
for i in range(len(items)-1,-1,-1):
    #print(i)
    print(items[i])
    emp.append(items[i])
    print(emp)