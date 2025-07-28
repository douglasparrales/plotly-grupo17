import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Cargar el archivo CSV 
df = pd.read_csv("..\epl_player_stats_24_25.csv")

# Agrupar goles por club
goles_por_club = df.groupby("Club")["Goals"].sum().reset_index().sort_values(by="Goals", ascending=False)

# Crear gráfico de barras con Plotly Express
fig_px = px.bar(
    goles_por_club,
    x="Club",
    y="Goals",
    title="Goles por Club en la Premier League 2024/25",
    labels={"Goals": "Total de Goles", "Club": "Club"},
    color="Goals",
    color_continuous_scale="Blues"
)

# Convertir a graph_objects para añadir línea de tendencia
fig = go.Figure(fig_px)

# Agregar línea de tendencia (media móvil de 3)
fig.add_trace(go.Scatter(
    x=goles_por_club["Club"],
    y=goles_por_club["Goals"].rolling(window=3).mean(),
    name="Tendencia (Media Móvil)",
    mode="lines+markers",
    line=dict(color="crimson", width=3)
))

# Añadir explicación como anotación
fig.update_layout(
    title={
        'text': "Goles por Club + Línea de Tendencia (Premier League 2024/25)",
        'x': 0.5
    },
    xaxis_title="Club",
    yaxis_title="Total de Goles",
    coloraxis_showscale=False,
    annotations=[
        dict(
            x=0.5,
            y=-0.3,
            xref="paper",
            yref="paper",
            showarrow=False,
            font=dict(size=12),
            align="left"
        )
    ],
    height=600
)

# Mostrar gráfico
fig.show()
