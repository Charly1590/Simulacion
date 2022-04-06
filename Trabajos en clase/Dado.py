import random
import matplotlib.pyplot as plt

historico={"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0}

def lanzar_dados():

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma=dado1+dado2
    return suma

def repeticiones(n):

    global historico
    for i in range(n+1):
        resultado=lanzar_dados()
        historico[str(resultado)]+=1

def dibujar(n): 

    global historico

    repeticiones(n)
    
    eje_x = list(historico.keys())
    eje_y = list(historico.values())

    plt.figure()
    plt.barh(eje_x, eje_y, color="blue")
    plt.ylabel('Numero')
    plt.xlabel('Repeticiones')
    plt.show()
    print(historico)
    historico={"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0}

dibujar(100)
dibujar(1000)
dibujar(10000)



