#importanto bibliotecas
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#escolha de ensaio
a = int(input(
'''*******************************
   ENSAIOS DE GRANULOMETRIA
*******************************
 1 - Peneiramento Grosso
 2 - Peneiramento Fino
 Insira o ensaio que deseja realizar: '''))
if a == 1:
    # Inserindo variáveis (Peneiramento Grosso)
    ms = float(input('Insira a Massa de Sólidos:'))
    m1 = float(input('Insira a massa retida na peneira de 50 mm: '))
    m2 = float(input('Insira a massa retida na peneira de 38 mm: '))
    m3 = float(input('Insira a massa retida na peneira de 25 mm: '))
    m4 = float(input('Insira a massa retida na peneira de 19 mm: '))
    m5 = float(input('Insira a massa retida na peneira de 9.5 mm: '))
    m6 = float(input('Insira a massa retida na peneira de 6.3 mm: '))
    m7 = float(input('Insira a massa retida na peneira de 4.8 mm: '))
    m8 = float(input('Insira a massa retida na peneira de 2 mm: '))
    m9 = float(input('Insira a massa retida no prato: '))

    # Criando vetor para diametro das peneiras
    peneiras = ['50', '38', '25', '19', '9.5', '6.3', '4.8', '2', 'prato']

    # Criando vetor das massas retidas
    retida = [m1, m2, m3, m4, m5, m6, m7, m8, m9] 

    # Calculo de Massa Retida Acumulada
    retida_acumulada = []
    count = 1
    valor_atual = 0
    for i in range(0, len(retida)):
        valor_atual = 0
        for j in range(count):
            valor_atual += retida[j]
        count += 1
        retida_acumulada.append(valor_atual)
    
    # Calculo % retida Acumulada
    retida_acum_porcen = []
    for i in range(0,len(retida_acumulada)):
        retida_acum_porcen.append(retida_acumulada[i]*100/ms)

    # Calculo % que passa 
    passa_acum = []
    for i in range(0,len(retida_acum_porcen)):
        passa_acum.append(100-retida_acum_porcen[i])

    # Criando Matriz
    d = {'Diâmetros': peneiras, 'massa retida': retida, 'massa retida acumulada': retida_acumulada, '% retida acumulada': retida_acum_porcen, '% que passa': passa_acum }
    dados = pd.DataFrame(data = d)
    blankIndex=[''] * len(dados)
    dados.index=blankIndex
    print(dados)

    # Criando Plot de Gráfico
    x = [50, 38, 25, 19, 9.5, 6.3, 4.8, 2, 0]
    y = passa_acum

    plt.plot(x,y)
    plt.xscale("log")
    plt.yscale("linear")
    plt.show()

elif a == 2: 
    ms = float(input('Insira a Massa de Sólidos (em g): '))
    m1 = float(input('Insira a massa retida na #16 (em g): '))
    m2 = float(input('Insira a massa retida na #30 (em g): '))
    m3 = float(input('Insira a massa retida na #40 (em g): '))
    m4 = float(input('Insira a massa retida na #50 (em g): '))
    m5 = float(input('Insira a massa retida na #70 (em g): '))
    m6 = float(input('Insira a massa retida na #100 (em g): '))
    m7 = float(input('Insira a massa retida na #200 (em g): '))
    m8 = float(input('Insira a massa retida no prato (em g): '))

    # Criando vetor para diametro das peneiras
    peneiras = ['#16', '#30', '#40', '#50', '#70', '#100', '#200', 'prato']

    # Criando vetor das massas retidas
    retida = [m1, m2, m3, m4, m5, m6, m7, m8] 

    # Calculo de Massa Retida Acumulada
    retida_acumulada = []
    count = 1
    valor_atual = 0
    for i in range(0, len(retida)):
        valor_atual = 0
        for j in range(count):
            valor_atual += retida[j]
        count += 1
        retida_acumulada.append(valor_atual)
    
    # Calculo % retida Acumulada
    retida_acum_porcen = []
    for i in range(0,len(retida_acumulada)):
        retida_acum_porcen.append(retida_acumulada[i]*100/ms)

    # Calculo % que passa 
    passa_acum = []
    for i in range(0,len(retida_acum_porcen)):
        passa_acum.append(100-retida_acum_porcen[i])

    # Criando Matriz
    d = {'Diâmetros': peneiras, 'massa retida': retida, 'massa retida acumulada': retida_acumulada, '% retida acumulada': retida_acum_porcen, '% que passa': passa_acum }
    dados = pd.DataFrame(data = d)
    blankIndex = [''] * len(dados)
    dados.index = blankIndex
    print(dados)

    # Criando Plot de Gráfico
    x = [1.18, 0.59, 0.42, 0.30, 0.21, 0.15, 0.074, 0]
    y = passa_acum

    plt.plot(x,y)
    plt.xscale("log")
    plt.yscale("linear")
    plt.show()

else:
    print('Numero inválido! Tente Novamente!')

