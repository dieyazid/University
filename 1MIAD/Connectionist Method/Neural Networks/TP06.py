import numpy as np
import random

def sigmoide(x):
    return 1/(1+np.exp(-x))

def sum(x1,x2,w0,w1,w2):
    return w0+x1*w1+x2*w2

bais=1
taux=0.1
w = np.random.rand(9)
x1,x2 = np.random.rand(2)

def afficher():
    y1 = sigmoide(sum(x1,x2,w[0],w[1],w[4]))
    y2 = sigmoide(sum(x1,x2,w[3],w[2],w[5]))
    s = sigmoide(sum(y1,y2,w[6],w[7],w[8]))
    print("S = "+str(s))

#ei(n) = s-y
def Ei(S,Y):
    return S-Y

#wij(n) = wij(n-1) + delta_wij(n) 
def Wij(w,y,s,x):
    return w + Delta_Wij(s,y)

#delta_wij(n) = taux *eta_i(n) * yi(n)
def Delta_Wij(s,y):
    return taux * Eta_i(s,y) * y

#eta_i(n) = ei(n) * yi(n) [1-yi(n)]
def Eta_i(s,y):
    return Ei(s,y) * y * (1-y)

#retropropation
def retropropagation():
    global w
    y1 = sigmoide(sum(x1,x2,w[0],w[1],w[4]))
    y2 = sigmoide(sum(x1,x2,w[3],w[2],w[5]))
    s = sigmoide(sum(y1,y2,w[6],w[7],w[8]))
    w[0] = Wij(w[0],y1,s,x1)
    w[1] = Wij(w[1],y1,s,x2)
    w[2] = Wij(w[2],y2,s,x1)
    w[3] = Wij(w[3],y2,s,x2)
    w[4] = Wij(w[4],y1,s,bais)
    w[5] = Wij(w[5],y2,s,bais)
    w[6] = Wij(w[6],s,1,y1)
    w[7] = Wij(w[7],s,1,y2)
    w[8] = Wij(w[8],s,1,bais)
    print("weights: "+str(w))
    afficher()

print("===========Propagation==================")
print("weights: "+str(w))
print("x1: %f \nx2: %f"% (x1,x2))
afficher()
print("===========Retro-Propagation============")
retropropagation()


