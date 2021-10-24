import React, {useCallback, useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import * as gl from 'echarts-gl';
import * as echarts from 'echarts';
import * as ramda from 'ramda';
import * as ecStat from 'echarts-stat';
import bmap from 'echarts/extension/bmap/bmap';
// import 'mapbox-gl/dist/mapbox-gl.css';
import mapboxgl from 'mapbox-gl';
import * as amap from 'echarts-extension-amap';

const loadFuns = (funs, obj) => {
    Object.keys(funs).forEach(key => {
        if (typeof funs[key] === 'string') {
            const fun = new Function("return "+funs[key].trim()+".bind(this)").bind(obj)
            funs[key] = fun();
        }
    })
}


function DashECharts(props)  {
    const {
        // eslint-disable-next-line no-unused-vars
        n_clicks, n_clicks_timestamp, click_data,
        selected_data,
        brush_data,
        axis_data,
        event,
        option,
        style, id, setProps,
        maps,
        funs, fun_keys, fun_values, fun_paths,
        fun_befores, fun_afters, fun_loaded,
        mapbox_token, bmap_token, amap_token,
        resize_id,
        reset_id,
    } = props;

    const g = {};

    // eslint-disable-next-line no-unused-vars
    const [chart, setChart] = useState({});
    const chartRef = useRef(null)

    //obj is the option
    const funConvertKeys = useCallback((obj) => {
        if (obj !== null) {
            Object.keys(obj).forEach(key => {
                const v = obj[key]
                if (typeof v === 'string') {

                    if (fun_keys.includes(key)) {
                        obj[key] = funs[v]
                    }
                } else if (typeof v === 'object') {
                    funConvertKeys(v)
                }
            })
        }
    })

    const funConvertValues = useCallback((obj) => {
        if (obj !== null) {
            Object.keys(obj).forEach(key => {
                const v = obj[key]
                if (!ramda.isEmpty(v)) {
                    if (typeof v === 'string') {
                        if (fun_values.includes(v)) {
                            obj[key] = funs[v]
                        }
                    }
                    else if (typeof v === 'object') {
                        funConvertValues(v)
                    }
                } 
            })
        }
    })

    const funConvertPaths = useCallback((obj) => {
        if (obj !== null) {
            for (const key of fun_paths) {
                ramda.assocPath(fun_paths[key], funs[key], obj)
            }
        }
    })

    const funRun = useCallback((fun_names, funs) => {
        for (const key of fun_names) {
            funs[key]()
        }
    })
    // const funAftersRun = useCallback((obj) => {
    //     for (const key of fun_afters) {
    //         if (typeof key === 'string') {
    //             funs[key]()
    //         } else {
    //             funs[key](obj)
    //         }
    //     }
    // })
    // const funLoadedRun = useCallback((obj) => {
    //     for (const key of fun_loaded) {
    //         if (typeof key === 'string') {
    //             funs[key]()
    //         } else {
    //             funs[key](obj)
    //         }
    //     }
    // })

    const registerMapForEach = useCallback((value, key) => {
        // eslint-disable-next-line no-prototype-builtins
        if (value.hasOwnProperty('svg') && typeof value.svg === 'string') {
            const oParser = new DOMParser();
            const oDOM = oParser.parseFromString(value.svg, "image/svg+xml");
            value.svg = oDOM;
        }
        echarts.registerMap(key, value);
    })

    if (!ramda.isEmpty(maps)) {
        ramda.forEachObjIndexed(registerMapForEach, maps);
    }

    if (!ramda.isEmpty(mapbox_token)) {
        g.mapboxgl = mapboxgl;
        // funs.mapboxgl = mapboxgl;
        mapboxgl.accessToken = mapbox_token;
        window.mapboxgl = mapboxgl;
    }

    if (!ramda.isEmpty(bmap_token)) {
        g.bmap = bmap;
    }

    if (!ramda.isEmpty(amap_token)) {
        g.amap = amap;
    }

    g.echarts = echarts;
    g.ramda = ramda;
    g.gl = gl;
    g.ecStat = ecStat;
    loadFuns(funs, g)
    if (!ramda.isEmpty(fun_befores)) {funRun(fun_befores, funs)}
    if (!ramda.isEmpty(fun_keys)) {funConvertKeys(option)}
    if (!ramda.isEmpty(fun_values)) {funConvertValues(option)}
    if (!ramda.isEmpty(fun_paths)) {funConvertPaths(option)}
    if (!ramda.isEmpty(fun_afters)) {funRun(fun_afters, funs)}

    echarts.registerTransform(ecStat.transform.regression);
    echarts.registerTransform(ecStat.transform.histogram);
    echarts.registerTransform(ecStat.transform.clustering);

    useEffect(() => {

        const myChart = echarts.init(chartRef.current)
        myChart.setOption(option)
        setChart(myChart)

        g.chart = myChart;
        myChart.on("click", e => {
            const ts = Date.now()
            const clickCount = n_clicks + 1
            const data = ramda.pick([
                'componentType',
                'seriesType', 'seriesIndex', 'seriesName',
                'name',
                'dataIndex', 'data', 'dataType',
                'value', 'color',
                ], e)
            data.n_clicks = clickCount;
            data.core_timestamp = ts;
            setProps({
                event: e.event.event,
                n_clicks: clickCount,
                n_clicks_timestamp: ts,
                click_data: data
            });
        });
        myChart.on("selectchanged", e => {
            const ts = Date.now()
            const data = ramda.pick([
                'escapeConnect',
                'fromAction', 'fromActionPayload', 'isFromClick',
                'selected', 'type'
            ], e)
            data.core_timestamp = ts;
            setProps({
                selected_data: data
            });
        })
        myChart.on("brushEnd", e => {
            const ts = Date.now()
            const data = ramda.pick([
                'areas', 'brushId', 'type'
            ], e)
            data.core_timestamp = ts;
            setProps({
                brush_data: data
            });
        })
        myChart.on("updateAxisPointer", e => {
            const ts = Date.now()
            const data = ramda.pick([
                'axisInfo',
                'dataIndex','dataIndexInside', 'seriesIndex',
                'type'
            ], e)
            data.core_timestamp = ts;
            setProps({
                axis_data: data
            });
        })
        funRun(fun_loaded, funs)
    // }, []);
    }, [option]);


    useEffect(() => {
        if (!ramda.isEmpty(chart)) {
            chart.setOption(option)
            const resizeFunc = () => {
                if (!ramda.isEmpty(chart)) {
                    chart.resize();
                    const ts = Date.now()
                    setProps({
                        n_resizes: ts,
                        n_clicks_timestamp: ts,
                    });
                }
            }
            window.addEventListener('resize', resizeFunc);
            return () => {
              window.removeEventListener('resize', resizeFunc)
            }
        }
        return () => {
        }
    }, [option])

    useEffect(() => {
        if (!ramda.isEmpty(chart)) {
            if (resize_id>0) {
                setTimeout(function () {
                    chart.resize()
                }, 500)
            }
        }
    }, [resize_id])

    useEffect(() => {
        if (!ramda.isEmpty(chart)) {
            if (reset_id>0) {
                chart.clear()
                chart.setOption(option)
            }
        }
    }, [reset_id])

    return (
        <div>
            <div id={id} style={style} ref={chartRef}/>
        </div>
    );
}

DashECharts.defaultProps = {
    resize_id: 0,
    reset_id: 0,
    n_clicks: 0,
    n_clicks_timestamp: -1,
    click_data: {},
    selected_data: {},
    brush_data: {},
    axis_data: {},
    style: {},
    option: {},
    maps: {},
    fun_keys: [],
    fun_values: [],
    fun_paths: {},
    fun_befores: [],
    fun_afters: [],
    fun_loaded: [],
    funs: {},
    mapbox_token: null,
    bmap_token: null,
    amap_token: null,
};

DashECharts.propTypes = {
    resize_id: PropTypes.number,
    reset_id: PropTypes.number,
    n_clicks: PropTypes.number,
    n_clicks_timestamp: PropTypes.number,
    click_data: PropTypes.object,
    selected_data: PropTypes.object,
    brush_data: PropTypes.object,
    axis_data: PropTypes.object,
    style: PropTypes.object,
    event: PropTypes.object,
    option: PropTypes.object,
    maps: PropTypes.object,
    funs: PropTypes.object,
    fun_keys: PropTypes.array,
    fun_values: PropTypes.array,
    fun_paths: PropTypes.object,
    fun_befores: PropTypes.array,
    fun_afters: PropTypes.array,
    fun_loaded: PropTypes.array,
    mapbox_token: PropTypes.string,
    bmap_token: PropTypes.string,
    amap_token: PropTypes.string,
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