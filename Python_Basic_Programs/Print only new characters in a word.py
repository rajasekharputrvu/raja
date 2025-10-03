word = "Programming"

emp = []

for i in word:
    if i not in emp:
        emp.append(i)
         
print("".join(emp))



