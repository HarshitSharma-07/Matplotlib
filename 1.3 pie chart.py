import matplotlib.pyplot as plt

regions=["EAST","WEST","NORTH","SOUTH"]
data=[234,432,456,765]
plt.pie(data,labels=regions,autopct="%1.1f%%",colors=["gold","pink","red","orange"])
plt.title("Revenue contribution  by region")
plt.show()