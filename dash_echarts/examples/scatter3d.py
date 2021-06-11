import dash_echarts
import dash, random
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from os import path
import json


def main():
    '''
    dash_echarts examples
    name: scatter 3d
    author: dameng <pingf0@gmail.com>
    '''
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath+'/static', 'life-expectancy-table.json'))
    with open(filepath) as json_file:
        data = json.load(json_file)

    option =  {
        'grid3D': {},
        'xAxis3D': {
            'type': 'category',
            'axisLabel': {
                'interval': 0,
                'rotate': 45 
            },
        },
        'yAxis3D': {
            'min': 1750,
            'max': 2050
        },
        'zAxis3D': {
            'min': 0,
            'max': 100
        },
        'dataset': {
            'dimensions': [
                {'name': 'Income', 'type': 'int'},
                {'name': 'Life', 'type': 'int'},
                {'name': 'Population', 'type': 'int'},
                {'name': 'Country','type': 'ordinal'},
                {'name': 'Year', 'type': 'int'}
            ],
            'source': data
        },
        'series': [
            {
                'type': 'scatter3D',
                'symbolSize': 6,
                'encode': {
                    'x': 'Country',
                    'y': 'Year',
                    'z': 'Income',
                    'tooltip': [0,1,2,3,4]
                }
            },
        ]
    }
    dropdowns = [ 'Income', 'Life', 'Population', 'Country', 'Year' ]
    controls = dbc.Card(
        [
            dbc.FormGroup(
                [
                    dbc.Label("X"),
                    dcc.Dropdown(
                        id="x",
                        options=[
                            {"label": col, "value": col} for col in dropdowns
                        ],
                        value="Country",
                    ),
                ],
            ),
            dbc.FormGroup(
                [
                    dbc.Label("Y"),
                    dcc.Dropdown(
                        id="y",
                        options=[
                            {"label": col, "value": col} for col in dropdowns
                        ],
                        value="Year",
                    ),
                ],
            ),
            dbc.FormGroup(

                [
                    dbc.Label("Z"),
                    dcc.Dropdown(
                        id="z",
                        options=[
                            {"label": col, "value": col} for col in dropdowns
                        ],
                        value="Life",
                    ),
                ]
            ),
        ],
        body=True,
        style={
            'position': 'absolute', 
            'height': 300, 'width': 300, 
            'top': '20vh', 'left': '10vw'
        }
    )

    app.layout = dbc.Container(
        [
            dbc.Row(
                [
                    dash_echarts.DashECharts(
                        option = option,
                        id='echarts',
                        style={
                            'position': 'absolute',
                            "width": '100vw',
                            "height": '80vh',
                            "left": '10vw'
                        }
                    ),
                ]
            ),
            controls,
        ],
        fluid=True,
    )
    
    def setup_axis(option, an, v):
        if v == 'Country':
            option[an] = {
                'type': 'category',
                'axisLabel': {
                    'interval': 0,
                    'rotate': 45 
                },
            }
        elif v == 'Year':
            option[an] = {
                'type': 'value',
                'min': 1750,
                'max': 2050
            }
        elif v == 'Income':
            option[an] = {
                'type': 'value',
                'min': 0,
                'max': 80000
            }
        elif v == 'Population':
            option[an] = {
                'type': 'value',
                'min': 0,
                'max': 2000000000
            }
        elif v == 'Life':
            option[an] = {
                'type': 'value',
                'min': 0,
                'max': 100
            }

    @app.callback(
        Output('echarts', 'option'),
        [Input('x', 'value'),Input('y', 'value'),Input('z', 'value')])
    def update(x, y, z):
        option['series'][0]['encode']['x'] = x
        option['series'][0]['encode']['y'] = y
        option['series'][0]['encode']['z'] = z
        
        setup_axis(option, 'xAxis3D', x)
        setup_axis(option, 'yAxis3D', y)
        setup_axis(option, 'zAxis3D', z)
        
        return option


    app.run_server(debug=True)

if __name__ == '__main__':
    main()