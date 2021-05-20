import dash_echarts
import dash_html_components as html
import dash_core_components as dcc


option = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Direct", "Mail Ad", "Affiliate Ad", "Video Ad", "Search Engine"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "series": [
        {
            "name": "Direct",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [320, 302, 301, 334, 390, 330, 320],
        },
        {
            "name": "Mail Ad",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [120, 132, 101, 134, 90, 230, 210],
        },
        {
            "name": "Affiliate Ad",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [220, 182, 191, 234, 290, 330, 310],
        },
        {
            "name": "Video Ad",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [150, 212, 201, 154, 190, 330, 410],
        },
        {
            "name": "Search Engine",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": [820, 832, 901, 934, 1290, 1330, 1320],
        },
    ],
}

layout = html.Div([
    dash_echarts.DashECharts(
        option = option,
        id='echarts-bar-horizontal-stacked',
        style={
            "width": '100%',
            "height": '100vh',
        }
    ),
    dcc.Markdown('''
    
    ```python
    import dash_echarts
    import dash
    import dash_html_components as html
    import dash_core_components as dcc

    def main():
        app = dash.Dash(__name__)

        option = {
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "legend": {
                "data": ["Direct", "Mail Ad", "Affiliate Ad", "Video Ad", "Search Engine"]
            },
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": {"type": "value"},
            "yAxis": {
                "type": "category",
                "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            },
            "series": [
                {
                    "name": "Direct",
                    "type": "bar",
                    "stack": "total",
                    "label": {"show": True},
                    "emphasis": {"focus": "series"},
                    "data": [320, 302, 301, 334, 390, 330, 320],
                },
                {
                    "name": "Mail Ad",
                    "type": "bar",
                    "stack": "total",
                    "label": {"show": True},
                    "emphasis": {"focus": "series"},
                    "data": [120, 132, 101, 134, 90, 230, 210],
                },
                {
                    "name": "Affiliate Ad",
                    "type": "bar",
                    "stack": "total",
                    "label": {"show": True},
                    "emphasis": {"focus": "series"},
                    "data": [220, 182, 191, 234, 290, 330, 310],
                },
                {
                    "name": "Video Ad",
                    "type": "bar",
                    "stack": "total",
                    "label": {"show": True},
                    "emphasis": {"focus": "series"},
                    "data": [150, 212, 201, 154, 190, 330, 410],
                },
                {
                    "name": "Search Engine",
                    "type": "bar",
                    "stack": "total",
                    "label": {"show": True},
                    "emphasis": {"focus": "series"},
                    "data": [820, 832, 901, 934, 1290, 1330, 1320],
                },
            ],
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
                     # "display": 'block',
                     "width": '80%',
                     "marginLeft": '10%',
                     "marginRight": '10%',
                     "height": '100vh',
                 }
                 ),
])