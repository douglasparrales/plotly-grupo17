import pandas as pd
import plotly.express as px

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Crear tabla de frecuencias: Club vs Nacionalidad
heatmap_data = df.groupby(['Club', 'Nationality']).size().reset_index(name='Count')

# Crear gráfico de mapa de calor
fig = px.density_heatmap(
    heatmap_data,
    x='Nationality',
    y='Club',
    z='Count',
    color_continuous_scale='Viridis',
    title='Mapa de calor: Jugadores por Club y Nacionalidad',
    labels={'Count': 'Cantidad de Jugadores'}
)

fig.update_layout(
    xaxis={'categoryorder': 'total descending'},
    yaxis={'categoryorder': 'total descending'},
    margin=dict(t=50, l=50, r=50, b=50)
)

fig.show()
