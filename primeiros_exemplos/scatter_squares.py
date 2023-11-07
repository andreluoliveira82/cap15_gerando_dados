import matplotlib.pyplot as plt 
from random import randint as r
#----------------------------------------------------------------
def set_styles():
    """Define o estilo do gáfico"""

    estilos = [
        'Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10'
    ]

    estilo_escolhido = estilos[r(0, len(estilos)-1)]
    #print(f"Estilo utilizado: {estilo_escolhido}")
    return estilo_escolhido

#----------------------------------------------------------------

# calculando automaticamente os dados:
x_values = range(1 ,1001) # 1000 registros
y_values = [x**2 for x in x_values] # lista do quadrado de cada valor na lista x_values


# estilizando o gráfico
estilo = set_styles()
plt.style.use(estilo)

# plotando um simples gráfico de linha
fig, ax = plt.subplots()
ax.scatter(
        x_values, 
        y_values,
        #color="red", # passando o argum. color para a cor desejada
        #color=(0, 0.8, 0),# cor verde usando valores entre 0 e 1
        c=y_values, cmap=plt.cm.Blues, #usando o colormap
        s=1
    ) 

# define o titulo do gráfico e os títulso  dos eixos X, Y
ax.set_title(f"Sequência de Números Quadrados\n({estilo})", fontsize=14)
ax.set_xlabel("Valores", fontsize=9) 
ax.set_ylabel("Quadrados dos valores", fontsize=9)

#Define o tamanho dos rotulos de marcação de escala
ax.tick_params(labelsize=7)

# Define o intervalo para cada eixo:
ax.axis([0, 1100, 0, 1_100_000])

# solicitando ao matplotlib que deixe os rótulos em notação simples
ax.ticklabel_format(style="plain")

#salvando o gráfico como uma imagem
plt.savefig("squares_plot_" + estilo + ".png", bbox_inches="tight")

plt.show() # exibindo o grafico na tela
