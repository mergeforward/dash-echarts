import dash_echarts
import dash, random
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate



def main():
    '''
    dash_echarts examples
    name: custom profit with echarts
    author: dameng <pingf0@gmail.com>
    '''
    app = dash.Dash(__name__)
    raw = [
        [10, 16, 3, 'A'], 
        [16, 18, 15, 'B'], 
        [18, 26, 12, 'C'], 
        [26, 32, 22, 'D'], 
        [32, 56, 7, 'E'], 
        [56, 62, 17, 'F']
    ];
    color_list = ['#4f81bd', '#c0504d', '#9bbb59', '#604a7b', '#948a54', '#e46c0b'];
    data = []
    for i,e in enumerate(raw):
        data.append({
            'value': e,
            'itemStyle': {
                'color': color_list[i]
            }
        })


    option =  {
        'title': {
            'text': 'Profit',
            'left': 'center'
        },
        'tooltip': {
        },
        'xAxis': {
            'scale': True
        },
        'yAxis': {
        },
        'series': [{
            'type': 'custom',
            'renderItem': 'ri',
            'label': {
                'show': True,
                'position': 'top'
            },
            'dimensions': ['from', 'to', 'profit'],
            'encode': {
                'x': [0, 1],
                'y': 2,
                'tooltip': [0, 1, 2],
                'itemName': 3
            },
            'data': data
        }]
    }; 

    app.layout = html.Div([
        dash_echarts.DashECharts(
            option = option,
            id='echarts',
            fun_keys=['renderItem'],
            funs= {
                'ri': '''
                function renderItem(params, api) {
                    var yValue = api.value(2);
                    var start = api.coord([api.value(0), yValue]);
                    var size = api.size([api.value(1) - api.value(0), yValue]);
                    var style = api.style();

                    return {
                        type: 'rect',
                        shape: {
                            x: start[0],
                            y: start[1],
                            width: size[0],
                            height: size[1]
                        },
                        style: style
                    };
                }
                '''
            },
            style={
                "width": '100vw',
                "height": '100vh',
            }
        ),
        dcc.Interval(id="interval", interval=1 * 1000, n_intervals=0),
    ])


    app.run_server(debug=True)

if __name__ == '__main__':
    main()