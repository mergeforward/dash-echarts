import React, {useLayoutEffect, useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import * as gl from 'echarts-gl';
import * as echarts from 'echarts';
import * as ramda from 'ramda';
import * as ecStat from 'echarts-stat';
import bmap from 'echarts/extension/bmap/bmap';
import 'mapbox-gl/dist/mapbox-gl.css';
import mapboxgl from 'mapbox-gl';


const getCircularReplacer = () => {
  const seen = new WeakSet();
  return (key, value) => {
    if (typeof value === "object" && value !== null) {
      if (seen.has(value)) {
        return;
      }
      seen.add(value);
    }
    return value;
  };
};

const safeObj = (e) => {
    return JSON.parse(JSON.stringify(e, getCircularReplacer()));
}

const loadFuns = (obj) => {
    Object.keys(obj).forEach(key => {
        if (typeof obj[key] === 'string' && !['chart','echarts', 'bmap', 'ramda', 'gl', 'ecStat', 'mapboxgl'].includes(key)) {
            const fun = new Function("return "+obj[key].trim()+".bind(this)").bind(obj)
            obj[key] = fun();
        }
    })
}

function DashECharts(props)  {
    const {
        // eslint-disable-next-line no-unused-vars
        n_clicks, n_clicks_timestamp, click_data,
        selected_data,
        brush_data,
        event,
        option,
        style, id, setProps,
        maps,
        funs, fun_keys, fun_values, fun_paths, fun_effects, fun_prepares,
        mapbox_token, bmap_token,
    } = props;


    // eslint-disable-next-line no-unused-vars
    const [chart, setChart] = useState({});


    const funConvertKeys = (obj) => {
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
    }

    const funConvertValues = (obj) => {
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
    }

    const funConvertPaths = (obj) => {
        if (obj !== null) {
            for (const key of fun_paths) {
                ramda.assocPath(fun_paths[key], funs[key], obj)
            }
        }
    }

    const funPreparesRun = (obj) => {
        for (const key of fun_prepares) {
            funs[key](obj)
        }
    }

    if (!ramda.isEmpty(maps)) {
        const registerMapForEach = (value, key) => {
            // eslint-disable-next-line no-prototype-builtins
            if (value.hasOwnProperty('svg') && typeof value.svg === 'string') {
                const oParser = new DOMParser();
                const oDOM = oParser.parseFromString(value.svg, "image/svg+xml");
                value.svg = oDOM;
            }
            echarts.registerMap(key, value);
        }
        ramda.forEachObjIndexed(registerMapForEach, maps);
    }

    if (!ramda.isEmpty(mapbox_token)) {
        funs.mapboxgl = mapboxgl;
        mapboxgl.accessToken = mapbox_token;
        window.mapboxgl = mapboxgl;
    }

    if (!ramda.isEmpty(bmap_token)) {
        funs.bmap = bmap;
    }

    const chartRef = useRef(null)

    funs.echarts = echarts;
    funs.ramda = ramda;
    funs.gl = gl;
    funs.ecStat = ecStat;
    loadFuns(funs)
    if (!ramda.isEmpty(fun_prepares)) {funPreparesRun(option)}
    if (!ramda.isEmpty(fun_keys)) {funConvertKeys(option)}
    if (!ramda.isEmpty(fun_values)) {funConvertValues(option)}
    if (!ramda.isEmpty(fun_paths)) {funConvertPaths(option)}

    echarts.registerTransform(ecStat.transform.regression);
    echarts.registerTransform(ecStat.transform.histogram);
    echarts.registerTransform(ecStat.transform.clustering);

    useEffect(() => {
        const myChart = echarts.init(chartRef.current)
        setChart(myChart)

        funs.chart = myChart;
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

        if (!ramda.isEmpty(fun_effects)) {
            fun_effects.forEach(e => {
                if (typeof e === 'string') {
                    funs[e]()
                } else {
                    funs[e.name](e.option)
                }
            })
        }
    }, []);

    window.onresize = function() {
        if (!ramda.isEmpty(chart)) {
            chart.resize();
        }
    };

    useEffect(() => {
        if (!ramda.isEmpty(chart)) {
            chart.setOption(option)
        }
    }, [option, chart])

    return (
        <div id={id} style={style} ref={chartRef}/>
    );
}

DashECharts.defaultProps = {
    n_clicks: 0,
    n_clicks_timestamp: -1,
    click_data: {},
    selected_data: {},
    brush_data: {},
    style: {},
    option: {},
    maps: {},
    fun_keys: [],
    fun_values: [],
    fun_paths: {},
    fun_effects: [],
    fun_prepares: [],
    funs: {},
    mapbox_token: null,
    bmap_token: null,
};

DashECharts.propTypes = {
    n_clicks: PropTypes.number,
    n_clicks_timestamp: PropTypes.number,
    click_data: PropTypes.object,
    selected_data: PropTypes.object,
    brush_data: PropTypes.object,
    style: PropTypes.object,
    event: PropTypes.object,
    option: PropTypes.object,
    maps: PropTypes.object,
    funs: PropTypes.object,
    fun_keys: PropTypes.array,
    fun_values: PropTypes.array,
    fun_paths: PropTypes.object,
    fun_effects: PropTypes.array,
    fun_prepares: PropTypes.array,
    mapbox_token: PropTypes.string,
    bmap_token: PropTypes.string,
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