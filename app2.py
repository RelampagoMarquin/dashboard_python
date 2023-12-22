from dash import Dash, html, dcc, dash_table, callback, Output, Input
import plotly.express as px
import pandas as pd
##buscando dados de fora
app = Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app.layout = html.Div([
    html.Div(
        className="my-header",
        children=[
            html.H1(children="Análise sobre países"),
            dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controle-radio'),
            dcc.Graph(
                id="controle-grafico",
                figure={}
            )
        ]
    ),
    html.Hr(),
    dash_table.DataTable(data=df.to_dict("records"), page_size=10),
    html.Hr(),
    html.Div(
        className="grafico-pizza",
        children=[
            html.H2(className='pizza-titulo', children="gráfico de pizza"),
            dcc.Dropdown(id='controle-radio-pizza',
                    options=['pop', 'gdpPercap'],
                    value='gdpPercap', clearable=True,
                ),
            dcc.Graph(
                id="controle-grafico-pizza",
                figure={}
            )
        ]
    ),


])

@callback(
    Output(component_id='controle-grafico', component_property='figure'),
    Input(component_id='controle-radio', component_property='value')
)
def atualizar_grafico(col):
    fig = px.histogram(df, x='continent', y=col, histfunc='avg')
    return fig
# grafico de pizza
@callback(
    Output(component_id='controle-grafico-pizza', component_property='figure'),
    Input(component_id='controle-radio-pizza', component_property='value')
)
def atualizar_grafico_pizza(col):
    contry_continentes = px.data.gapminder().query("continent == 'Americas'")
    fig = px.pie(contry_continentes, values=col, names='country')
    fig.update_traces(textposition='inside')
    fig.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')
    return fig

if __name__ == '__main__':
    app.run(debug=True)