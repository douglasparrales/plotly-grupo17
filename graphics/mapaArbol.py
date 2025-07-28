import pandas as pd
import plotly.express as px

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Filtrar jugadores con al menos 1 gol para no llenar el gráfico con jugadores sin goles
df_goals = df[df['Goals'] > 0].copy()

# Crear el treemap
fig = px.treemap(
    df_goals,
    path=['Club', 'Position', 'Player Name'],  # jerarquía de grupos
    values='Goals',                            # tamaño según goles
    color='Goals',                            # color según goles (más goles = color más intenso)
    color_continuous_scale='Viridis',        # paleta de color
    hover_data={
        'Goals': True,
        'Assists': True,
        'Shots On Target': True,
        'Player Name': False,  
        'Position': False,
        'Club': False
    }
)

fig.update_layout(
    title='Distribución de goles en Premier League 24/25: Club > Posición > Jugador',
    margin=dict(t=50, l=25, r=25, b=25)
)

fig.show()
