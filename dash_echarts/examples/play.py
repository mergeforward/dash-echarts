import dash
import time
import json
import datetime
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from .gallery.main import layout as layout_main
from .gallery.line_basic import layout as layout_line_basic
from .gallery.line_basic import gen_randlist as gen_line_basic
from .gallery.line_area_basic import layout as layout_line_area_basic
from .gallery.line_stacked import layout as layout_line_stacked
from .gallery.line_area_stacked import layout as layout_line_area_stacked
from .gallery.line_race import layout as layout_line_race
from .gallery.bar_basic import layout as layout_bar_basic
from .gallery.bar_basic import gen_randlist as gen_bar_basic
from .gallery.bar_style import layout as layout_bar_style
from .gallery.bar_style import gen_week_data as gen_bar_style
from .gallery.bar_waterfall import layout as layout_bar_waterfall
from .gallery.bar_horizontal_stacked import layout as layout_bar_horizontal_stacked
from .gallery.bar_race import layout as layout_bar_race
from .gallery.bar_race import gen_next_year_data as gen_bar_race
from os import path



basepath = path.dirname(__file__)
assets_path = f'{basepath}/static'

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
    assets_folder=assets_path,
    suppress_callback_exceptions=True,
)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

@app.server.route('/static/<path:path>')
def static_file(path):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, path)

# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("Gallery", className="display-4")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "borderColor": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "borderColor": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "Dash ECharts Gallery",
                    className="lead",
                ),
                html.P(
                    "Developed by Jesse MENG",
                    style = {
                        'color': 'gray',
                        'textAlign': 'right',
                        'opacity': 0.6,
                        'fontSize': 10
                    }
                ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Intro", href="/", active="exact"),
                    dbc.NavLink([html.P("Line: Basic ", style={'display': 'inline'}), dbc.Badge("Dynamic", color="success", className="mr-1")], href="/line-basic", active="exact"),
                    dbc.NavLink([html.P("Line: Area Basic ", style={'display': 'inline'}), dbc.Badge("Dynamic", color="success", className="mr-1")], href="/line-area-basic", active="exact"),
                    dbc.NavLink("Line: Stacked", href="/line-stacked", active="exact"),
                    dbc.NavLink("Line: Area Stacked", href="/line-area-stacked", active="exact"),
                    dbc.NavLink([html.P("Line: Racing ", style={'display': 'inline'}),
                                 dbc.Badge("Animated", color="orange", className="mr-1"),
                                 dbc.Badge("Interactive", color="primary", className="mr-1"),
                                 ], href="/line-race", active="exact"),
                    dbc.NavLink([html.P("Bar: Basic ", style={'display': 'inline'}), dbc.Badge("Dynamic", color="success", className="mr-1")], href="/bar-basic", active="exact"),
                    dbc.NavLink([html.P("Bar: Style ", style={'display': 'inline'}),
                                 dbc.Badge("Dynamic", color="success", className="mr-1"),
                                 dbc.Badge("Interactive", color="primary", className="mr-1"),
                                 ], href="/bar-style", active="exact"),
                    dbc.NavLink("Bar: Waterfall", href="/bar-waterfall", active="exact"),
                    dbc.NavLink("Bar: Horizontal Stacked", href="/bar-horizontal-stacked", active="exact"),
                    dbc.NavLink([html.P("Bar: Racing ", style={'display': 'inline'}),
                                 dbc.Badge("Dynamic", color="success", className="mr-1"),
                                 dbc.Badge("Animated", color="orange", className="mr-1"),
                                 dbc.Badge("Interactive", color="primary", className="mr-1"),
                                 ], href="/bar-race", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div(id="page-content")

app.layout = html.Div([
    dcc.Location(id="url"), sidebar, content,
    dcc.Interval(id="interval-1s", interval=1 * 1000, n_intervals=0),
])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return layout_main
    if pathname == "/line-basic":
      return layout_line_basic
    if pathname == "/line-area-basic":
        return layout_line_area_basic
    if pathname == "/line-stacked":
        return layout_line_stacked
    if pathname == "/line-area-stacked":
        return layout_line_area_stacked
    if pathname == "/line-race":
        return layout_line_race
    if pathname == "/bar-basic":
        return layout_bar_basic
    if pathname == "/bar-style":
        return layout_bar_style
    if pathname == "/bar-waterfall":
        return layout_bar_waterfall
    if pathname == "/bar-horizontal-stacked":
        return layout_bar_horizontal_stacked
    if pathname == "/bar-race":
        return layout_bar_race
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

####
@app.callback(
    Output('echarts-line-basic', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/line-basic':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-line-area-basic', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/line-area-basic':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-line-stacked', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/line-stacked':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-line-area-stacked', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/line-area-stacked':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-line-race', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/line-race':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-bar-basic', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/bar-basic':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-bar-style', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/bar-style':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate


@app.callback(
    Output('echarts-bar-waterfall', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/bar-waterfall':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-bar-horizontal-stacked', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/bar-horizontal-stacked':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-bar-race', 'resize_id'),
    [Input("sidebar-toggle", "n_clicks"), Input("url", "pathname")],
)
def resize(n, path):
    if path=='/bar-race':
        triggered = dash.callback_context.triggered
        value = triggered[0]['value']
        prop_id, event = triggered[0]['prop_id'].split('.')
        if 'sidebar-toggle' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-line-basic', 'option'),
    [Input('interval-1s', 'n_intervals'), Input("url", "pathname")],
    [State('echarts-line-basic', 'option')]
)
def update_line_basic(n_intervals, path, opt):
    if n_intervals > 0 and path == '/line-basic':
        opt['series'][0]['data'] = gen_line_basic(200)
        opt['series'][1]['data'] = gen_line_basic(100)
        return opt
    raise PreventUpdate


@app.callback(
        Output('echarts-line-area-basic', 'option'),
        [Input('interval-1s', 'n_intervals'), Input("url", "pathname")],
        [State('echarts-line-area-basic', 'option')]
)
def update_line_area_basic(n_intervals, path, opt):
    if n_intervals > 0 and path == '/line-area-basic':
        opt['series'][0]['data'] = gen_line_basic(100)
        opt['series'][1]['data'] = gen_line_basic(200)
        return opt
    raise PreventUpdate

@app.callback(
    Output('echarts-bar-basic', 'option'),
    [Input('interval-1s', 'n_intervals'), Input("url", "pathname")],
    [State('echarts-bar-basic', 'option')]
)
def update_line_basic(n_intervals, path, opt):
    if n_intervals > 0 and path == '/bar-basic':
        opt['series'][0]['data'] = gen_bar_basic(200)
        opt['series'][1]['data'] = gen_bar_basic(100)
        return opt
    raise PreventUpdate


@app.callback(
    Output('echarts-bar-style', 'option'),
    [Input('interval', 'n_intervals'),
     Input("url", "pathname"),
     Input('bar-style-high-color', 'value'),
     Input('bar-style-mid-color', 'value'),
     Input('bar-style-low-color', 'value'),
     ],
    [State('echarts-bar-style', 'option')]
)
def update(n_intervals, path, high_color, mid_color, low_color, opt):
    if n_intervals > 0 and n_intervals % 5 == 0 and path == '/bar-style':
        opt['series'][0]['data'] = gen_bar_style(100,
                                                high_color=high_color,
                                                mid_color=mid_color,
                                                low_color=low_color)
        return opt
    raise PreventUpdate

@app.callback(
    Output('echarts-line-race', 'reset_id'),
    [Input("url", "pathname"), Input("line-race-button", "n_clicks")],
)
def update_line_race(path, n_clicks):
    triggered = dash.callback_context.triggered
    # value = triggered[0]['value']
    prop_id, event = triggered[0]['prop_id'].split('.')
    if n_clicks and path == '/line-race':
        if 'line-race-button' in prop_id:
            dtime = datetime.datetime.now()
            int_time = int(time.mktime(dtime.timetuple()))
            return int_time
    raise PreventUpdate

@app.callback(
    Output('echarts-bar-race', 'option'),
    [Input('interval-1s', 'n_intervals'), Input("url", "pathname"), Input("bar-race-button", "n_clicks")],
    [State('echarts-bar-race', 'option')]
)
def update_bar_race(n_intervals, path, btn, opt):
    if n_intervals > 0 and path == '/bar-race':
        triggered = dash.callback_context.triggered
        prop_id, event = triggered[0]['prop_id'].split('.')
        if prop_id == 'bar-race-button':
            year = None
        else:
            year = int(opt['graphic']['elements'][0]['style']['text'])
        year, data = gen_bar_race(year=year)
        opt['graphic']['elements'][0]['style']['text'] = year
        opt['dataset']['source'] = data
        # same as below
        # opt['series'][0]['data'] = data
        return opt
    raise PreventUpdate

def main():
    app.run_server(debug=True)

if __name__ == "__main__":
    main()