# AUTO GENERATED FILE - DO NOT EDIT

dashECharts <- function(n_clicks=NULL, n_clicks_timestamp=NULL, n_clicks_data=NULL, selected_data=NULL, brush_data=NULL, option=NULL, notMerge=NULL, lazyUpdate=NULL, theme=NULL, events=NULL, style=NULL, opts=NULL, maps=NULL, funs=NULL, fun_keys=NULL, fun_paths=NULL, id=NULL) {
    
    props <- list(n_clicks=n_clicks, n_clicks_timestamp=n_clicks_timestamp, n_clicks_data=n_clicks_data, selected_data=selected_data, brush_data=brush_data, option=option, notMerge=notMerge, lazyUpdate=lazyUpdate, theme=theme, events=events, style=style, opts=opts, maps=maps, funs=funs, fun_keys=fun_keys, fun_paths=fun_paths, id=id)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashECharts',
        namespace = 'dash_echarts',
        propNames = c('n_clicks', 'n_clicks_timestamp', 'n_clicks_data', 'selected_data', 'brush_data', 'option', 'notMerge', 'lazyUpdate', 'theme', 'events', 'style', 'opts', 'maps', 'funs', 'fun_keys', 'fun_paths', 'id'),
        package = 'dashEcharts'
        )

    structure(component, class = c('dash_component', 'list'))
}
