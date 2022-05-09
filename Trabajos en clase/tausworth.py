import pandas as pd

q=int(input("Ingrese el valor de q: "))
h=int(input("Ingrese el valor de h: "))
l=int(input("Ingrese el valor de l: "))
nBits=int(input("Ingrese el numero de bits con el que decea trabajar: "))

generador=[]
conversion=[]
result=0

vector_l=list(range(l))
vector_l.reverse()

if h<q:
    for i in range(1,len(list(range(1,nBits+1)))+1):
        if i<=q:
            generador.append(1)
        else:
            aux1=i-(h+1)
            aux2=i-(q+1)
            generador.append((generador[aux1]+generador[aux2])%2)

    for i in range(l,len(generador)+1,l):
        fragmento=generador[i-l:i]
        for j in range(len(fragmento)):
            result+=fragmento[j]*2**vector_l[j]
        conversion.append(result)
        result=0

    df = pd.DataFrame(generador,index=list(range(1,41)))

    print(df)
    print(conversion)

else:
    print("el valor de h tiene que ser menor a q")