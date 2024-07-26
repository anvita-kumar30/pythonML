# SIMPLE LINEAR REGRESSION
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("Experience-Salary.csv",converters={"exp(in months)":int()})
# y = Bo + Bi X
x= data['exp(in months)']
print(x)
y = data['salary(in thousands)']
plt.scatter(x,y)
plt.show
mean_x = np.mean(x)
mean_y = np.mean(y)
print(mean_y)
numerator =0
denominatr =0
L = len(x)
for i in range(L):
    ab = (x[i]-mean_x)*(y[i]-mean_y)
    cd = (x[i]-mean_x)**2
    numerator += ab
    denominatr += cd
ans = numerator/denominatr
print(ans)
reg = mean_y - (ans * mean_x)
max_X = np.max(x) +100
min_y = np.min(y) -100
X = np.linspace(max_X,min_y,100)
Y = reg + ans*X
plt.plot(X,Y,color='green')
plt.scatter(x,y)
plt.xlabel("op")
plt.ylabel('sal')
plt.legend()
plt.show()