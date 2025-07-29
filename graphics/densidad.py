import pandas as pd
import plotly.figure_factory as ff

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Filtrar solo los jugadores que hayan marcado al menos 1 gol (para evitar acumulación en cero)
goals_data = df[df['Goals'] > 0]['Goals']

# Crear el gráfico de densidad
fig = ff.create_distplot(
    [goals_data],
    group_labels=["Goles"],
    show_hist=False,       # Solo curva KDE, sin histograma
    curve_type='kde',      # Tipo KDE (Kernel Density Estimate)
    colors=['skyblue']
)

fig.update_layout(
    title="Distribución de Goles (KDE)",
    xaxis_title="Cantidad de Goles",
    yaxis_title="Densidad",
    template="plotly_dark"
)

fig.show()