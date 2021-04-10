# AUTO GENERATED FILE - DO NOT EDIT

export chart

"""
    chart(;kwargs...)

A Chart component.

Keyword arguments:
- `id` (Bool | Real | String | Dict | Array; optional)
- `option` (Bool | Real | String | Dict | Array; optional)
- `config` (Bool | Real | String | Dict | Array; optional)
- `style` (Bool | Real | String | Dict | Array; optional)
- `resizeObserver` (Dict; optional)
"""
function chart(; kwargs...)
        available_props = Symbol[:id, :option, :config, :style, :resizeObserver]
        wild_props = Symbol[]
        return Component("chart", "Chart", "dash_echarts", available_props, wild_props; kwargs...)
end

