import numpy as np
a=[] 
size=15 # size of the Matrix
leave=5 # Number of leds needed to fold 
if size%2==0:
  for i in range (int(size/2)):
    for j in range (size):
      a.append(j+(i*(2*(size+leave))))
    for k in range (size):
      a.append((((2*size)+leave)*(i+1))-(k+1))
else:
  for i in range (int((size+1)/2)):
    for j in range (size):
      a.append(j+(i*(2*(size+leave))))
    if i==(size-1)/2:
      break
    for k in range (size):
      a.append((((2*size)+leave)*(i+1))-(k+1))
req=np.array(a).reshape(size,size)
print(repr(req))
