import React, {useEffect, useRef} from 'react';
import PropTypes from 'prop-types';
import ReactECharts from 'echarts-for-react';
import * as gl from 'echarts-gl';
import * as echarts from 'echarts';
import * as ramda from 'ramda';
import * as ecStat from 'echarts-stat';

const loadFuns = (obj) => {
    Object.keys(obj).forEach(key => {
        if (typeof obj[key] === 'string' && !['chart','echarts', 'ramda', 'gl', 'ecStat'].includes(key)) {
            let fun = new Function("return "+obj[key].trim()+".bind(this)").bind(obj)
            obj[key] = fun();
        }
    })
}

function DashECharts(props)  {

    const {
        n_clicks, n_clicks_timestamp, 
        n_clicks_data, selected_data, brush_data, 
        events, option, 
        not_merge, lazy_update, theme,
        style, opts, 
        maps,
        funs, fun_keys, fun_values, fun_paths, fun_effects,
        id, setProps
    } = props;


    function clickHandler(e) {
        setProps({
            n_clicks: n_clicks + 1,
            n_clicks_timestamp: Date.now(),
            n_clicks_data: ramda.pick([
                'componentType', 
                'seriesType', 'seriesIndex', 'seriesName',
                'name',
                'dataIndex', 'data', 'dataType',
                'value', 'color',
                ], e)
            });
    }

    function selectChangedHandler(e) {
        setProps({
            selected_data: ramda.pick([
                'escapeConnect', 
                'fromAction', 'fromActionPayload', 'isFromClick',
                'selected', 'type'
            ], e)
        });
    }

    function brushEndHandler(e) {
        setProps({
            brush_data: ramda.pick([
                'areas', 'brushId', 'type'
            ], e)
        });
    }

    function eventsHandlers(events) {
        let eventsDict = {
            'click': events => clickHandler(events),
            'selectchanged': events => selectChangedHandler(events),
            'brushEnd': events => brushEndHandler(events),
        }
        return ramda.pick(events, eventsDict)
    }

    const registerMapForEach = (value, key) => echarts.registerMap(key, value);


    const funConverterKeys = (obj) => {
        Object.keys(obj).forEach(key => {
            if (typeof obj[key] === 'string') { 

                if (fun_keys.includes(key)) {
                    obj[key] = funs[obj[key]]
                } 
            }     
            else if (typeof obj[key] === 'object') {
                funConverterKeys(obj[key])
            }
        })
    }

    const funConverterValues = (obj) => {
        Object.keys(obj).forEach(key => {
            let v = obj[key]
            if (typeof v === 'string') { 
                if (fun_values.includes(v)) {
                    obj[key] = funs[v]
                } 
            }     
            else if (typeof v === 'object') {
                funConverterValues(v)
            }
        })
    }
    
    const funConverterPaths = (obj) => {
        for (const prop in fun_paths) {
            ramda.assocPath(fun_paths[prop], funs[prop], obj)
        }
    }

    const chartRef = useRef(null);
    funs['echarts'] = echarts;
    funs['ramda'] = ramda;
    funs['gl'] = gl;
    funs['ecStat'] = ecStat;
    funs['chart'] = chartRef;
    loadFuns(funs)

    if (!ramda.isEmpty(fun_keys)) funConverterKeys(option)
    if (!ramda.isEmpty(fun_values)) funConverterValues(option)
    if (!ramda.isEmpty(fun_paths)) funConverterPaths(option)
    
    echarts.registerTransform(ecStat.transform.regression);
    echarts.registerTransform(ecStat.transform.histogram);
    echarts.registerTransform(ecStat.transform.clustering);
    useEffect(() => {
        if (!ramda.isEmpty(maps))   ramda.forEachObjIndexed(registerMapForEach, maps);
        if (!ramda.isEmpty(fun_effects)) {
            fun_effects.forEach(e => {
                if (typeof e === 'string') {
                    funs[e]()
                } else {
                    funs[e.name](e.option)
                }
            })
        } 
        funs['chart'] = chartRef;

        const chart = chartRef.current.getEchartsInstance();
        chart.on("click", e => {
            setProps({
                n_clicks: n_clicks + 1,
                n_clicks_timestamp: Date.now(),
                n_clicks_data: ramda.pick([
                    'componentType', 
                    'seriesType', 'seriesIndex', 'seriesName',
                    'name',
                    'dataIndex', 'data', 'dataType',
                    'value', 'color',
                    ], e)
            });
        });
        chart.on("selectchanged", e => {
            setProps({
                selected_data: ramda.pick([
                    'escapeConnect', 
                    'fromAction', 'fromActionPayload', 'isFromClick',
                    'selected', 'type'
                ], e)
            });
        })
        chart.on("brushEnd", e => {
            setProps({
                brush_data: ramda.pick([
                    'areas', 'brushId', 'type'
                ], e)
            });
        })
    }, []);


    return (
        <ReactECharts
            id={id}
            ref={chartRef}
            option={option}
            notMerge={not_merge}
            lazyUpdate={lazy_update}
            theme={theme}
            // onEvents={eventsHandlers(events)}
            style={style}
            opts={opts}
        />
    );
}

DashECharts.defaultProps = {
    theme: 'vintage',
    n_clicks: 0,
    n_clicks_timestamp: -1,
    n_clicks_data: {},
    selected_data: {},
    brush_data: {},
    events: [],
    style: {},
    opts: {},
    maps: {},
    fun_keys: [],
    fun_values: [],
    fun_paths: {},
    fun_effects: [],
    funs: {},
};

DashECharts.propTypes = {
    n_clicks: PropTypes.number,
    n_clicks_timestamp: PropTypes.number,
    n_clicks_data: PropTypes.object,
    selected_data: PropTypes.object,
    brush_data: PropTypes.object,
    option: PropTypes.object,
    notMerge: PropTypes.bool,
    lazyUpdate: PropTypes.bool,
    theme: PropTypes.string,
    events: PropTypes.array,
    style: PropTypes.object,
    opts: PropTypes.object,
    maps: PropTypes.object,
    funs: PropTypes.object,
    fun_keys: PropTypes.array,
    fun_values: PropTypes.array,
    fun_paths: PropTypes.object,
    fun_effects: PropTypes.array,
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};


export default DashECharts;