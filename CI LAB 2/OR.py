def OR(x,y):
    if x==1 or y==1 :
        return 1
    return 0

def activation(x,y):
    w1=1
    w2=1
    b=-0.5
    y=w1*x+w2*y+b
    if y>=0:
        return 1
    return 0

flag=True
ORGATE=[0,1,1,1]
OUTPUT=[]
for x in range (0,2):
    for y in range (0,2):
        if OR(x,y)!=activation(x,y):
            flag=False
        OUTPUT.append(activation(x,y))

print(flag)
print("OR =",ORGATE)
print("SLP =",OUTPUT)

