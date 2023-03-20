import numpy as np
import random
import matplotlib.pyplot as plt

T=[]
Table = []
w0 = random.uniform(0,1)
w1 = random.uniform(0,1)
w2 = random.uniform(0,1)
epsilon = 0.1
num_epochs = 100
Erreur_Q,Erreur_C=[],[]

def Fill_Tables():
    for i in range(0,100):
        if i+1 <= 50:
            E1 = random.uniform(-10,10)
            E2 = random.uniform(-10,10)
            output = 1
            Table.append([E1, E2, output])
        else:
            E1 = random.uniform(-10,10)
            E2 = random.uniform(-10,10)
            output = 0
            Table.append([E1, E2, output])

def Sigmoide(IN):
    return 1/(1+np.exp(-IN))

def Hebb(w0, w1, w2, calc_out, E1, E2):
    w0 = w0 + epsilon*calc_out*1
    w1 = w1 + epsilon*calc_out*E1
    w2 = w2 + epsilon*calc_out*E2
    return w0, w1, w2

def global_error():
    error = []
    sum_err = 0
    for i in range(len(Table)):
        E1 = Table[i][0]
        E2 = Table[i][1]
        out = Table[i][2]
        input_ = w0 + E1*w1 + E2*w2
        calc_out = Sigmoide(input_)
        error.append(out - calc_out)
        sum_err += (out- calc_out)
    return sum_err,error

def calc_erreur_quadratique(G):
    er=0
    for u in range(0,len(G)):
        er += pow(G[u],2)
    return er/(len(G))

def calc_erreur_carr(T):
    er=0
    for u in range(0,len(T)):
        er += pow(T[u],2)
    return er/2

Fill_Tables()

for epoch in range(num_epochs):
    print(f'============Epoch {epoch+1}=====================')
    for i in range(len(Table)):
        E1 = Table[i][0]
        E2 = Table[i][1]
        out = Table[i][2]
        input_ = w0 + E1*w1 + E2*w2
        calc_out = Sigmoide(input_)
        if calc_out != out:
            w0, w1, w2 = Hebb(w0, w1, w2, calc_out, E1, E2)
    print(f"Les Poids pour epoch {epoch+1}: \nw0={round(w0, 2)}, \nw1={round(w1, 2)}, \nw2={round(w2, 2)}")
    glob_error,error = global_error()
    T.append(glob_error)
    Erreur_Q.append(calc_erreur_quadratique(error))
    Erreur_C.append(calc_erreur_carr(error))
    print(f'Erreur Globale: {glob_error}')
    print("Erreur Quad = ",Erreur_Q[epoch])
    print("Erreur Carr = ",Erreur_C[epoch])

print("=======================================================================")
print("Erreur Quadratique optimal =",min(Erreur_Q))
print("Erreur Carré optimal =",min(Erreur_C))
print("=======================================================================")

# Plot T
plt.plot(T)
plt.xlabel('Epoch')
plt.ylabel('Erreur Global')
plt.title(f'''
Erreur Quadratique optimal =,{min(Erreur_Q)})
Erreur Carré optimal =,{min(Erreur_C)})
''')
plt.show()
