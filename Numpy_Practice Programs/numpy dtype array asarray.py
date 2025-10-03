import numpy as np

a = [10,2,30]
a = np.array(a,dtype=float)
print(a)

a = [[10,20],[30,40]]

a = np.asarray(a,dtype=int,order = "C")
print(a)

for i in np.nditer(a):
    print(i)


a = np.asarray(a,dtype=int,order = "F")
print(a)

for i in np.nditer(a):
    print(i)
print(a)