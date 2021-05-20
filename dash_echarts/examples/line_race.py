import json
import datetime, time
from os import path
import dash
import dash_echarts
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath+'/static', 'life-expectancy-table.json'))
with open(filepath) as json_file:
    raw_data = json.load(json_file)


def get_countries():
    return list(set([e[3] for e in raw_data[1:]]))

dataset_with_filters = [
    {
        "id": f"dataset_{country}",
        "fromDatasetId": "dataset_raw",
        "transform": {
            "type": "filter",
            "config": {
                "and": [
                    {"dimension": "Year", "gte": 1950},
                    {"dimension": "Country", "=": country},
                ]
            },
        },
    }
    for country in get_countries()
]

series_list = [
    {
        "type": "line",
        "datasetId": f"dataset_{country}",
        "showSymbol": False,
        "name": country,
        "endLabel": {
            "show": True,
            "formatter": "line_race_formatter"
        },
        "labelLayout": {"moveOverlap": "shiftY"},
        "emphasis": {"focus": "series"},
        "encode": {
            "x": "Year",
            "y": "Income",
            "label": ["Country", "Income"],
            "itemName": "Year",
            "tooltip": ["Income"],
        },
    }
    for country in get_countries()
]

option = {
    "animationDuration": 10000,
    "animation": True,
    "dataset": [{"id": "dataset_raw", "source": raw_data}] + dataset_with_filters,
    "title": {"text": "Income since 1950"},
    "tooltip": {"order": "valueDesc", "trigger": "axis"},
    "xAxis": {"type": "category", "nameLocation": "middle"},
    "yAxis": {"name": "Income"},
    "grid": {"right": 140},
    "series": series_list,
}

layout = html.Div([
    dash_echarts.DashECharts(
        option = option,
        id='echarts',
        style={
            "width": '100%',
            "height": '100vh',
        },
        funs={
            "line_race_formatter":
            '''
            function(params){ 
                return params.value[3] + ': ' + params.value[0];
            }
            '''
        },
        fun_values=['line_race_formatter']
    ),
    dbc.Button('restart', color='success',
               id='line-race-button',
               style={
                   'position': 'absolute',
                   'height': 50, 'width': '5%',
                   'top': '25%', 'right': '15%',
                   'opacity': 0.8
               }
   ),
])

def main():
    app = dash.Dash(
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1"}
        ],
        suppress_callback_exceptions=True,
    )

    app.layout = layout

    @app.callback(
        Output('echarts', 'reset_id'),
        [Input("line-race-button", "n_clicks")],
    )
    def update_line_race(n_clicks):
        triggered = dash.callback_context.triggered
        # value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if n_clicks:
            if 'line-race-button' in prop_id:
                dtime = datetime.datetime.now()
                int_time = int(time.mktime(dtime.timetuple()))
                return int_time
        raise PreventUpdate

    app.run_server(debug=True)

if __name__ == '__main__':
    main()
