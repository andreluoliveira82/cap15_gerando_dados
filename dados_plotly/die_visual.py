from die import Die
import plotly.express as px

# cria um D6 (dados de 06 lados)
die = Die()  # por padrão Die recebe um valor de 06 lados

# Realiza alguns testes e armazena os resultados em uma lista
results = []
jogadas = 1000

for rol_num in range(jogadas):  # rolando o dado por x vezes
    result = die.roll()  # chama método que rola o dado
    results.append(result)

# Analisa os resultados
frequencies = []
poss_results = range(1, die.num_sides + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# visualiza os resultados:
titulo = f"Frequência de possiblidades de Dados (em {jogadas} rodadas.)"
rotulos_eixos = {
    'x': 'Números do Dado (Possibilidades)', 'y': 'Freqência do Número'}

# Calcula os percentuais e cria os rótulos personalizados
rotulos = []
for freq in frequencies:
    percent = freq/jogadas * 100
    rotulos.append(f"{freq}\n({percent:.0f}%)")


fig = px.bar(
    x=poss_results,
    y=frequencies,
    title=titulo,
    labels=rotulos_eixos,
    text=rotulos,
    orientation='v'

)

# Personalizando ainda mais o grafico

# salvando o grafico
fig.write_html('visual1.html')

fig.show()
