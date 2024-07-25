
import math as m
import numpy as np


# READ ME
# READ ME
# READ ME
# for single ODE, just SET a1, b2 and y1_prime to desire function AND SET y2_prime = 0



def f(a1, b1, a2, b2):  ### need to set y_prime and y2_prime manually, a1b1 = x1y1, a2b2 = x2y2
    y1_prime = a1 + 2 - b1
    y2_prime =  0
    ans = np.array([y1_prime, y2_prime])
    
    return ans

#index for looping
i = 1

#determine limit
x_initial = 0
x_final = 1

#finding h, n is number of division
n = 10
h = (x_final - x_initial)/10

x1 = 0 
y1 = 2 #y1
x2 = 0
y2 = 0 #y2

y0 = (y1, y2)

k1 = f(x1, y1, x2, y2) 

k2 = f(x1+(1/4)*h, y1+(1/4)*k1[0]*h, x2+(1/4)*h, y2+(1/4)*k1[1]*h)

k3 = f(x1+(3/8)*h,y1+(3/32)*h*(k1[0]+3*k2[0]), x2+(3/8)*h, y2+(3/32)*h*(k1[1]+3*k2[1]))

k4 = f(x1+(12/13)*h, y1+(12/2197)*h*(161*k1[0]-600*k2[0]+608*k3[0]), x2+(12/13)*h, y2+(12/2197)*h*(161*k1[1]-600*k2[1]+608*k3[1]))

k5 = f(x1+h, y1+(1/4104)*h*(8341*k1[0]-32832*k2[0]+29440*k3[0]-845*k4[0]), x2+h, y2+(1/4104)*h*(8341*k1[1]-32832*k2[1]+29440*k3[1]-845*k4[1]))

k6 = f(x1+(0.5)*h,y1+h*(-(8/27)*k1[0]+2*k2[0]-(3544/2565)*k3[0]+(1859/4104)*k4[0]-(11/40)*k5[0]), x2+(0.5)*h, y2+h*(-(8/27)*k1[1]+2*k2[1]-(3544/2565)*k3[1]+(1859/4104)*k4[1]-(11/40)*k5[1])) 

y_next= y0 + 1/5*((16/27)*k1+(6656/2565)*k3+(28561/11286)*k4-(9/10)*k5+(2/11)*k6)*h 

#print(k1)
#print(k2)
#print(k3)
#print(k4)
#print(k5)
#print(k6)

print("\n")

#global error, enter exact solution
def exact(a):
    f = a + 1 + m.exp(-a)
   
    
    return f

f_exact = exact(x1+h) 

error = y_next[0] - f_exact


#print("======= Results =========")
#print("y = ", y_next)
#print("exact solution = ", f_exact)
#print("error = " ,error)





for i in range(2,n+2):

    y0 = (y1, y2)

    k1 = f(x1, y1, x2, y2) 

    k2 = f(x1+(1/4)*h, y1+(1/4)*k1[0]*h, x2+(1/4)*h, y2+(1/4)*k1[1]*h)

    k3 = f(x1+(3/8)*h,y1+(3/32)*h*(k1[0]+3*k2[0]), x2+(3/8)*h, y2+(3/32)*h*(k1[1]+3*k2[1]))

    k4 = f(x1+(12/13)*h, y1+(12/2197)*h*(161*k1[0]-600*k2[0]+608*k3[0]), x2+(12/13)*h, y2+(12/2197)*h*(161*k1[1]-600*k2[1]+608*k3[1]))

    k5 = f(x1+h, y1+(1/4104)*h*(8341*k1[0]-32832*k2[0]+29440*k3[0]-845*k4[0]), x2+h, y2+(1/4104)*h*(8341*k1[1]-32832*k2[1]+29440*k3[1]-845*k4[1]))

    k6 = f(x1+(0.5)*h,y1+h*(-(8/27)*k1[0]+2*k2[0]-(3544/2565)*k3[0]+(1859/4104)*k4[0]-(11/40)*k5[0]), x2+(0.5)*h, y2+h*(-(8/27)*k1[1]+2*k2[1]-(3544/2565)*k3[1]+(1859/4104)*k4[1]-(11/40)*k5[1])) 

    y_next= y0 + 1/5*((16/27)*k1+(6656/2565)*k3+(28561/11286)*k4-(9/10)*k5+(2/11)*k6)*h 

    f_exact = exact(x1+h) 

    error = y_next[0] - f_exact


    print("\n\n======= Results =========")
    print("x =" ,round(x1+h, 1))
    print("Y =" , y_next[0])
    print("exact solution =", f_exact)
    print("error =" ,error)

    x1 = x1 + h  
    y1 = y_next[0]
    x2 = x2 + h
    y2 = y_next[1]

