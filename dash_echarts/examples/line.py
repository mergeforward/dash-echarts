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
        'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    'yAxis': {
        'type': 'value'
    },
    'series': [{
        'data': gen_randlist(200),
        'type': 'line',
    }]
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
    [Input('interval', 'n_intervals')],
    [State('echarts', 'option')],
)
def update(n_intervals, opt):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        opt['series'][0]['data'] = gen_randlist(200)
        return opt

app.run_server(debug=True)
