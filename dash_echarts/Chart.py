# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Chart(Component):
    """A Chart component.


Keyword arguments:
- id (boolean | number | string | dict | list; optional)
- option (boolean | number | string | dict | list; optional)
- config (boolean | number | string | dict | list; optional)
- style (boolean | number | string | dict | list; optional)
- resizeObserver (dict; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, option=Component.UNDEFINED, config=Component.UNDEFINED, style=Component.UNDEFINED, resizeObserver=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'option', 'config', 'style', 'resizeObserver']
        self._type = 'Chart'
        self._namespace = 'dash_echarts'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'option', 'config', 'style', 'resizeObserver']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Chart, self).__init__(**args)
