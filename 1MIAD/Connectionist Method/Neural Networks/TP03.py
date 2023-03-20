import math
import random


Table=[]
w0=random.uniform(0,1)
w1=random.uniform(0,1)
w2=random.uniform(0,1)
epsilon=1


def Fill_Tables():
    for i in range(0,100):
        if i+1<=50:
            E1=random.uniform(-10,10)
            E2=random.uniform(-10,10)
            output=1
            Table.append([E1,E2,output])
        else:
            E1=random.uniform(-10,10)
            E2=random.uniform(-10,10)
            output=0
            Table.append([E1,E2,output])

def Sigmoide(IN):
    return 1/(1+math.exp(-IN))

def Widrow_Hoff(w0,w1,w2):
    w0=w0+epsilon*(out-calc_out)*1
    w1=w1+epsilon*(out-calc_out)*E1
    w2=w2+epsilon*(out-calc_out)*E2
    return w0,w1,w2

def Hebb(w0,w1,w2):
    w0=w0+epsilon*calc_out*1
    w1=w1+epsilon*calc_out*E1
    w2=w2+epsilon*calc_out*E2
    return w0,w1,w2

Fill_Tables()
for i in range(0,len(Table)):
    print(f'========[ Result {i+1} ]===========')
   
    E1=Table[i][0]
    E2=Table[i][1]
    
    out=Table[i][2]
    input_=w0+E1*w1+E2*w2
    calc_out=Sigmoide(input_)
    
    print(f'Entree 1 = {round(E1,2)} \nEntree 2 = {round(E2,2)} \nw0={round(w0,2)} \nw1={round(w1,2)} \nw2={round(w2,2)}')
    print(f'Sortie prevue = {out}')
    print(f'Sortie calculee = {calc_out}')
    
    if calc_out==out:
        print('Le reseau pour cette donnee est conforme')
    else:
        print('Le reseau pour cette donnee est non conforme')
        while calc_out!=out:
            w0,w1,w2=Widrow_Hoff(w0,w1,w2)
            input_=w0+E1*w1+E2*w2
            calc_out=Sigmoide(input_)
        print(f'Nouveau w0 = {round(w0,2)} \nNouveau w1 = {round(w1,2)} \nNouveau w2 = {round(w2,2)}')
        print(f'Sortie de nouveau calcule = {calc_out}')
