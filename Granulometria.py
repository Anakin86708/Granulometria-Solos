# %%
# importanto bibliotecas
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.text import OffsetFrom
from scipy.interpolate import make_interp_spline, BSpline
# %%


def calcular_peneiramento_grosso(ms, m1, m2, m3, m4, m5, m6, m7, m8, m9):
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
    for i in range(0, len(retida_acumulada)):
        retida_acum_porcen.append(retida_acumulada[i]*100/ms)

    # Calculo % que passa
    passa_acum = []
    for i in range(0, len(retida_acum_porcen)):
        passa_acum.append(100-retida_acum_porcen[i])

    # Criando Matriz
    d = {'Diâmetros': peneiras, 'massa retida': retida, 'massa retida acumulada': retida_acumulada,
         '% retida acumulada': retida_acum_porcen, '% que passa': passa_acum}
    dados = pd.DataFrame(data=d)
    blankIndex = [''] * len(dados)
    dados.index = blankIndex
    print(dados)

    # Criando Plot de Gráfico
    x = [50, 38, 25, 19, 9.5, 6.3, 4.8, 2, 0]
    y = passa_acum

    plt.plot(x, y)
    plt.xscale("log")
    plt.yscale("linear")
    plt.show()

# %%


def calcular_peneiramento_fino(ms, m1, m2, m3, m4, m5, m6, m7, m8):
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
    for i in range(0, len(retida_acumulada)):
        retida_acum_porcen.append(retida_acumulada[i]*100/ms)

    # Calculo % que passa
    passa_acum = []
    for i in range(0, len(retida_acum_porcen)):
        passa_acum.append(100-retida_acum_porcen[i])

    # Criando Matriz
    d = {'Diâmetros': peneiras, 'massa retida': retida, 'massa retida acumulada': retida_acumulada,
         '% retida acumulada': retida_acum_porcen, '% que passa': passa_acum}
    dados = pd.DataFrame(data=d)
    blankIndex = [''] * len(dados)
    dados.index = blankIndex
    print(dados)

    # Criando Plot de Gráfico
    x = [1.18, 0.59, 0.42, 0.30, 0.21, 0.15, 0.074, 0]
    y = passa_acum

    fig, ax = plt.subplots()
    ax.plot(x, y, label='amostra 1')
    ax.set_xlabel('Diâmetros(mm)', fontsize=10, verticalalignment='bottom')
    ax.set_xscale('log')
    ax.set_ylabel('% que passa', fontsize=10, verticalalignment='bottom')
    ax.axvline(1.18, 0, 1, color='brown', zorder=-10, linestyle="--", linewidth=0.5)
    ax.axvline(0.59, 0, 1, color='brown', zorder=-10, linestyle="--", linewidth=0.5)
    ax.axvline(0.42, 0, 1, color='brown', zorder=-10, linestyle="--", linewidth=0.5)
    ax.axvline(0.30, 0, 1, color='brown', zorder=-10, linestyle="--", linewidth=0.5)
    ax.axvline(0.21, 0, 1, color='brown', zorder=-10, linestyle="--", linewidth=0.5)
    ax.axvline(0.15, 0, 1, color='brown', zorder=-10, linestyle="--", linewidth=0.5)
    ax.axvline(0.074, 0, 1, color='brown', zorder=-10, linestyle="--", linewidth=0.5)
    ax.grid(linestyle=":", linewidth=0.5, color='.25', zorder=-10)
    ax.annotate('Granulometria',
            xy=(1, 0), xycoords='axes fraction',
            color='black',
            xytext=(-95, 230), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
            size=20 )
    ax.annotate('#16',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-6, 220), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
            size=8 )
    ax.annotate('#30',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-85, 220), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
            size=8 )
    ax.annotate('#40',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-120, 220), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
            size=8 )
    ax.annotate('#50',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-157, 220), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
            size=8 )
    ax.annotate('#70',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-195, 220), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
            size=8 )
    ax.annotate('#100',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-230, 220), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
            size=8 )
    ax.annotate('#200',
            xy=(1, 0), xycoords='axes fraction',
            xytext=(-312, 220), textcoords='offset pixels',
            horizontalalignment='right',
            verticalalignment='bottom',
            size=8 )

    plt.legend()
    plt.show()


# %%

def main():
    
    # a = int(input('teste'))
    a = 2

    if a == 1:
        # Inserindo variáveis (Peneiramento Grosso)
        massa_solidos = 100
        massa_retida_peneira_50mm = 0
        massa_retida_peneira_38mm = 0
        massa_retida_peneira_25mm = 0
        massa_retida_peneira_19mm = 0
        massa_retida_peneira_9_5mm = 0
        massa_retida_peneira_6_3mm = 0
        massa_retida_peneira_4_8mm = 0
        massa_retida_peneira_2mm = 0
        massa_retida_prato = 0

        calcular_peneiramento_grosso(
            massa_solidos,
            massa_retida_peneira_50mm,
            massa_retida_peneira_38mm,
            massa_retida_peneira_25mm,
            massa_retida_peneira_19mm,
            massa_retida_peneira_9_5mm,
            massa_retida_peneira_6_3mm,
            massa_retida_peneira_4_8mm,
            massa_retida_peneira_2mm,
            massa_retida_prato
        )

    elif a == 2:
        massa_solidos = 117.47
        massa_retida_peneira_16 = 0
        massa_retida_peneira_30 = 0.4
        massa_retida_peneira_40 = 2.54
        massa_retida_peneira_50 = 9.70
        massa_retida_peneira_70 = 21.19
        massa_retida_peneira_100 = 37.94
        massa_retida_peneira_200 = 15.59
        massa_retida_prato = 0.57

        calcular_peneiramento_fino(
            massa_solidos, 
            massa_retida_peneira_16, 
            massa_retida_peneira_30, 
            massa_retida_peneira_40, 
            massa_retida_peneira_50, 
            massa_retida_peneira_70, 
            massa_retida_peneira_100, 
            massa_retida_peneira_200, 
            massa_retida_prato
        )


# %%
if __name__ == '__main__':
    main()
