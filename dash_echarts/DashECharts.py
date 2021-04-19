# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashECharts(Component):
    """A DashECharts component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- brush_data (dict; optional)

- events (list; optional)

- fun_effects (list; optional)

- fun_keys (list; optional)

- fun_paths (dict; optional)

- fun_values (list; optional)

- funs (dict; optional)

- lazyUpdate (boolean; optional)

- maps (dict; optional)

- n_clicks (number; default 0)

- n_clicks_data (dict; optional)

- n_clicks_timestamp (number; default -1)

- notMerge (boolean; optional)

- option (dict; optional)

- opts (dict; optional)

- selected_data (dict; optional)

- style (dict; optional)

- theme (string; default 'vintage')"""
    @_explicitize_args
    def __init__(self, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, n_clicks_data=Component.UNDEFINED, selected_data=Component.UNDEFINED, brush_data=Component.UNDEFINED, option=Component.UNDEFINED, notMerge=Component.UNDEFINED, lazyUpdate=Component.UNDEFINED, theme=Component.UNDEFINED, events=Component.UNDEFINED, style=Component.UNDEFINED, opts=Component.UNDEFINED, maps=Component.UNDEFINED, funs=Component.UNDEFINED, fun_keys=Component.UNDEFINED, fun_values=Component.UNDEFINED, fun_paths=Component.UNDEFINED, fun_effects=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'brush_data', 'events', 'fun_effects', 'fun_keys', 'fun_paths', 'fun_values', 'funs', 'lazyUpdate', 'maps', 'n_clicks', 'n_clicks_data', 'n_clicks_timestamp', 'notMerge', 'option', 'opts', 'selected_data', 'style', 'theme']
        self._type = 'DashECharts'
        self._namespace = 'dash_echarts'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'brush_data', 'events', 'fun_effects', 'fun_keys', 'fun_paths', 'fun_values', 'funs', 'lazyUpdate', 'maps', 'n_clicks', 'n_clicks_data', 'n_clicks_timestamp', 'notMerge', 'option', 'opts', 'selected_data', 'style', 'theme']
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
