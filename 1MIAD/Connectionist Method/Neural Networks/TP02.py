import random

def Seuil(IN):
    if IN>0:
        return 1
    else:
        return 0

for i in range(0,100):
    a=random.uniform(0,1)
    b=random.uniform(0,1)
    w0=random.uniform(-1,1)
    w1=random.uniform(-1,1)
    w2=random.uniform(-1,1)
    print(f'========[ Result {i+1} ]===========')
    print(f'a={round(a,2)} \nb={round(b,2)} \nw0={round(w0,2)} \nw1={round(w1,2)} \nw2={round(w2,2)}')
    input_=w0+a*w1+b*w2
    print(f'Output = {Seuil(input_)}')
