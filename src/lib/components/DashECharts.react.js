import React, {Component,useState, useEffect} from 'react';
import PropTypes from 'prop-types';
import ReactECharts from 'echarts-for-react';
import {pick, clone, last} from 'ramda';

function DashECharts(props)  {
    const {
        n_clicks, n_clicks_timestamp, 
        n_clicks_data, selected_data, brush_data, 
        events, option, 
        not_merge, lazy_update, theme,
        style, opts,
        id, setProps
    } = props;
    
    
    function clickHandler(e) {
        setProps({
            n_clicks: n_clicks + 1,
            n_clicks_timestamp: Date.now(),
            n_clicks_data: pick([
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
            selected_data: pick([
                'escapeConnect', 
                'fromAction', 'fromActionPayload', 'isFromClick',
                'selected', 'type'
                ], e)
          });
    }
    
    function brushEndHandler(e) {
        setProps({
            brush_data: pick([
                'areas', 'brushId', 'type'
            ], e)
        });
    }
    
    function eventsHandlers(events) {
        let eventsDict = {
            'click': clickHandler,
            'selectchanged': selectChangedHandler,
            'brushEnd': brushEndHandler,
        }
        return pick(events, eventsDict)
    }
    return (
        <ReactECharts
            id={id}
            option={option}
            notMerge={not_merge}
            lazyUpdate={lazy_update}
            theme={theme}
            onEvents={eventsHandlers(events)}
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