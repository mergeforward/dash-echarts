import random

import dash_echarts
import dash_html_components as html
import dash_core_components as dcc

def gen_randlist(num):
    return random.sample(range(num), 7)

option = {
    'xAxis': {
        'type': 'category',
        'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    'yAxis': {
        'type': 'value'
    },
    'series': [{
        'data': gen_randlist(100),
        'type': 'bar',
        'smooth': True
    }, {
        'data': gen_randlist(200),
        'type': 'bar',
        'smooth': True
    }]
}

layout = html.Div([
    dash_echarts.DashECharts(
        option = option,
        id='echarts-bar-basic',
        style={
            "width": '100%',
            "height": '100vh',
        }
    ),
    dcc.Markdown('''
    
    ```python
    import dash_echarts
    import dash, random
    from dash.dependencies import Input, Output
    import dash_html_components as html
    import dash_core_components as dcc
    from dash.exceptions import PreventUpdate


    def gen_randlist(num):
        return random.sample(range(num), 7)

    def main():
        app = dash.Dash(__name__)

        option =  {
            'xAxis': {
                'type': 'category',
                'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            'yAxis': {
                'type': 'value'
            },
            'series': [{
                'data': gen_randlist(100),
                'type': 'bar',
                'smooth': True
            }, {
                'data': gen_randlist(200),
                'type': 'bar',
                'smooth': True
            }]
        } 

        app.layout = html.Div([
            dash_echarts.DashECharts(
                option = option,
                id='echarts',
                style={
                    "width": '100vw',
                    "height": '100vh',
                }
            ),
            dcc.Interval(id="interval", interval=1 * 1000, n_intervals=0),
        ])


        @app.callback(
            Output('echarts', 'option'),
            [Input('interval', 'n_intervals')])
        def update(n_intervals):
            if n_intervals == 0:
                raise PreventUpdate
            else:
                option['series'][0]['data'] = gen_randlist(200)
                option['series'][1]['data'] = gen_randlist(200)
            return option
        app.run_server(debug=True)

    if __name__ == '__main__':
        main()
    ```
    ''',
                 style={
                     # "display": 'block',
                     "width": '80%',
                     "marginLeft": '10%',
                     "marginRight": '10%',
                     "height": '100vh',
                 }
                 ),
])