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
            id = 'meu_dropdown',
            options=[
                {'label': 'Linha', 'value': 'line'},
                {'label': 'Barra', 'value': 'bar'},
            ],
            value='line'
        ),
        dcc.Slider(
            min=0,
            max=10,
            step=1,
            value=5
        ),
        dcc.Checklist(
            id= 'meu_checklist',
            options=[
                {'label': 'Menores de Idade', 'value': 'menores'},
                {'label': 'Bebes', 'value': 'bebes'},
                {'label': 'Maiores de idade', 'value': 'maiores'}
            ],
            value=['bebes']
        ),
        dcc.Graph(
            id = 'meu_grafico',
            config={'displayModeBar': False},

        )
    ]
)

@app.callback(
    Output('meu_grafico', 'figure'),
    [ 
    Input('meu_checklist', 'value'),
    Input('meu_dropdown', 'value')
    ]
)
def my_callback(input_data, graph_type):
    grafico = {
        'data': []
    }
    for x in input_data:
        grafico['data'].append(    
                    {
                        'y': database[x],
                        'x': database['index'],
                        'name': x,
                        'type': graph_type
                    },            
        )
    return grafico
    
app.run_server(debug=True)