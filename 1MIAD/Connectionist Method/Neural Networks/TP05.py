import numpy as np
import random
import matplotlib.pyplot as plt

Table = []
def fill ():
    for indx in range(100):
        X.append([0] * 3)
        Y.append([0] * 1)
        YP.append([0] * 1)
    W.append([0] * 1 )
    W.append([1] * 1 )
    W.append([2] * 1 )
    W[0] = float(random.random())
    W[1] = float(random.random())
    W[2] = float(random.random())
    for i in range (100):
        X[i][0] = 1
        X[i][1] = random.random()
        X[i][2] = random.random()
        if (i<=50):
            Y[i] = 0
        else:
            Y[i] = 1

def Sigmoide(IN):
    return 1/(1+np.exp(-IN))

def learn(X,Y,w,e,dw,n) :
    # for i in range(n) : # répétons n fois
    w = descend(X,Y,w,e,dw) # effectuons un pas
    LW.append(L(X,Y,w))
    print(L(X,Y,w)) # imprimons la valeur du coût
    return w # on renvoie le vecteur de poids
    
def descend(X,Y,w,e,dw) :
    g = gradient(X,Y,w,dw) # calcul du vecteur de gradient
    w[0] = w[0] - e*g[0] # mise à jour de w[0]
    w[1] = w[1] - e*g[1] # mise à jour de w[1]
    return w # on renvoie le nouveau vecteur de paramètres

def gradient(X,Y,w,dw) :
    h = L(X,Y,w) # calcul du coût
    wa = [0,0] # crée un vecteur wa
    wa[0] = w[0] + dw # perturbation de la 1re coordonnée
    wa[1] = w[1]
    a = L(X,Y,wa) # calcul du coût après perturbation
    wb = [0,0] # crée un vecteur wb
    wb[0] = w[0]
    wb[1] = w[1] + dw # perturbation de la 2e coordonnée
    b = L(X,Y,wb) # calcul du coût après perturbation
    g = [0,0] # crée un vecteur g
    g[0] = (a-h)/dw # pente dans la 1re coordonnée
    g[1] = (b-h)/dw # pente dans la 2e coordonnée
    return g # retourne le vecteur de gradient

def L(X,Y,w) :
    s = 0
    for i in range(0,2) :
        # print(i)
        s = s + pow(Y[i]-YP[i],2)
    return s/2
# /////////////////   PROGRAMME PRINCIPAL    //////////////////////////
# X : Tableau des entrées
# Y : Tableau des sorties désirées
# W : vecteur des poids
# e : Pas du gradient
# dw : Perturbation
# YP : Tabelau des sorties calculées
X = []
Y = []
YP = []
LW=[]
W=[]
fill()
e=0.01
dw=0.01
n=10
print("Winitial[ 1 , 2 , 3 ]")
print(W)
for epoch in range(n):
    print(f'============Epoch {epoch+1}=====================')
    for i in range(len(X)):
        input_ = X[i][0] * W[0] + X[i][1] * W[1] + X[i][2] * W[2]
        output = Sigmoide(input_)
        YP[i] = output
        error = Y[i] - output
    T = learn (X,Y,W,e,dw,n)
print("Affichage des poids optimals :")
print("Wfinal[ 0, 1,  2  ]:")
print(T)
plt.plot(LW)
plt.show()



