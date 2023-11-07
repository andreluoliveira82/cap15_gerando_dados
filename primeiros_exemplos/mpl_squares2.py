import matplotlib.pyplot as plt 
from random import randint as r

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # lista de quadrados

estilos = [
    'Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10'
    ]

estilo_escolhido = estilos[r(0, len(estilos))]
print(f"Estilo utilizado: {estilo_escolhido}")

# estilizando o gráfico
plt.style.use(estilo_escolhido)

# plotando um simples gráfico de linha
fig, ax = plt.subplots()
ax.plot(input_values,squares, linewidth=0.5)

# define o titulo do gráfico e os títulso  dos eixos X, Y
ax.set_title("Sequência de Números Quadrados", fontsize=14)
ax.set_xlabel("Valores", fontsize=9) 
ax.set_ylabel("Quadrados dos valores", fontsize=9)

#Define o tamanho dos rotulos de marcação de escala
ax.tick_params(labelsize=7)

plt.show()