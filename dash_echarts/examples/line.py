import dash_echarts
import dash, random
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate


def gen_randlist(num):
    return random.sample(range(num), 7)


app = dash.Dash(__name__)

option =  {
    'xAxis': {
        'type': 'category',
        # 'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    'yAxis': {
        'gridIndex': 0
    },
'dataset': {
      'source': [
        ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
        ['Milk Tea', 56.5, 82.1, 88.7, 70.1, 53.4, 85.1],
        ['Matcha Latte', 51.1, 51.4, 55.1, 53.3, 73.8, 68.7],
        ['Cheese Cocoa', 40.1, 62.2, 69.5, 36.4, 45.2, 32.5],
        ['Walnut Brownie', 25.2, 37.1, 41.2, 18, 33.9, 49.1]
      ]
    },
    'series': [
      {
        'type': 'line',
        'smooth': True,
        'seriesLayoutBy': 'row',
        'emphasis': { 'focus': 'series' }
      },
    ],
    'tooltip': {
      'trigger': 'axis',
      'showContent': False
    },
    # 'series': [{
    #     'data': gen_randlist(200),
    #     'type': 'line',
    # }]
}

app.layout = html.Div([
    dash_echarts.DashECharts(
        option = option,
        id='echarts',
        style={"width": '100vw',"height": '100vh'}
    ),
    dcc.Interval(id="interval", interval=1 * 1000, n_intervals=0),
])


@app.callback(
    Output('echarts', 'option'),
    [Input('echarts', 'axis_pointer_data')],
    [State('echarts', 'option')],
)
def update(axis, opt):
    print(axis, '<<<<<')
    return opt
    # if n_intervals == 0:
    #     raise PreventUpdate
    # else:
    #     opt['series'][0]['data'] = gen_randlist(200)
    #     return opt



app.run_server(debug=True)
