import dash_echarts
import dash, random
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate


def gen_data():
    return [[random.uniform(0,30), random.randint(0,300)] for i in range(32)]


def main():
    '''
    dash_echarts examples
    name: hist bar with echarts
    author: dameng <pingf0@gmail.com>
    '''
    app = dash.Dash(__name__)

    option = {
        'dataset': [
            {
                'source': [
                            [28604,77,17096869,'Australia',1990],
                            [31163,77.4,27662440,'Canada',1990],
                            [1516,68,1154605773,'China',1990],
                            [13670,74.7,10582082,'Cuba',1990],
                            [28599,75,4986705,'Finland',1990],
                            [29476,77.1,56943299,'France',1990],
                            [31476,75.4,78958237,'Germany',1990],
                            [28666,78.1,254830,'Iceland',1990],
                            [1777,57.7,870601776,'India',1990],
                            [29550,79.1,122249285,'Japan',1990],
                            [2076,67.9,20194354,'North Korea',1990],
                            [12087,72,42972254,'South Korea',1990],
                            [24021,75.4,3397534,'New Zealand',1990],
                            [43296,76.8,4240375,'Norway',1990],
                            [10088,70.8,38195258,'Poland',1990],
                            [19349,69.6,147568552,'Russia',1990],
                            [10670,67.3,53994605,'Turkey',1990],
                            [26424,75.7,57110117,'United Kingdom',1990],
                            [37062,75.4,252847810,'United States',1990],
                            [44056,81.8,23968973,'Australia',2015],
                            [43294,81.7,35939927,'Canada',2015],
                            [13334,76.9,1376048943,'China',2015],
                            [21291,78.5,11389562,'Cuba',2015],
                            [38923,80.8,5503457,'Finland',2015],
                            [37599,81.9,64395345,'France',2015],
                            [44053,81.1,80688545,'Germany',2015],
                            [42182,82.8,329425,'Iceland',2015],
                            [5903,66.8,1311050527,'India',2015],
                            [36162,83.5,126573481,'Japan',2015],
                            [1390,71.4,25155317,'North Korea',2015],
                            [34644,80.7,50293439,'South Korea',2015],
                            [34186,80.6,4528526,'New Zealand',2015],
                            [64304,81.6,5210967,'Norway',2015],
                            [24787,77.3,38611794,'Poland',2015],
                            [23038,73.13,143456918,'Russia',2015],
                            [19360,76.5,78665830,'Turkey',2015],
                            [38225,81.4,64715810,'United Kingdom',2015],
                            [53354,79.1,321773631,'United States',2015]
                        ]
            }, 
            {
                'transform': {
                    'type': 'filter',
                    'config': { 'dimension': 4, 'eq': 1990 }
                }
            }, 
            {
                'transform': {
                    'type': 'filter',
                    'config': { 'dimension': 4, 'eq': 2015 }
                }
            }, 
            {
                'transform': {
                    'type': 'ecStat:regression',
                    'config': {
                        'method': 'logarithmic'
                    }
                }
            }
        ],
        'legend': {
            'data': ['1990', '2015']
        },
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'cross'
            }
        },
        'xAxis': {
            'type': 'value',
            'splitLine': {
                'lineStyle': {
                    'type': 'dashed'
                }
            },
        },
        'yAxis': {
            'type': 'value',
            'splitLine': {
                'lineStyle': {
                    'type': 'dashed'
                }
            },
        },
        'visualMap': {
            'show': False,
            'dimension': 2,
            'min': 20000,
            'max': 1500000000,
            'seriesIndex': [0, 1],
            'inRange': {
                'symbolSize': [10, 70]
            }
        },
        'series': [
            {
                'name': '1990',
                'type': 'scatter',
                'datasetIndex': 1
            },
            {
                'name': '2015',
                'type': 'scatter',
                'datasetIndex': 2
            }, 
            {
                'name': 'line',
                'type': 'line',
                'smooth': True,
                'datasetIndex': 3,
                'symbolSize': 0.1,
                'symbol': 'circle',
                'label': { 'show': True, 'fontSize': 16 },
                'labelLayout': { 'dx': -20 },
                'encode': { 'label': 2, 'tooltip': 1 }
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
        # dcc.Interval(id="interval", interval=1 * 1000, n_intervals=0),
    ])


    # @app.callback(
    #     Output('echarts', 'option'),
    #     [Input('interval', 'n_intervals')])
    # def update(n_intervals):
    #     if n_intervals == 0:
    #         raise PreventUpdate
    #     else:
    #         option['dataset'][0]['source'] = gen_data()
    #     return option


    app.run_server(debug=True)

if __name__ == '__main__':
    main()