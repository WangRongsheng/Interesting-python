import numpy as np
import matplotlib.pyplot as plt
import math

x0 = 0
y0 = 1
h = 0.1
N = 10

# 公式
def func(x,y):
    return (2*x*(y**(-2)))/3
# 欧拉（Euler）公式
def Euler():
    x1 = np.zeros(N+1)
    y1 = np.zeros(N+1)
    for i in range(N+1):
        x1[i] = x0 + h*(i)
    # 计算y数组各值
    for i in range(N+1):
        if i==0:
            y1[i] = y0
        else:
            y1[i] = y1[i-1] + h*func(x1[i-1],y1[i-1])
    return x1,y1
# 改进的欧拉（Euler）公式
def ImproEuler():
    x1 = np.zeros(N+1)
    y1 = np.zeros(N+1)
    for i in range(N+1):
        x1[i] = x0 + h*(i)
    # 计算y数组各值
    for i in range(N+1):
        if i==0:
            y1[i] = y0
        else:
            k1 = y1[i-1] + h*func(x1[i-1],y1[i-1])
            k2 = y1[i-1] + h*func(x1[i],k1)
            y1[i] = (k1+k2)*1/2
    return x1,y1
# 四阶龙格-库塔(Runge-Kutta)方法
def RungeKutta():
    x1 = np.zeros(N+1)
    y1 = np.zeros(N+1)
    for i in range(N+1):
        x1[i] = x0 + h*(i)
    for i in range(N+1):
        if i==0:
            y1[i] = y0
        else:
            k1 = func(x1[i-1],y1[i-1])
            k2 = func(x1[i-1]+h/2,y1[i-1]+k1*h/2)
            k3 = func(x1[i-1]+h/2,y1[i-1]+k2*h/2)
            k4 = func(x1[i-1]+h,y1[i-1]+h*k3)
            y1[i] = y1[i-1] + (k1+2*k2+2*k3+k4)*h/6
    print(x1,y1)
    return x1,y1
def Draw():
#三条线画在同一张图中
    aEuler,bEuler = Euler()
    xEuler,yEuler = ImproEuler()
    xKutta,yKutta = RungeKutta()
    plt.title(r'Euler or ImproEuler or RK', fontsize=20)
    plt.plot(aEuler,bEuler,'+',xEuler,yEuler,'*',xKutta,yKutta,'gx')#,xEuler,((1+(xEuler**2))^(1/3)),'r')
    plt.legend(['Euler', 'ImproEuler','RK'], loc = 'upper right') 
    plt.grid(True)
    plt.savefig('ODE test',dpi = 600)
    plt.show()
if __name__ == '__main__':
    Draw()
