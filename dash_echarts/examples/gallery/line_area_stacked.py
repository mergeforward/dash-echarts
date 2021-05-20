import dash_echarts
import dash_html_components as html
import dash_core_components as dcc


option = {
    'title': {
        'text': 'Line Area Stacked'
    },
    'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
            'type': 'cross',
            'label': {
                'backgroundColor': '#6a7985'
            }
        }
    },
    'legend': {
        'data': ['Mail Ad', 'Affiliate Ad', 'Video Ad', 'Direct', 'Search Engine']
    },
    'grid': {
        'left': '3%',
        'right': '4%',
        'bottom': '3%',
        'containLabel': True
    },
    'toolbox': {
        'feature': {
            'saveAsImage': {}
        }
    },
    'xAxis': {
        'type': 'category',
        'boundaryGap': False,
        'data': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    },
    'yAxis': {
        'type': 'value'
    },
    'series': [
        {
            'name': 'Mail Ad',
            'type': 'line',
            'stack': 'Total',
            "areaStyle": {},
            "emphasis": {"focus": "series"},
            'data': [120, 132, 101, 134, 90, 230, 210],
        },
        {
            'name': 'Affiliate Ad',
            'type': 'line',
            'stack': 'Total',
            "areaStyle": {},
            "emphasis": {"focus": "series"},
            'data': [220, 182, 191, 234, 290, 330, 310],
        },
        {
            'name': 'Video Ad',
            'type': 'line',
            'stack': 'Total',
            'data': [150, 232, 201, 154, 190, 330, 410],
            "areaStyle": {},
            "emphasis": {"focus": "series"},
        },
        {
            'name': 'Direct',
            'type': 'line',
            'stack': 'Total',
            'data': [320, 332, 301, 334, 390, 330, 320],
            "areaStyle": {},
            "emphasis": {"focus": "series"},
        },
        {
            'name': 'Search Engine',
            'type': 'line',
            'stack': 'Total',
            'data': [820, 932, 901, 934, 1290, 1330, 1320],
            "areaStyle": {},
            "emphasis": {"focus": "series"},
        }
    ]
}

layout = html.Div([
    dash_echarts.DashECharts(
        option = option,
        id='echarts-line-area-stacked',
        style={
            "width": '100%',
            "height": '90vh',
        }
    ),
    dcc.Markdown('''
        ```python
        import dash_echarts
        import dash


        def main():
            app = dash.Dash(__name__)

            option = {
                'title': {
                    'text': 'Line Stacked'
                },
                'tooltip': {
                    'trigger': 'axis'
                },
                'legend': {
                    'data': ['Mail Ad', 'Affiliate Ad', 'Video Ad', 'Direct', 'Search Engine']
                },
                'grid': {
                    'left': '3%',
                    'right': '4%',
                    'bottom': '3%',
                    'containLabel': True
                },
                'toolbox': {
                    'feature': {
                        'saveAsImage': {}
                    }
                },
                'xAxis': {
                    'type': 'category',
                    'boundaryGap': False,
                    'data': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                },
                'yAxis': {
                    'type': 'value'
                },
                'series': [
                    {
                        'name': 'Mail Ad',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [120, 132, 101, 134, 90, 230, 210],
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
                    },
                    {
                        'name': 'Affiliate Ad',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [220, 182, 191, 234, 290, 330, 310],
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
                    },
                    {
                        'name': 'Video Ad',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [150, 232, 201, 154, 190, 330, 410],
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
                    },
                    {
                        'name': 'Direct',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [320, 332, 301, 334, 390, 330, 320],
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
                    },
                    {
                        'name': 'Search Engine',
                        'type': 'line',
                        'stack': 'Total',
                        'data': [820, 932, 901, 934, 1290, 1330, 1320],
                        "areaStyle": {},
                        "emphasis": {"focus": "series"},
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
            ])

            app.run_server(debug=True)

        if __name__ == '__main__':
            main()
        ```
    ''',
         style={
             "width": '80%',
             "marginLeft": '10%',
             "marginRight": '10%',
             "height": '100vh',
         }
    ),
])