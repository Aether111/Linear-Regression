import numpy as np
import matplotlib.pyplot as plt

def compute_error(slope,y_int,X):
    v_dist = [] # Vertical Distance
    for coord in X:
        line_y = slope*coord[0]+y_int
        v_dist.append(line_y-coord[1])
    mse = 0
    for y in v_dist:
        mse += (y**2)/2
    return mse

X = np.zeros([100,2],dtype='float')
for b in range(100):
    X[b] = [b,(-1.5)*b+1]
    
rng = np.random.default_rng()
vals = rng.standard_normal(len(X))

for point in range(len(X)):
    X[point,1] += 10*vals[point]

print(X)

slope = np.arange(-20,20,0.05)#0.05 * (s + 1)

y_int = np.arange(-10,10,0.5)#0.5 * i - 10

mse_list = []
slope_list = []
for s in slope:
    for i in y_int:
        mse_list.append(compute_error(round(s,3),round(i,3),X))
        slope_list.append([round(s,3),round(i,3)])

best = np.argmin(mse_list)
print(best,mse_list[best],slope_list[best],sep=" ")

plt.scatter(X[:,0],X[:,1],s=1)
plt.grid(True)
plt.axis("Equal")
plt.plot([np.min(X[:,0]),np.max(X[:,0])],[slope_list[best][0]*np.min(X[:,0])+slope_list[best][1],slope_list[best][0]*np.max(X[:,0])+slope_list[best][1]])
