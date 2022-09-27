from scipy import stats
import numpy as np
from random import randint

x = [1,2,3,4]
y = [3,5,7,9]

coef = np.polyfit(x,y,1)
print(coef)
print(stats.linregress(x,y))
print(stats.pearsonr(x,y))

x = [0,1,2,3]
y = [randint(0,100),randint(0,100),randint(0,100),randint(0,100)]

coef = np.polyfit(x,y,1)
print(coef)
print(stats.linregress(x,y))
print(stats.pearsonr(x,y))