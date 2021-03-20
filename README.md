# dash_echarts


## quick play

step 1. run command

```
pip install 'dash_echarts[play]'
```

step 2. run command

```
echarts_play
```

step 3. access url

```
http://127.0.0.1:8050/
```

![](dash_echarts_line.gif)

## how to install

```bash
pip install dash_echarts
```

## how to use
```python
app.layout = html.Div([
    dash_echarts.DashECharts(
        option = option,
        id='echarts',
    ),
    ...
]) ```

then you can modify option in python

## full example
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
    '''
    dash_echarts examples
    name: smooth line with echarts
    author: dameng <pingf0@gmail.com>
    '''
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
            'data': gen_randlist(200),
            'type': 'line',
            'smooth': True
        }, {
            'data': gen_randlist(200),
            'type': 'line',
            'smooth': True
        }]
    } 
    events = []

    app.layout = html.Div([
        dash_echarts.DashECharts(
            option = option,
            events = events,
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