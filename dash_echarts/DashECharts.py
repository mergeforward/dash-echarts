# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashECharts(Component):
    """A DashECharts component.


Keyword arguments:
- n_clicks (number; default 0)
- n_clicks_timestamp (number; default -1)
- n_clicks_data (dict; optional)
- selected_data (dict; optional)
- brush_data (dict; optional)
- option (dict; optional)
- notMerge (boolean; optional)
- lazyUpdate (boolean; optional)
- theme (string; default 'vintage')
- events (list; optional)
- style (dict; optional)
- opts (dict; optional)
- maps (dict; optional)
- fun_formatter (boolean; default False)
- id (string; optional): The ID used to identify this component in Dash callbacks."""
    @_explicitize_args
    def __init__(self, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, n_clicks_data=Component.UNDEFINED, selected_data=Component.UNDEFINED, brush_data=Component.UNDEFINED, option=Component.UNDEFINED, notMerge=Component.UNDEFINED, lazyUpdate=Component.UNDEFINED, theme=Component.UNDEFINED, events=Component.UNDEFINED, style=Component.UNDEFINED, opts=Component.UNDEFINED, maps=Component.UNDEFINED, fun_formatter=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['n_clicks', 'n_clicks_timestamp', 'n_clicks_data', 'selected_data', 'brush_data', 'option', 'notMerge', 'lazyUpdate', 'theme', 'events', 'style', 'opts', 'maps', 'fun_formatter', 'id']
        self._type = 'DashECharts'
        self._namespace = 'dash_echarts'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['n_clicks', 'n_clicks_timestamp', 'n_clicks_data', 'selected_data', 'brush_data', 'option', 'notMerge', 'lazyUpdate', 'theme', 'events', 'style', 'opts', 'maps', 'fun_formatter', 'id']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashECharts, self).__init__(**args)
