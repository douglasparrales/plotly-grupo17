import pandas as pd
import plotly.express as px
import numpy as np

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Filtrar para tener solo jugadores con al menos 1 gol para mejor visualización
df_goals = df[df['Goals'] > 0].copy()

# Agregar jitter manualmente en el eje X (categorías)
# Primero convertir las posiciones a números para poder agregar jitter
pos_dict = {pos: i for i, pos in enumerate(df_goals['Position'].unique())}
df_goals['pos_num'] = df_goals['Position'].map(pos_dict)

# Agregar jitter (ruido aleatorio pequeño) en el eje X
np.random.seed(42)  # para reproducibilidad
df_goals['pos_jitter'] = df_goals['pos_num'] + np.random.uniform(-0.3, 0.3, size=len(df_goals))

# Gráfico con scatter y jitter
fig = px.scatter(
    df_goals,
    x='pos_jitter',
    y='Goals',
    color='Position',
    hover_data=['Player Name', 'Club', 'Goals', 'Assists'],
    title='Distribución de Goles por Posición'
)

# Ajustar etiquetas del eje X para que muestren las posiciones originales
fig.update_layout(
    xaxis=dict(
        tickmode='array',
        tickvals=list(pos_dict.values()),
        ticktext=list(pos_dict.keys()),
        title='Posición'
    ),
    yaxis_title='Goles',
    showlegend=False,
    margin=dict(t=50, l=25, r=25, b=25)
)

fig.show()
