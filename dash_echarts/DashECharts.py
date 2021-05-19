# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashECharts(Component):
    """A DashECharts component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- bmap_token (string; optional)

- brush_data (dict; optional)

- click_data (dict; optional)

- event (dict; optional)

- fun_effects (list; optional)

- fun_keys (list; optional)

- fun_paths (dict; optional)

- fun_prepares (list; optional)

- fun_values (list; optional)

- funs (dict; optional)

- mapbox_token (string; optional)

- maps (dict; optional)

- n_clicks (number; default 0)

- n_clicks_timestamp (number; default -1)

- option (dict; optional)

- reset_id (number; default 0)

- resize_id (number; default 0)

- selected_data (dict; optional)

- style (dict; optional)"""
    @_explicitize_args
    def __init__(self, resize_id=Component.UNDEFINED, reset_id=Component.UNDEFINED, n_clicks=Component.UNDEFINED, n_clicks_timestamp=Component.UNDEFINED, click_data=Component.UNDEFINED, selected_data=Component.UNDEFINED, brush_data=Component.UNDEFINED, style=Component.UNDEFINED, event=Component.UNDEFINED, option=Component.UNDEFINED, maps=Component.UNDEFINED, funs=Component.UNDEFINED, fun_keys=Component.UNDEFINED, fun_values=Component.UNDEFINED, fun_paths=Component.UNDEFINED, fun_effects=Component.UNDEFINED, fun_prepares=Component.UNDEFINED, mapbox_token=Component.UNDEFINED, bmap_token=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bmap_token', 'brush_data', 'click_data', 'event', 'fun_effects', 'fun_keys', 'fun_paths', 'fun_prepares', 'fun_values', 'funs', 'mapbox_token', 'maps', 'n_clicks', 'n_clicks_timestamp', 'option', 'reset_id', 'resize_id', 'selected_data', 'style']
        self._type = 'DashECharts'
        self._namespace = 'dash_echarts'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bmap_token', 'brush_data', 'click_data', 'event', 'fun_effects', 'fun_keys', 'fun_paths', 'fun_prepares', 'fun_values', 'funs', 'mapbox_token', 'maps', 'n_clicks', 'n_clicks_timestamp', 'option', 'reset_id', 'resize_id', 'selected_data', 'style']
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
