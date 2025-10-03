import numpy as np
a = b"welcome to numpy"

a = np.frombuffer(a,dtype = "S1",count=2,offset=9)
print(a)
