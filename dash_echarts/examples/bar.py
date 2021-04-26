import dash_echarts
import dash, random
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate


def gen_randlist(num):
    return random.sample(range(num), 7)


def main():
    '''
    dash_echarts examples
    name: bar with echarts
    author: dameng <pingf0@gmail.com>
    '''
    app = dash.Dash(__name__)

    label_option = {
        'show': True,
        'position': 'insideBottom',
        'distance': 15,
        'align': 'left',
        'verticalAlign': 'middle',
        'rotate': 90,
        'formatter': '{c}  {name|{a}}',
        'fontSize': 16,
        'rich': {
            'name': {
            }
        }
    }
    option = {
        'xAxis': [{
            'type': 'category',
            'axisTick': {'show': False},
            'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        }],
        'yAxis': [{
            'type': 'value'
        }],
        'legend': {
            'data': ['Forest', 'Steppe', 'Desert', 'Wetland']
        },
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'shadow'
            }
        },
        'toolbox': {
            'show': True,
            'orient': 'vertical',
            'left': 'right',
            'top': 'center',
            'feature': {
                'mark': {'show': True},
                'dataView': {'show': True, 'readOnly': False},
                'magicType': {'show': True, 'type': ['bar', 'stack', 'tiled']},
                'restore': {'show': True},
                'saveAsImage': {'show': True}
            }
        },
        'series': [
            {
                'name': 'Forest',
                'data': gen_randlist(200),
                'label': label_option,
                'barGap': 0,
                'emphasis': {
                    'focus': 'series'
                },
                'type': 'bar',
            },
            {
                'name': 'Steppe',
                'data': gen_randlist(200),
                'label': label_option,
                'barGap': 0,
                'emphasis': {
                    'focus': 'series'
                },
                'type': 'bar',
            },
            {
                'name': 'Wetland',
                'data': gen_randlist(200),
                'label': label_option,
                'barGap': 0,
                'emphasis': {
                    'focus': 'series'
                },
                'type': 'bar',
            },
            {
                'name': 'Forest',
                'data': gen_randlist(200),
                'label': label_option,
                'barGap': 0,
                'emphasis': {
                    'focus': 'series'
                },
                'type': 'bar',
            }
        ]
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
            option['series'][2]['data'] = gen_randlist(200)
            option['series'][3]['data'] = gen_randlist(200)
        return option
    app.run_server(debug=True)

if __name__ == '__main__':
    main()