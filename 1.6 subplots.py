import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
plt.subplot(1,2,1)  #1 row, 2 cloumn, 1subplot
plt.plot(x,y,color="brown")
plt.title("Line chart")


plt.subplot(1,2,2)  #1 row, 2 cloumn, 2subplot
plt.bar(x,y,color="pink")
plt.title("Bar Chart")
# plt.tight_layout()
plt.show()


# But if you want more control over the graphs, you can use this method...

fig,ax=plt.subplot(1,2,figsize=(10,15))

ax[0].plot(x,y)
ax[0].set_title('Line Plot')

ax[1].bar(x,y)
ax[1].title('Bar Chart')
plt.tight_layout()
plt.show()


# id understand this part(complete part)