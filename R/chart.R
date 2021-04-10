# AUTO GENERATED FILE - DO NOT EDIT

chart <- function(id=NULL, option=NULL, config=NULL, style=NULL, resizeObserver=NULL) {
    
    props <- list(id=id, option=option, config=config, style=style, resizeObserver=resizeObserver)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Chart',
        namespace = 'dash_echarts',
        propNames = c('id', 'option', 'config', 'style', 'resizeObserver'),
        package = 'dashEcharts'
        )

    structure(component, class = c('dash_component', 'list'))
}
