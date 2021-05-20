import dash_echarts
import dash, random
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.exceptions import PreventUpdate


def gen_week_data(num=100, high_value=90, low_value=60,
                           high_color='green',
                           mid_color='blue',
                           low_color='red'):
    result = []
    for n in random.sample(range(num), 7):
        if n >= high_value:
            color = high_color
        elif n < low_value:
            color = low_color
        else:
            color = mid_color
        result.append({
            "value": n,
            "itemStyle": {
                "color": color,
            },
            'label': {
                'show': True,
                'position': 'inside'
            },
        })
    return result

dropdowns = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("High Color"),
                dcc.Dropdown(
                    id="high-color",
                    options=[
                        {"label": col, "value": col} for col in dropdowns
                    ],
                    value="green",
                ),
            ],
        ),
        dbc.FormGroup(
            [
                dbc.Label("Mid Color"),
                dcc.Dropdown(
                    id="mid-color",
                    options=[
                        {"label": col, "value": col} for col in dropdowns
                    ],
                    value="blue",
                ),
            ],
        ),
        dbc.FormGroup(
            [
                dbc.Label("Low Color"),
                dcc.Dropdown(
                    id="low-color",
                    options=[
                        {"label": col, "value": col} for col in dropdowns
                    ],
                    value="red",
                ),
            ],
        ),
    ],

    body=True,
    style={
        'position': 'absolute',
        'height': 300, 'width': '10%',
        'top': '5%', 'right': '10%',
        'opacity': 0.8

    }
)

def main():
    """
    dash_echarts examples
    name: bar style with echarts
    author: dameng <pingf0@gmail.com>
    """
    app = dash.Dash(__name__)

    option = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {
            "type": "value",
            "max": 100,
            "min": 0
        },
        "series": [
            {
                "data": gen_week_data(100),
                "type": "bar",
            }
        ],
    }

    app.layout = dbc.Container(
        [
            dbc.Row(
                [
                    dash_echarts.DashECharts(
                        option=option,
                        id='echarts',
                        style={
                            "width": '100vw',
                            "height": '80vh',
                        }
                    ),
                ]
            ),
            controls,
            dcc.Interval(id="interval", interval=5 * 1000, n_intervals=0),
        ],
        fluid=True,
    )

    @app.callback(
        Output('echarts', 'option'),
        [Input('interval', 'n_intervals'),
         Input('high-color', 'value'),
         Input('mid-color', 'value'),
         Input('low-color', 'value'),
         ],

        [State('echarts', 'option')]
    )
    def update(n_intervals, high_color, mid_color, low_color, opt):
        if n_intervals == 0:
            raise PreventUpdate
        else:
            opt['series'][0]['data'] = gen_week_data(100,
                                                        high_color=high_color,
                                                        mid_color=mid_color,
                                                        low_color=low_color)
        return opt

    app.run_server(debug=True)

if __name__ == '__main__':
    main()