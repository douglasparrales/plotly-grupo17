import pandas as pd
import plotly.graph_objects as go

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Selecciona un jugador, por ejemplo "Erling Haaland"
player_name = 'Erling Haaland'
player_stats = df[df['Player Name'] == player_name].iloc[0]

# Datos para el gráfico de cascada
metrics = ['Goals', 'Assists', 'Big Chances Missed', 'Shots On Target']
values = [
    player_stats['Goals'],
    player_stats['Assists'],
    -player_stats['Big Chances Missed'],  # restamos oportunidades perdidas
    player_stats['Shots On Target']
]

# Etiquetas 
labels = ['Goals', 'Assists', 'Big Chances Missed', 'Shots On Target']

# Construir gráfico waterfall
fig = go.Figure(go.Waterfall(
    name = player_name,
    orientation = "v",
    measure = ["relative", "relative", "relative", "relative"],
    x = labels,
    textposition = "outside",
    text = [str(v) for v in values],
    y = values,
    connector = {"line":{"color":"rgb(63, 63, 63)"}}
))

fig.update_layout(
    title=f'Contribuciones ofensivas de {player_name} - Premier League 24/25',
    waterfallgap = 0.3,
    yaxis_title='Cantidad',
    showlegend=False
)

fig.show()
