
# codigo para plotar todos os passos do passeio aleat´rio gerados com a classe random_walk()
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
from random_walk import RandomWalk

#-------------------------------------------------------------------
def create_directory():
    """Retorna o diretório """
    n = datetime.now().strftime("%y%m%d%H%M%S")

    diretorio = Path("C:/Users\gestao.dados/OneDrive - ALBAN INDUSTRIA E COMERCIO DE EMBALAGENS PLASTICAS LTDA/Imagens/matplotlib_graficos/")

    return diretorio/f"mapa-random-walk-{n}"
#-------------------------------------------------------------------


# continua criando passeios novos, desde que o programa esteja ativo
while True:
    
    # intancia um random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # plota os pontos de rw em um grafico
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15,9),dpi=128)

    
    point_numbers = range(rw.num_points)

    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers, cmap=plt.cm.Blues, # colorindo os pontos
        edgecolors='none', # descartando o contorno preto em torno de cada ponto
        s=1)
    
    ax.set_aspect("equal") 
    
    # destaca o primeiro e o último ponto
    # ponto inicial
    ax.scatter(0, 0, c="green", edgecolors='none', s=100) 
     # último ponto
    ax.scatter(rw.x_values[-1], rw.y_values[-1],c='red',edgecolors='none',s=100)

    # removendo os eixos para evitar 
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # ocultando os valores dos eixos x e y 
    # plt.xticks([])
    # plt.yticks([])

    # salvando o grafico
    local_arquivo = create_directory()
    # print(local_arquivo)
    plt.savefig(str(local_arquivo) + ".png", bbox_inches="tight")

    #exibe o grafico
    plt.show()

    keep_runnung = input("Gostaria de fazer outo caminho? (y/n): ")
    if keep_runnung.lower() == "n":
        break
