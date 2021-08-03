# -*- coding: utf-8 -*-
"""
@author: Daniel

"""

from math import exp
import matplotlib.pyplot as plt
import numpy as np

    
def f(t,y):
    func=t*exp(3*t)-2*y
    return func

def RK4(t0,y0,h,n):
    t=np.zeros(n+1)
    y=np.zeros(n+1)
    t[0]=t0
    y[0]=y0
    print('y(',t,')=',y)
    
    for k in range(n):
        k1=f(t[k],y[k])
        k2=f(t[k]+h/2,y[k]+(h/2)*k1)
        k3=f(t[k]+h/2,y[k]+(h/2)*k2)
        k4=f(t[k]+h,y[k]+h*k3)
        y[k+1]=y[k]+(h/6)*(k1+2*k2+2*k3+k4)
        t[k+1]=t[k]+h
        print('y(',round(t[k+1],3),')=',y[k+1])
        
    plt.plot(t,y)

val=exp(3)/5-exp(3)/25+51*exp(-2)/25
RK4(0,2,0.01,100)
print(val)