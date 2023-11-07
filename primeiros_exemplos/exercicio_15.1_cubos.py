import matplotlib.pyplot as plt

x_values = range(1, 5001)
cubos = [1, 8, 27, 48, 125] # primeiros 05 cubos
y_values = [x**3 for x in x_values]

# Plotando um simples gráfico de dispersão:
fig, ax = plt.subplots()
ax.scatter(
        x_values, 
        y_values,
        c=y_values, cmap=plt.cm.Reds,
        linewidth=0.75
    
        )


# define o titulo do gráfico e os títulso  dos eixos X, Y
ax.set_title("Sequência dos Cinco Primeiros Cubos", fontsize=14)
ax.set_xlabel("Valores", fontsize=9) 
ax.set_ylabel("Cubos dos Valores", fontsize=9)

#Define o tamanho dos rotulos de marcação de escala
ax.tick_params(labelsize=7)

# Define o estilo do gráfico
plt.style.use('bmh')

# solicitando que a matplotlib exiba os rotulos em formato normal de numero (n ao científico)
ax.ticklabel_format(style='plain')

plt.show()