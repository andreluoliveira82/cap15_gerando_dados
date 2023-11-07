from random import choice

# modelando um passeio aleatório.
# simula o caminho de uma formiga na terra,
# ou o movimento de uma gota de água na natureza
class RandomWalk:
    """
    Classe para gerar passeios aleatórios
    
    """
    def __init__(self, num_points=5000):
        """Inicializa os atribuitos de um passeio"""
        self.num_points = num_points

        #Todos os passeios começam em 0
        self.x_values = [0]
        self.y_values = [0]

    #--------------------------------------------------------
    def fill_walk(self):
        """Escolhendo a direção, calcula todos os passos do passeio"""
        # continua dando passos até que o passeio atinga o comprimento desejado
        while len(self.x_values) < self.num_points:
            #decide qual direção tomar e até onde ir
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # rejeita movimentos que nao vai a lugar algum:
            if x_step == 0 and y_step == 0 :
                continue

            # calcula a nova posição
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # armazena as posições nas listas:
            self.x_values.append(x)
            self.y_values.append(y)

