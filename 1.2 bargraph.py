import matplotlib.pyplot as plt
x=["A","B","C","D"]
y=[1000,1800,800,1200]
plt.bar(x,y,color="pink",label="Sales 2025")
plt.legend(loc=2,fontsize=10)
plt.ylim(0,1800)
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales Comparison")
plt.show()


# use barh for horizontal data  