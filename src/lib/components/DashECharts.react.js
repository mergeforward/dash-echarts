import React, {Component,useState, useEffect} from 'react';
import PropTypes from 'prop-types';
import ReactECharts from 'echarts-for-react';
import {pick, clone, last} from 'ramda';


function DashECharts(props)  {
    const {
        n_clicks, n_clicks_timestamp, 
        n_clicks_data, selected_data, brush_data, 
        option, not_merge, lazy_update, theme,
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

    const eventsDict = {
        'click': clickHandler,
        'selectchanged': selectChangedHandler,
        'brushEnd': brushEndHandler,
    }
    return (

        <div id={id}>
            <h1>Dash Echarts Integration Demo</h1>
            <ReactECharts
                option={option}
                notMerge={not_merge}
                lazyUpdate={lazy_update}
                theme={theme}
                onEvents={eventsDict}
            />
        </div>
    );
}

DashECharts.defaultProps = {
    theme: 'vintage',
    n_clicks: 0,
    n_clicks_timestamp: -1,
    n_clicks_data: {},
    selected_data: {},
    brush_data: {},
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