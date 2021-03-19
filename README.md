# dash_echarts

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
])
```

you can define option in python