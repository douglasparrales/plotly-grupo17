import pandas as pd
import plotly.graph_objects as go

# Cargar dataset
df = pd.read_csv('..\epl_player_stats_24_25.csv')

# Para hacer Sankey no queremos demasiados nodos para que sea legible,
# así que filtramos solo los top clubes y top jugadores por minutos.

# Top 5 clubes por suma de minutos
top_clubs = df.groupby('Club')['Minutes'].sum().sort_values(ascending=False).head(5).index.tolist()

df_top = df[df['Club'].isin(top_clubs)].copy()

# Top 3 posiciones por club (sumando minutos)
posiciones_top = df_top.groupby(['Club', 'Position'])['Minutes'].sum().reset_index()
posiciones_top = posiciones_top.groupby('Club').apply(lambda x: x.nlargest(3, 'Minutes')).reset_index(drop=True)

# Filtramos posiciones para incluir solo las top 3 por club
df_top = df_top.merge(posiciones_top[['Club', 'Position']], on=['Club', 'Position'], how='inner')

# Tomamos los top 4 jugadores por minutos en cada club y posición para no saturar
df_top['Rank'] = df_top.groupby(['Club', 'Position'])['Minutes'].rank(method='first', ascending=False)
df_top = df_top[df_top['Rank'] <= 4]

# Construcción de los nodos y enlaces Sankey
clubs = list(df_top['Club'].unique())
positions = list(df_top['Position'].unique())
players = list(df_top['Player Name'].unique())

# Crear lista completa de etiquetas y mapa para indices
labels = clubs + positions + players
label_indices = {label: i for i, label in enumerate(labels)}

# Función para crear enlaces (source, target, value)
def make_links(df, source_col, target_col, value_col):
    links = []
    grouped = df.groupby([source_col, target_col])[value_col].sum().reset_index()
    for _, row in grouped.iterrows():
        links.append({
            'source': label_indices[row[source_col]],
            'target': label_indices[row[target_col]],
            'value': row[value_col]
        })
    return links

# Enlaces Club → Posición
links_club_pos = make_links(df_top, 'Club', 'Position', 'Minutes')
# Enlaces Posición → Jugador
links_pos_player = make_links(df_top, 'Position', 'Player Name', 'Minutes')

# Unir todos los enlaces
all_links = links_club_pos + links_pos_player

# Crear Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=["#636EFA"]*len(clubs) + ["#EF553B"]*len(positions) + ["#00CC96"]*len(players)
    ),
    link=dict(
        source=[link['source'] for link in all_links],
        target=[link['target'] for link in all_links],
        value=[link['value'] for link in all_links],
        color="rgba(150,150,150,0.4)"
    )
)])

fig.update_layout(
    title_text="Distribución de minutos jugados: Club → Posición → Jugador",
    font_size=12
)

fig.show()
