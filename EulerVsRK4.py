#Euler method Vs RK4 method
#which one is more accurate
import math
import matplotlib.pyplot as plt

xf=10
xo=0
n=400
x=[xo]
h=math.sqrt((xf-xo)**2)/n
i=0
zo=1
z=[zo]
yo=0
z2=[zo]
y=[yo]
y2=[yo]
j=0





#-------------p(x)d2y/dx2+q(x)dy/dx+l(x)y=0-------
def p(x):
    return 1

def q(x):
    return 0

def l(x):
    return 1

#---------------------building x-axis----------------------
while i != n:
    x.append(round(x[i]+h,4))
    i+=1

#-------------------------Euler method----------------
def zed(t):
    return -((q(x[t])*z[t]+l(x[t])*y[t])*h/p(x[t]))+z[t]
def wye(t):
    return y[t]+z[t]*h


#------------------------Iteration ALGORITHM---------

while j+1 != len(x):
    z.append(round(zed(j),4))
    y.append(round(wye(j),4))
    j+=1

#--------------------RK4-----------------------------

def k1(t):
    return z2[t]
def m1 (t):
    return z2[t]

def k2(t):
    return (z2[t]+h*k1(t)/2)
def m2 (t):
    return z2[t]+(1/2)*h*k1(t)


def k3(t):
    return (z2[t]+h*k2(t)/2)
def m3(t):
    return z2[t]+(h/2)*k2(t)

def k4(t):
    return (y2[t]+h*k3(t))
def m4(t):
    return z2[t]+h*k3(t)

def zed2(t):
    return -((q(x[t])*z2[t]+l(x[t])*y2[t])*h/p(x[t]))+z2[t]

def wye2(t):
    return y2[t]+(h/6)*(m1(t)+2*m2(t)+2*m3(t)+m4(t))


#-----------------------------------------
j=0
while j+1 != len(x):
    z2.append(round(zed2(j),4))
    y2.append(round(wye2(j),4))
    j+=1


#-----------------------PLOTING RESULTS-------------
plt.plot(x,y)
plt.plot(x,y2)

plt.show()


