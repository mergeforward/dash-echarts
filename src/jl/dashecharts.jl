# AUTO GENERATED FILE - DO NOT EDIT

export dashecharts

"""
    dashecharts(;kwargs...)

A DashECharts component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `amap_token` (String; optional)
- `axis_pointer_data` (Dict; optional)
- `bmap_token` (String; optional)
- `brush_data` (Dict; optional)
- `click_data` (Dict; optional)
- `event` (Dict; optional)
- `fun_afters` (Array; optional)
- `fun_befores` (Array; optional)
- `fun_keys` (Array; optional)
- `fun_loaded` (Array; optional)
- `fun_paths` (Dict; optional)
- `fun_values` (Array; optional)
- `funs` (Dict; optional)
- `mapbox_token` (String; optional)
- `maps` (Dict; optional)
- `n_clicks` (Real; optional)
- `n_clicks_timestamp` (Real; optional)
- `option` (Dict; optional)
- `reset_id` (Real; optional)
- `resize_id` (Real; optional)
- `selected_data` (Dict; optional)
- `style` (Dict; optional)
"""
function dashecharts(; kwargs...)
        available_props = Symbol[:id, :amap_token, :axis_pointer_data, :bmap_token, :brush_data, :click_data, :event, :fun_afters, :fun_befores, :fun_keys, :fun_loaded, :fun_paths, :fun_values, :funs, :mapbox_token, :maps, :n_clicks, :n_clicks_timestamp, :option, :reset_id, :resize_id, :selected_data, :style]
        wild_props = Symbol[]
        return Component("dashecharts", "DashECharts", "dash_echarts", available_props, wild_props; kwargs...)
end

