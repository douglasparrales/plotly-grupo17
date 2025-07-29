import pandas as pd
import plotly.graph_objects as go

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Limpiar la columna 'Passes%' eliminando '%' y convirtiendo a float
df['Passes%'] = df['Passes%'].str.replace('%', '', regex=False).astype(float)

# Seleccionar jugador
player_name = 'Erling Haaland'
player = df[df['Player Name'] == player_name].iloc[0]

# Variables a comparar
metrics = {
    'Goals': player['Goals'],
    'Assists': player['Assists'],
    'Shots On Target': player['Shots On Target'],
    'Passes%': player['Passes%'],
    'Carries': player['Carries'],
    'Progressive Carries': player['Progressive Carries'],
    'Tackles': player['Tackles'],
    'Duels Won': player['gDuels Won'] + player['aDuels Won']
}

# Promedios generales
league_avg = {
    'Goals': df['Goals'].mean(),
    'Assists': df['Assists'].mean(),
    'Shots On Target': df['Shots On Target'].mean(),
    'Passes%': df['Passes%'].mean(),
    'Carries': df['Carries'].mean(),
    'Progressive Carries': df['Progressive Carries'].mean(),
    'Tackles': df['Tackles'].mean(),
    'Duels Won': (df['gDuels Won'] + df['aDuels Won']).mean()
}

categories = list(metrics.keys())

fig = go.Figure()

# Datos del jugador
fig.add_trace(go.Scatterpolar(
    r=list(metrics.values()),
    theta=categories,
    fill='toself',
    name=player_name,
    line=dict(color='blue')
))

# Datos promedio de la liga
fig.add_trace(go.Scatterpolar(
    r=list(league_avg.values()),
    theta=categories,
    fill='toself',
    name='Promedio Liga',
    line=dict(color='gray', dash='dot')
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            linewidth=1,
            showline=True,
            showticklabels=False,
            ticks=''
        )
    ),
    title=f'Perfil estadístico de {player_name} vs Promedio Liga',
    showlegend=True
)

fig.show()
