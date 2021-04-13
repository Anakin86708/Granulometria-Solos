#importanto bibliotecas
import math
import numpy as np
import pandas as pd
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
    peneiras = ['50', '38', '25', '19', '9.5', '6.3', '4.8', '2', 'fundo']

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
  
elif a == 2: 
    m1 = float(input('Insira a massa retida na #16:___ g'))
    m2 = float(input('Insira a massa retida na #30:___ g '))
    m3 = float(input('Insira a massa retida na #40:___ g '))
    m4 = float(input('Insira a massa retida na #50:___ g '))
    m5 = float(input('Insira a massa retida na #70:___ g '))
    m6 = float(input('Insira a massa retida na #100:___ g '))
    m7 = float(input('Insira a massa retida na #200:___ g '))
    m8 = float(input('Insira a massa retida no prato:___ g '))
else:
    print('Numero inválido! Tente Novamente!')

