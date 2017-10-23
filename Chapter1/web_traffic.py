import scipy as sp
import matplotlib.pyplot as plt
data = sp.genfromtxt("web_traffic.tsv")

print(data.shape)
x = data[:,0]
y = data[:,1]
z = sp.sum(sp.isnan(y))
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x,y)
plt.title("web_traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hours")
plt.xticks([w*7*24 for w in range(10)],
	['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

#计算误差
def error(f,x,y):
	return sp.sum((f(x)-y)**2)

#基线模型
fx = sp.linspace(0,x[-1])

