from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from random import randint
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = Dash(__name__)


N = 20

database = {
    'index':[],
    'maiores': [],
    'menores': [],
    'bebes': [],
}


app.layout = html.Div(
    children=[
        html.H1('Evento X'),
        html.H3('idade das pessoas que foram ao evento'),
        dcc.Interval(id='interval'),
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

def update_database(value):
    database['index'].append(value)
    database['bebes'].append(randint(1,200))
    database['maiores'].append(randint(1,200))
    database['menores'].append(randint(1,200))



@app.callback(
    Output('meu_grafico', 'figure'),
    [ 
    Input('meu_checklist', 'value'),
    Input('meu_dropdown', 'value'),
    Input('interval', 'n_intervals')
    ]
)
def my_callback(input_data, graph_type, n_intervals):
    update_database(n_intervals)
    grafico = {
        'data': []
    }
    for x in input_data:
        grafico['data'].append(    
                    {
                        'y': database[x][-20:],
                        'x': database['index'][-20:],
                        'name': x,
                        'type': graph_type
                    },            
        )
    return grafico
    
app.run_server(debug=True)