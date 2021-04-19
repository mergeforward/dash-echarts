# AUTO GENERATED FILE - DO NOT EDIT

dashECharts <- function(id=NULL, brush_data=NULL, events=NULL, fun_effects=NULL, fun_keys=NULL, fun_paths=NULL, fun_values=NULL, funs=NULL, lazyUpdate=NULL, maps=NULL, n_clicks=NULL, n_clicks_data=NULL, n_clicks_timestamp=NULL, notMerge=NULL, option=NULL, opts=NULL, selected_data=NULL, style=NULL, theme=NULL) {
    
    props <- list(id=id, brush_data=brush_data, events=events, fun_effects=fun_effects, fun_keys=fun_keys, fun_paths=fun_paths, fun_values=fun_values, funs=funs, lazyUpdate=lazyUpdate, maps=maps, n_clicks=n_clicks, n_clicks_data=n_clicks_data, n_clicks_timestamp=n_clicks_timestamp, notMerge=notMerge, option=option, opts=opts, selected_data=selected_data, style=style, theme=theme)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashECharts',
        namespace = 'dash_echarts',
        propNames = c('id', 'brush_data', 'events', 'fun_effects', 'fun_keys', 'fun_paths', 'fun_values', 'funs', 'lazyUpdate', 'maps', 'n_clicks', 'n_clicks_data', 'n_clicks_timestamp', 'notMerge', 'option', 'opts', 'selected_data', 'style', 'theme'),
        package = 'dashEcharts'
        )

    structure(component, class = c('dash_component', 'list'))
}
