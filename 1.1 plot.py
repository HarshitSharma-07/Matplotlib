import matplotlib.pyplot as plt

x=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]
y=[12,32,43,65,75,57]

plt.plot(x,y,color="orange",linestyle="--",linewidth=2,marker="x",label="random graph")
plt.title("Bakery Sales This Week")
plt.xlabel("Day of the week")
plt.ylabel("Sales")
plt.title("ANT SHANT DATA")
plt.legend(loc=3,fontsize=15)
plt.grid(linestyle=":",color="blue",linewidth=2)
plt.xlim(0,5)
plt.ylim(0,100)
plt.xticks([1,2,3,4,5,6],["A","B","C","D","E","F"])
plt.show()

