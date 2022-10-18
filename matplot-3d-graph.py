from tkinter import PROJECTING
from matplotlib import pyplot as plt

axis_x=[0,10,20,30,40,50,60,70,80,90,100]
axis_y=[0,10,20,30,40,50,60,70,80,90,100]
axis_z=[0,10,20,30,40,50,60,70,80,90,100]

x=plt.axes(projection='3d')  #to specify the no. of dimensions

# n_axis_x=[0,10,20,30,40,50,60,70,80,90,100]
# n_axis_y=[0,-10,-20,-30,-40,-50,-60,-70,-80,-90,-100]

plt.plot(axis_x,axis_y,axis_z)
# plt.plot(n_axis_x,n_axis_y)

plt.xlabel('shit x-axis')
plt.ylabel('shit y-axis')


plt.legend(['first shit','second shit'])
plt.title('shit')
plt.show()
