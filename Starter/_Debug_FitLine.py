import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [3,5,7,9] # 10, not 9, so the fit isn't perfect

coef = np.polyfit(x,y,1)
print(coef)