import numpy as np

x = [1,2,3,4]
y = [3,5,7,9]

coef = np.polyfit(x,y,1)
print(coef)


x = [0,1,2,3]
y = [3,5,7,9]

coef = np.polyfit(x,y,1)
print(coef)