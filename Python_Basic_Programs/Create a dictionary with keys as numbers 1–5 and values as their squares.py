#{1:1,2:4,3:9,4:16,5:25}



s = {x:x*2 for x in range(1,5)}

print(s)

e_o = {'even' if x%2 == 0 else 'odd' for x in range(1,10)  }

div_3 = {x: 'Yes'if x%3 == 0 else 'Not' for x in range(1,100)}
      
te = [22, 30, 15, 10, 35]

w={t:'hot' if t > 20 elif t < 20 'cold' else 'too cold' for t in te} 
