import json
from os import path
import dash_echarts
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

basepath = path.dirname(__file__)
filepath = path.abspath(path.join(basepath+'/../static', 'life-expectancy-table.json'))
with open(filepath) as json_file:
    raw_data = json.load(json_file)

# countries = [
#     "Finland",
#     "France",
#     "Germany",
#     "Iceland",
#     "Norway",
#     "Poland",
#     "Russia",
#     "United Kingdom",
# ]

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
        id='echarts-line-race',
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
    dcc.Markdown('''
    
    ```python
    import json
    from os import path
    import dash_echarts
    import dash_html_components as html
    import dash_core_components as dcc



    def main():
        app = dash.Dash(__name__)

        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, 'life-expectancy-table.json'))
        with open(filepath) as json_file:
            raw_data = json.load(json_file)

        countries = [
            "Finland",
            "France",
            "Germany",
            "Iceland",
            "Norway",
            "Poland",
            "Russia",
            "United Kingdom",
        ]

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
            for country in countries
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
            for country in countries
        ]

        option = {
            "animationDuration": 10000,
            "dataset": [{"id": "dataset_raw", "source": raw_data}] + dataset_with_filters,
            "title": {"text": "Income in Europe since 1950"},
            "tooltip": {"order": "valueDesc", "trigger": "axis"},
            "xAxis": {"type": "category", "nameLocation": "middle"},
            "yAxis": {"name": "Income"},
            "grid": {"right": 140},
            "series": series_list,
        }

        app.layout = html.Div([
            dash_echarts.DashECharts(
                option = option,
                id='echarts',
                style={
                    "width": '100vw',
                    "height": '100vh',
                },
                funs={
                    "line_race_formatter":
                    """
                    function(params){
                        return params.value[3] + ': ' + params.value[0];
                    }
                    """
                },
                fun_values=['line_race_formatter']
    
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