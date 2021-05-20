import dash_echarts
import dash_html_components as html
import dash_core_components as dcc

option = {
    "title": {
        "text": "Income & Expenditure",
    },
    "tooltip": {
        "trigger": "axis",
        "axisPointer": {"type": "shadow"},
        "formatter": "bar_waterfall_formatter"
    },
    "legend": {"data": ["Income", "Expenditure"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {
        "type": "category",
        "splitLine": {"show": False},
        "data": [f"Nov. {i}" for i in range(1, 12)],
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "acc",
            "type": "bar",
            "stack": "Total",
            "itemStyle": {
                "barBorderColor": "rgba(0,0,0,0)",
                "color": "rgba(0,0,0,0)",
            },
            "emphasis": {
                "itemStyle": {
                    "barBorderColor": "rgba(0,0,0,0)",
                    "color": "rgba(0,0,0,0)",
                }
            },
            "data": [0, 900, 1245, 1530, 1376, 1376, 1511, 1689, 1856, 1495, 1292],
        },
        {
            "name": "Income",
            "type": "bar",
            "stack": "Total",
            "label": {"show": True, "position": "top"},
            "data": [900, 345, 393, "-", "-", 135, 178, 286, "-", "-", "-"],
        },
        {
            "name": "Expenditure",
            "type": "bar",
            "stack": "Total",
            "label": {"show": True, "position": "bottom"},
            "data": ["-", "-", "-", 108, 154, "-", "-", "-", 119, 361, 203],
        },
    ],
}



layout = html.Div([
    dash_echarts.DashECharts(
        option = option,
        id='echarts-bar-waterfall',

        funs={
            "bar_waterfall_formatter":
            '''
            function(params){ 
                var tar;
                if(params[1].value!=='-'){
                    tar=params[1]
                }else{
                    tar=params[2]
                }
                return tar.name+'<br/>'+tar.seriesName+' : '+tar.value
            }
            '''
        },
        fun_values=['bar_waterfall_formatter'],
        style={
            "width": '100%',
            "height": '100vh',
        }
    ),
    dcc.Markdown("""
    
    ```python
    import dash_echarts
    import dash, random
    from dash.dependencies import Input, Output
    import dash_html_components as html
    import dash_core_components as dcc
    from dash.exceptions import PreventUpdate


    def main():
        app = dash.Dash(__name__)

        option = {
            "title": {
                "text": "Income & Expenditure",
            },
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "shadow"},
                "formatter": "bar_waterfall_formatter"
            },
            "legend": {"data": ["Income", "Expenditure"]},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": {
                "type": "category",
                "splitLine": {"show": False},
                "data": [f"Nov. {i}" for i in range(1, 12)],
            },
            "yAxis": {"type": "value"},
            "series": [
                {
                    "name": "acc",
                    "type": "bar",
                    "stack": "Total",
                    "itemStyle": {
                        "barBorderColor": "rgba(0,0,0,0)",
                        "color": "rgba(0,0,0,0)",
                    },
                    "emphasis": {
                        "itemStyle": {
                            "barBorderColor": "rgba(0,0,0,0)",
                            "color": "rgba(0,0,0,0)",
                        }
                    },
                    "data": [0, 900, 1245, 1530, 1376, 1376, 1511, 1689, 1856, 1495, 1292],
                },
                {
                    "name": "Income",
                    "type": "bar",
                    "stack": "Total",
                    "label": {"show": True, "position": "top"},
                    "data": [900, 345, 393, "-", "-", 135, 178, 286, "-", "-", "-"],
                },
                {
                    "name": "Expenditure",
                    "type": "bar",
                    "stack": "Total",
                    "label": {"show": True, "position": "bottom"},
                    "data": ["-", "-", "-", 108, 154, "-", "-", "-", 119, 361, 203],
                },
            ],
        }

        dash_echarts.DashECharts(
            option = option,
            id='echarts-bar-basic',

            funs={
                "bar_waterfall_formatter":
                '''
                function(params){
                    var tar;
                    if(params[1].value!=='-'){
                        tar=params[1]
                    }else{
                        tar=params[2]
                    }
                    return tar.name+'<br/>'+tar.seriesName+' : '+tar.value
                }
                '''
            },
            fun_values=['bar_waterfall_formatter'],
            style={
                "width": '100%',
                "height": '100vh',
            }
        )


        @app.callback(
        Output('echarts', 'option'),
        [Input('interval', 'n_intervals')])
        def update(n_intervals):
            if n_intervals == 0:
                raise PreventUpdate
            else:
                option['series'][0]['data'] = gen_randlist(200)
                option['series'][1]['data'] = gen_randlist(200)
            return option
        app.run_server(debug=True)

    if __name__ == '__main__':
        main()
    ```
""",
                 style={
                     # "display": 'block',
                     "width": '80%',
                     "marginLeft": '10%',
                     "marginRight": '10%',
                     "height": '100vh',
                 }
                 ),
])