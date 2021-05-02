# AUTO GENERATED FILE - DO NOT EDIT

dashECharts <- function(id=NULL, bmap_token=NULL, brush_data=NULL, event=NULL, fun_effects=NULL, fun_keys=NULL, fun_paths=NULL, fun_prepares=NULL, fun_values=NULL, funs=NULL, mapbox_token=NULL, maps=NULL, n_clicks=NULL, n_clicks_data=NULL, n_clicks_timestamp=NULL, option=NULL, selected_data=NULL, style=NULL) {
    
    props <- list(id=id, bmap_token=bmap_token, brush_data=brush_data, event=event, fun_effects=fun_effects, fun_keys=fun_keys, fun_paths=fun_paths, fun_prepares=fun_prepares, fun_values=fun_values, funs=funs, mapbox_token=mapbox_token, maps=maps, n_clicks=n_clicks, n_clicks_data=n_clicks_data, n_clicks_timestamp=n_clicks_timestamp, option=option, selected_data=selected_data, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashECharts',
        namespace = 'dash_echarts',
        propNames = c('id', 'bmap_token', 'brush_data', 'event', 'fun_effects', 'fun_keys', 'fun_paths', 'fun_prepares', 'fun_values', 'funs', 'mapbox_token', 'maps', 'n_clicks', 'n_clicks_data', 'n_clicks_timestamp', 'option', 'selected_data', 'style'),
        package = 'dashEcharts'
        )

    structure(component, class = c('dash_component', 'list'))
}
