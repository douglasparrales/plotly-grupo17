import pandas as pd
import plotly.graph_objects as go

# Cargar el dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Seleccionar los 10 jugadores con más minutos jugados
top_players = df.sort_values(by="Minutes", ascending=False).head(10)

# Crear gráfico de cinta (ribbon)
fig = go.Figure()

# Línea de Goles
fig.add_trace(go.Scatter(
    x=top_players["Player Name"],
    y=top_players["Goals"],
    mode="lines+markers",
    name="Goals",
    line=dict(color="blue")
))

# Línea de Asistencias y relleno entre ambas
fig.add_trace(go.Scatter(
    x=top_players["Player Name"],
    y=top_players["Assists"],
    mode="lines+markers",
    name="Assists",
    line=dict(color="green"),
    fill='tonexty',  # Relleno entre esta línea y la anterior
    fillcolor="rgba(0,200,0,0.3)"
))

# Personalización del diseño
fig.update_layout(
    title="Goles vs Asistencias - Top 10 jugadores por minutos jugados",
    xaxis_title="Jugador",
    yaxis_title="Cantidad",
    template="plotly_dark",
    hovermode="x unified"
)

fig.show()