import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # lista de quadrados

# plotando um simples gráfico de linha
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=0.5)

# define o titulo do gráfico e os títulso  dos eixos X, Y
ax.set_title("Sequência de Números Quadrados", fontsize=14)
ax.set_xlabel("Valores", fontsize=9) 
ax.set_ylabel("Quadrados dos valores", fontsize=9)

#Define o tamanho dos rotulos de marcação de escala
ax.tick_params(labelsize=7)

plt.show()