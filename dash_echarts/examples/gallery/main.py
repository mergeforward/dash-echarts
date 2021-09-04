import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([
    dcc.Markdown(
        '''
        # How to install
        
        ```bash
        pip install 'dash_echarts[play]'
        ```
        
        this command will install the dash_echarts, several demos and all related cool dash plugins.
        
        you can also install the dash_echarts purely by `pip install dash_echarts`
         
        # run the command to start the gallery app
        
        ```bash
        echarts_play
        ```
        
        # Quick Hands-on Demo
        
        ### line basic demo 
        ![](/static/dash_echarts_line.gif)  
        
        ```python
        import dash_echarts
        import dash, random
        from dash.dependencies import Input, Output
        import dash_html_components as html
        import dash_core_components as dcc
        from dash.exceptions import PreventUpdate

        def gen_randlist(num):
            return random.sample(range(num), 7)

        def main():
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
                    'data': random.sample(range(200), 7),
                    'type': 'line',
                    'smooth': True
                }, {
                    'data': random.sample(range(100), 7),
                    'type': 'line',
                    'smooth': True
                }]
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
                return option
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