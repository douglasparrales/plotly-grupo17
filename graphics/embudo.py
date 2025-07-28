import pandas as pd
import plotly.graph_objects as go

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Selecciona un jugador para el embudo
player_name = 'Erling Haaland'
player = df[df['Player Name'] == player_name].iloc[0]

# Datos para el embudo
stages = ['Touches', 'Passes', 'Shots', 'Shots On Target', 'Goals']
values = [
    player['Touches'],
    player['Passes'],
    player['Shots'],
    player['Shots On Target'],
    player['Goals']
]

fig = go.Figure(go.Funnel(
    y = stages,
    x = values,
    textinfo = "value+percent initial",
    marker={"color": ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]}
))

fig.update_layout(
    title=f'Proceso ofensivo de {player_name} - Premier League 24/25',
    margin=dict(t=50, l=25, r=25, b=25)
)

fig.show()
