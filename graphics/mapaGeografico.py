import pandas as pd
import plotly.express as px

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Contar jugadores por nacionalidad
nationality_counts = df['Nationality'].value_counts().reset_index()
nationality_counts.columns = ['Country', 'Players']

# Para mapear, necesitamos nombres estándar, a veces el dataset usa abreviaturas o variaciones.
# Plotly espera nombres de países estándar en inglés.
# Vamos a usar directamente los nombres del dataset, pero si no se reconocen, habría que hacer un mapeo manual.

fig = px.scatter_geo(
    nationality_counts,
    locations="Country",
    locationmode='country names',  # espera nombres estándar
    color="Players",
    size="Players",
    hover_name="Country",
    projection="natural earth",
    title="Cantidad de jugadores por nacionalidad en Premier League 24/25",
    color_continuous_scale=px.colors.sequential.Plasma
)

fig.update_layout(
    margin=dict(t=50, b=0, l=0, r=0)
)

fig.show()
