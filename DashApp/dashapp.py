from dash import Dash
import dash_html_components as html
import dash_core_components as dcc
from random import randint

external_stylesheets = ['https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css']


app = Dash(__name__, external_stylesheets=external_stylesheets)

N=20

database = {
    'index': list(range(N)),
    'maiores': [randint(1,1000) for _ in range(N)]
}

app.layout = html.Div(
    className="dashapp-style",
    children = [
        html.H1('Ola, mundo'),
       html.P("Bem vindo ao Dash"),
       html.H3("Grafico de Pizza"),
       dcc.Graph(
           config= {'displayModeBar':False},
           figure= {
               'data':[
                   {'y': database['maiores'],
                   'x': database['index'],
                   'name': 'a'},
               ],   
                'layout':{
                    'title': "Minha Pizza",
                    'paper_bgcolor':'#222225',
                    'titlefont':{
                        'size': 30,
                        'color': '#fff',
                    },
                    
                },
               
           }
       )
        ]
)

app.run_server(debug=True)