from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# df = pd.DataFrame({
#     "Points": ["Praça", "Lachonete", "Restaurante", "Praça", "Lachonete", "Restaurante"],
#     "Frequencia": [500, 3000, 1500, 200, 900, 450],
#     "Cidade": ["Currais Novos", "Currais Novos", "Currais Novos", "São Vicente", "São Vicente", "São Vicente", ]
# })

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
fig = px.bar(df, x="Points", y="Frequencia", color="Cidade", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Frequencia nos Points'),
    dcc.Graph(
        id="CN x SV", figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)