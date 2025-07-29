import pandas as pd
import plotly.express as px

# Cargar el dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Ordenar por goles y seleccionar los 20 mejores
pareto_df = df.sort_values(by="Goals", ascending=False).head(20).copy()

# Calcular el porcentaje acumulado
pareto_df["Cumulative Goals"] = pareto_df["Goals"].cumsum()
pareto_df["Cumulative %"] = 100 * pareto_df["Cumulative Goals"] / pareto_df["Goals"].sum()

# Crear gráfico de barras
fig = px.bar(
    pareto_df,
    x="Player Name",
    y="Goals",
    title="Gráfico de Pareto: Goles por Jugador (Top 20)",
    labels={"Goals": "Goles", "Player Name": "Jugador"},
    template="plotly_dark"
)

# Añadir línea de porcentaje acumulado
fig.add_scatter(
    x=pareto_df["Player Name"],
    y=pareto_df["Cumulative %"],
    mode="lines+markers",
    name="Porcentaje Acumulado",
    yaxis="y2"
)

# Configurar doble eje Y
fig.update_layout(
    yaxis=dict(title="Goles"),
    yaxis2=dict(
        title="Porcentaje Acumulado",
        overlaying="y",
        side="right",
        range=[0, 110]
    ),
    hovermode="x unified"
)

fig.show()
