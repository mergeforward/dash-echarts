import dash_echarts
import dash, random
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate


def gen_data(num):
    result = []
    for i in range(24):
        for j in range(7):
            d = {'name': ['a','b','c','d','e','f','g'][random.randint(0,6)], 'value': [i, j, random.randint(0, num)]}
            result.append(d)
    return result


def main():
    '''
    dash_echarts examples
    name: heat with echarts
    author: dameng <pingf0@gmail.com>
    '''
    app = dash.Dash(__name__)
    hours = ['12a', '1a', '2a', '3a', '4a', '5a', '6a',
             '7a', '8a', '9a', '10a', '11a',
             '12p', '1p', '2p', '3p', '4p', '5p',
             '6p', '7p', '8p', '9p', '10p', '11p']
    days = ['Saturday', 'Friday', 'Thursday',
            'Wednesday', 'Tuesday', 'Monday', 'Sunday']

    option = {
        'tooltip': {
            'position': 'top'
        },
        'grid': {
            'height': '50%',
            'top': '5%'
        },
        'xAxis': {
            'type': 'category',
            'data': hours,
            'splitArea': {
                'show': True
            }
        },
        'yAxis': {
            'type': 'category',
            'data': days,
            'splitArea': {
                'show': True
            }
        },
        'visualMap': {
            'min': 0,
            'max': 100,
            'calculable': True,
            'show': False,
            'orient': 'horizontal',
            'left': 'center',
            'bottom': '35%',
            'inRange': {
                'color': ['#ffff00', '#ff0000']
            }
        },
        'series': [{
            # 'symbol': 'none',

            'name': 'Punch Card',
            'type': 'heatmap',
            'data': gen_data(100),
            'label': {
                'show': True,
                'formatter': 'fm',
                'textStyle': {
                    'fontSize': '10px'
                },
                'rich': {
                    'large': {
                        'color': 'black',
                        'fontSize': '30px'
                    },
                    'small': {
                        'color': 'darkblue',
                        'fontSize': '15px'
                    }
                },
            },
            
            'emphasis': {
                'itemStyle': {
                    'shadowBlur': 10,
                    'shadowColor': 'rgba(0, 0, 0, 0.5)'
                }
            }
        }]
    }

    app.layout = html.Div([
        dash_echarts.DashECharts(
            fun_effects=[
                {'name':'t', 'option':{'a':1, 'b':2}},
                {'name':'t', 'option':{'a':3, 'b':4}}
            ],
            funs = {
                "t": '''
                function(option){
                    console.log(option)
                    console.log('hahahahehehe')
                    console.log(this.m)
                    this.m()
                }
                ''',
                
                "m": '''
                    function(){
                        console.log('yiiyiyiyiyiiy')
                    }
                ''',
                "fm": '''
                function (p){ 
                    if (p.value[2]<60) 
                        return '{small|'+p.name+'}'+
                            '\\n\\n'+
                            '{large|'+p.value[2]+'}';
                    return '{small|'+p.name+'}'+
                        '\\n\\n'+
                        p.value[2];
                }
                '''
            },
            option = option,
            id='echarts',
            fun_values=['fm'],
            # fun_keys=['formatter'],
            # fun_paths={'fm': ['series', '0', 'label', 'formatter']},
            style={
                "width": '100vw',
                "height": '100vh',
            }
        ),
        dcc.Interval(id="interval", interval=5 * 1000, n_intervals=0),
    ])


    @app.callback(
        Output('echarts', 'option'),
        [Input('interval', 'n_intervals')])
    def update(n_intervals):
        if n_intervals == 0:
            raise PreventUpdate
        else:
            option['series'][0]['data'] = gen_data(100)
        return option
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
    
    