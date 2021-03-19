import dash_echarts
import dash, time, random, json
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)

option1 = {
            "tooltip": {
                "trigger": 'item',
                "formatter": '{a} <br/>{b}: {c} ({d}%)'
            },
            "legend": {
                "data": ['直达', '营销广告', '搜索引擎', '邮件营销', '联盟广告', '视频广告', '百度', '谷歌', '必应', '其他']
            },
            "series": [
                {
                    "name": '访问来源',
                    "type": 'pie',
                    "selectedMode": 'single',
                    "radius": [0, '30%'],
                    "label": {
                        "position": 'inner',
                        "fontSize": 14,
                    },
                    "labelLine": {
                        "show": False
                    },
                    "data": [
                        {"value": 1548, "name": '搜索引擎'},
                        {"value": 775, "name": '直达'},
                        {"value": 679, "name": '营销广告', "selected": True}
                    ]
                },
                {
                    "name": '访问来源',
                    "type": 'pie',
                    "radius": ['45%', '60%'],
                    "labelLine": {
                        "length": 30,
                    },
                    "label": {
                        "formatter": '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                        "backgroundColor": '#F6F8FC',
                        "borderColor": '#8C8D8E',
                        "borderWidth": 1,
                        "borderRadius": 4,
                        
                        "rich": {
                            "a": {
                                "color": '#6E7079',
                                "lineHeight": 22,
                                "align": 'center'
                            },
                            "hr": {
                                "borderColor": '#8C8D8E',
                                "width": '100%',
                                "borderWidth": 1,
                                "height": 0
                            },
                            "b": {
                                "color": '#4C5058',
                                "fontSize": 14,
                                "fontWeight": 'bold',
                                "lineHeight": 33
                            },
                            "per": {
                                "color": '#fff',
                                "backgroundColor": '#4C5058',
                                "padding": [3, 4],
                                "borderRadius": 4
                            }
                        }
                    },
                    "data": [
                        {"value": 1048, "name": '百度'},
                        {"value": 335, "name": '直达'},
                        {"value": 310, "name": '邮件营销'},
                        {"value": 251, "name": '谷歌'},
                        {"value": 234, "name": '联盟广告'},
                        {"value": 147, "name": '必应'},
                        {"value": 135, "name": '视频广告'},
                        {"value": 102, "name": '其他'}
                    ]
                }
            ]
        }
option2 =  {
    'brush': {
        'toolbox': ['lineX', 'lineY', 'keep', 'clear'],
        'xAxisIndex': 0
    },
    'xAxis': {
        'type': 'category',
        'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    'yAxis': {
        'type': 'value'
    },
    'series': [{
        'data': [120, {
            'value': 200,
            'itemStyle': {
                'color': '#a90000'
            }
        }, 150, 80, 70, 110, 130],
        'type': 'bar'
    }],
    'toolbox': {
        'feature': {
            'magicType': {
                'type': ['stack', 'tiled']
            },
            'dataView': {}
        }
    },
}

option_stack = [option2]
app.layout = html.Div([
    dash_echarts.DashECharts(
        option = option2,
        # theme='dark',
        id='echarts',
    ),
    html.P('output1', id='output1'),
    html.P('output2', id='output2'),
    html.P('output3', id='output3'),
    dcc.Interval(id="refresh", interval=1 * 1000, n_intervals=0),
    html.Div(id="hidden_div", style={"display":"none"})


    
])

@app.callback(
    Output('output1', 'children'),
    [Input('echarts', 'n_clicks_data')])
def handler1(n_clicks_data):
    return 'clicked {}'.format(json.dumps(n_clicks_data))

@app.callback(
    Output('output2', 'children'),
    [Input('echarts', 'selected_data')])
def handler2(selected_data):
    return 'selected {}'.format(json.dumps(selected_data))

@app.callback(
    Output('output3', 'children'),
    [Input('echarts', 'brush_data')])
def handler3(brush_data):
    return 'brush {}'.format(json.dumps(brush_data))
# def update(n_intervals):
#     # time.sleep(3)
#     if n_intervals == 0:
#         raise PreventUpdate
#     else:
#         option={
#             "xAxis": {
#                 "type": 'category',
#                 "data": ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#             },
#             "yAxis": {
#                 "type": 'value'
#             },
#             "series": [{
#                 "data": random.sample(range(2000), 7),
#                 "type": 'line',
#                 "smooth": True
#             }]
#         }
#     return option

if __name__ == '__main__':
    app.run_server(debug=True)
