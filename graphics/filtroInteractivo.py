import pandas as pd
import plotly.graph_objects as go

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Preparar datos
clubs = df['Club'].unique()
clubs = sorted(clubs)

# Rango de goles para el slider
min_goals = int(df['Goals'].min())
max_goals = int(df['Goals'].max())

# Función para filtrar datos
def filter_data(selected_club, goal_range):
    filtered = df[(df['Club'] == selected_club) & 
                  (df['Goals'] >= goal_range[0]) & 
                  (df['Goals'] <= goal_range[1])]
    return filtered

# Inicial filtro
initial_club = clubs[0]
initial_goals = [min_goals, max_goals]

filtered_df = filter_data(initial_club, initial_goals)

# Crear gráfico inicial (barras de goles por jugador)
fig = go.Figure()

fig.add_trace(go.Bar(
    x=filtered_df['Player Name'],
    y=filtered_df['Goals'],
    name='Goles',
    marker_color='indianred'
))

fig.update_layout(
    title=f'Goles por jugador en {initial_club}',
    xaxis_title='Jugador',
    yaxis_title='Goles',
    xaxis_tickangle=-45,
    margin=dict(t=50, b=150),
    height=500
)

# Dropdown para seleccionar club
dropdown_buttons = []
for club in clubs:
    dropdown_buttons.append(dict(
        method='update',
        label=club,
        args=[{'x': [df[df['Club'] == club]['Player Name']],
               'y': [df[df['Club'] == club]['Goals']]},
              {'title': f'Goles por jugador en {club}',
               'xaxis': {'categoryorder': 'total descending'}}]
    ))

# Slider para rango de goles (simple versión con pasos enteros)
steps = []
for goal in range(min_goals, max_goals + 1):
    steps.append(dict(
        method='restyle',
        label=str(goal),
        args=[{'y': [df[(df['Club'] == initial_club) & (df['Goals'] >= goal)]['Goals']],
               'x': [df[(df['Club'] == initial_club) & (df['Goals'] >= goal)]['Player Name']]}]
    ))

fig.update_layout(
    updatemenus=[dict(
        active=0,
        buttons=dropdown_buttons,
        x=0,
        y=1.15,
        xanchor='left',
        yanchor='top'
    )],
    sliders=[dict(
        active=0,
        currentvalue={'prefix': 'Goles mínimo: '},
        pad={'b': 10},
        steps=steps
    )]
)

fig.show()
