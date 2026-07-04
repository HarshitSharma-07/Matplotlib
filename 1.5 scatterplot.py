import matplotlib.pyplot as plt

xdata=[1,2,3,4,5,6,7,8]
ydata=[10,20,30,40,50,60,70,80]

plt.scatter(xdata,ydata,color="red",label="Random data",marker="^")
plt.scatter(ydata,xdata,color="orange",label="Random data",marker="^")
plt.grid(color="gray",linewidth=0.3)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Ant Shant data part-2")
plt.legend()
plt.show()