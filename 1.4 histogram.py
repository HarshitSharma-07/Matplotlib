import matplotlib.pyplot as plt

scores=[10,12,43,34,23,67,43,78,54,78,93,45,85,27,94,74,27,95]
plt.hist(scores,bins=5,color="yellow",edgecolor="Black")
plt.title("Score Distribution Of Students")
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.plot([10,30,50,70,90],[1,2,3,4,5],color="green",linestyle=":",linewidth=2,marker="x",label="Testing graph")
plt.legend(loc=3,fontsize=12)
plt.show()