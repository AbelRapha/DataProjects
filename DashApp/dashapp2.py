from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from random import randint
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output




app = Dash(__name__)


N = 20

database = {
    'index': list(range(N)),
    'maiores': [randint(1, 1000) for _ in range(N)],
    'menores': [randint(1, 1000) for _ in range(N)],
    'bebes': [randint(1, 1000) for _ in range(N)],
}


app.layout = html.Div(
    children=[
        html.H1('Evento X'),
        html.H3('idade das pessoas que foram ao evento'),
        dcc.Dropdown(
            options=[
                {'label': 'Menores de Idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'}
            ],
            value='menores'
        ),
        dcc.Slider(
            min=0,
            max=10,
            step=1,
            value=5
        ),
        dcc.Checklist(
            options=[
                {'label': 'Menores de Idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'}
            ],
            value=['bebes']
        ),
        dcc.Graph(
            config={'displayModeBar': False},
            figure={
                'data': [
                    {
                        'y': database['maiores'],
                        'x': database['index'],
                        'name': 'Maiores'
                    },
                ],
            }
        )
    ]
)


app.run_server(debug=True)