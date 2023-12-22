from dash import Dash, html, dcc, dash_table, callback, Output, Input
import datetime
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from collections import deque

##constante update
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(children=[
                    dcc.Graph(id='live-update-graph'),
                    dcc.Interval(
                        'live-component-line',
                        interval=200,
                        n_intervals=1
                    )
                ]),
                html.Div(children=[
                    dcc.Graph(id='live-update-histogram'),
                    dcc.Interval(
                        'live-component-histogram',
                        interval=200,
                        n_intervals=1
                    )
                ]),
            ]
        ),
        html.Div(
            children=[
                html.Div(children=[
                    dcc.Graph(id='live-update-graph-normal'),
                    dcc.Interval(
                        'live-component-line-normal',
                        interval=200,
                        n_intervals=1
                    )
                ]),
                html.Div(children=[
                    dcc.Graph(id='live-update-histogram-normal'),
                    dcc.Interval(
                        'live-component-histogram-normal',
                        interval=200,
                        n_intervals=1
                    )
                ]),
            ]
        ),


    ]
)

X = deque(maxlen=20)
Y = deque(maxlen=20)
hist = []
def generate_random_data():
        X.append(datetime.datetime.now())
        y = np.random.uniform(0,1)
        hist.append(y)
        Y.append(y)
        return go.Scatter(y=list(Y), x=list(X), mode='lines+markers', name='Valores Uniformes Aleatorios')

# uniform
@callback(
    Output('live-update-graph', 'figure'),
    Input('live-component-line', 'n_intervals'),

)
def update_graph(n):
    fig = generate_random_data()
    layout = go.Layout(title='Valores Uniformes Aleatorios', xaxis=dict(title='Tempo'),
                       yaxis=dict(title='Valor', range=[0, 1]))
    return {'data': [fig], 'layout': layout}

@callback(
    Output('live-update-histogram', 'figure'),
    Input('live-component-histogram', 'n_intervals'),

)
def update_hist(n):
    fig = px.histogram(x=hist, nbins=50, range_x=[0, 1], title='Histograma Uniforme Aleatorios')
    return fig


# normal
Xn = deque(maxlen=20)
Yn = deque(maxlen=20)
histn = []
def generate_random_data_histogram():
    Xn.append(datetime.datetime.now())
    y = np.random.normal(0.5, 0.1)
    histn.append(y)
    Yn.append(y)
    return go.Scatter(y=list(Yn), x=list(Xn), mode='lines+markers', name='Valores Uniformes Normais')


@callback(
    Output('live-update-graph-normal', 'figure'),
    Input('live-component-line-normal', 'n_intervals'),

)
def update_graph_normal(n):
    fig = generate_random_data_histogram()
    layout = go.Layout(title='Valores Normais Aleatorios', xaxis=dict(title='Tempo'),
                       yaxis=dict(title='Valor', range=[0, 1]))
    return {'data': [fig], 'layout': layout}

@callback(
    Output('live-update-histogram-normal', 'figure'),
    Input('live-component-histogram-normal', 'n_intervals'),

)
def update_hist_normal(n):
    fig = px.histogram(x=histn, nbins=50, range_x=[0, 1], title='Histograma Normal', color_discrete_sequence=['indianred'])
    return fig

# o normal tende a preencher preferencialmente o valor perto do loc que seria o loc, enquanto que o uniforme vai gerando
# aleadoriamente dentro do intervalo

if __name__ == '__main__':
    app.run(debug=True)