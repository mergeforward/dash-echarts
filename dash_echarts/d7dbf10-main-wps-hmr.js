webpackHotUpdatedash_echarts("main",{

/***/ "./src/lib/components/DashECharts.react.js":
/*!*************************************************!*\
  !*** ./src/lib/components/DashECharts.react.js ***!
  \*************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "./node_modules/react/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! prop-types */ "./node_modules/prop-types/index.js");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var echarts_gl__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! echarts-gl */ "./node_modules/echarts-gl/index.js");
/* harmony import */ var echarts__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! echarts */ "./node_modules/echarts/index.js");
/* harmony import */ var ramda__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ramda */ "./node_modules/ramda/es/index.js");
/* harmony import */ var echarts_stat__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! echarts-stat */ "./node_modules/echarts-stat/index.js");
/* harmony import */ var echarts_stat__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(echarts_stat__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var echarts_extension_bmap_bmap__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! echarts/extension/bmap/bmap */ "./node_modules/echarts/extension/bmap/bmap.js");
function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest(); }

function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

function _iterableToArrayLimit(arr, i) { if (typeof Symbol === "undefined" || !(Symbol.iterator in Object(arr))) return; var _arr = []; var _n = true; var _d = false; var _e = undefined; try { for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }

function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }









var loadFuns = function loadFuns(obj) {
  Object.keys(obj).forEach(function (key) {
    if (typeof obj[key] === 'string' && !['chart', 'echarts', 'bmap', 'ramda', 'gl', 'ecStat'].includes(key)) {
      var fun = new Function("return " + obj[key].trim() + ".bind(this)").bind(obj);
      obj[key] = fun();
    }
  });
};

function DashECharts(props) {
  var n_clicks = props.n_clicks,
      n_clicks_timestamp = props.n_clicks_timestamp,
      n_clicks_data = props.n_clicks_data,
      selected_data = props.selected_data,
      brush_data = props.brush_data,
      option = props.option,
      style = props.style,
      id = props.id,
      setProps = props.setProps;

  var _useState = Object(react__WEBPACK_IMPORTED_MODULE_0__["useState"])({}),
      _useState2 = _slicedToArray(_useState, 2),
      chart = _useState2[0],
      setChart = _useState2[1];

  var chartRef = Object(react__WEBPACK_IMPORTED_MODULE_0__["useRef"])(null);
  Object(react__WEBPACK_IMPORTED_MODULE_0__["useEffect"])(function () {
    // let chart = echarts.init(myChart);
    // chart.setOption(option);
    var myChart = echarts__WEBPACK_IMPORTED_MODULE_3__["init"](chartRef.current);
    myChart.setOption(option);
    setChart(myChart);
    console.log('console');
    myChart.on("click", function (e) {
      setProps({
        n_clicks: n_clicks + 1,
        n_clicks_timestamp: Date.now(),
        n_clicks_data: ramda__WEBPACK_IMPORTED_MODULE_4__["pick"](['componentType', 'seriesType', 'seriesIndex', 'seriesName', 'name', 'dataIndex', 'data', 'dataType', 'value', 'color'], e)
      });
    });
    myChart.on("selectchanged", function (e) {
      setProps({
        selected_data: ramda__WEBPACK_IMPORTED_MODULE_4__["pick"](['escapeConnect', 'fromAction', 'fromActionPayload', 'isFromClick', 'selected', 'type'], e)
      });
    });
    myChart.on("brushEnd", function (e) {
      setProps({
        brush_data: ramda__WEBPACK_IMPORTED_MODULE_4__["pick"](['areas', 'brushId', 'type'], e)
      });
    });

    window.onresize = function () {
      window.resize();
    };
  }, [option]);
  return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
    id: id,
    style: style,
    ref: chartRef
  });
}

DashECharts.defaultProps = {
  n_clicks: 0,
  n_clicks_timestamp: -1,
  n_clicks_data: {},
  selected_data: {},
  brush_data: {},
  style: {},
  option: {}
};
DashECharts.propTypes = {
  n_clicks: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.number,
  n_clicks_timestamp: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.number,
  n_clicks_data: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.object,
  selected_data: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.object,
  brush_data: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.object,
  style: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.object,
  option: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.object,

  /**
   * The ID used to identify this component in Dash callbacks.
   */
  id: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.string,

  /**
   * Dash-assigned callback that should be called to report property changes
   * to Dash, to make them available for callbacks.
   */
  setProps: prop_types__WEBPACK_IMPORTED_MODULE_1___default.a.func
};
/* harmony default export */ __webpack_exports__["default"] = (DashECharts);

/***/ })

})
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9kYXNoX2VjaGFydHMvLi9zcmMvbGliL2NvbXBvbmVudHMvRGFzaEVDaGFydHMucmVhY3QuanMiXSwibmFtZXMiOlsibG9hZEZ1bnMiLCJvYmoiLCJPYmplY3QiLCJrZXlzIiwiZm9yRWFjaCIsImtleSIsImluY2x1ZGVzIiwiZnVuIiwiRnVuY3Rpb24iLCJ0cmltIiwiYmluZCIsIkRhc2hFQ2hhcnRzIiwicHJvcHMiLCJuX2NsaWNrcyIsIm5fY2xpY2tzX3RpbWVzdGFtcCIsIm5fY2xpY2tzX2RhdGEiLCJzZWxlY3RlZF9kYXRhIiwiYnJ1c2hfZGF0YSIsIm9wdGlvbiIsInN0eWxlIiwiaWQiLCJzZXRQcm9wcyIsInVzZVN0YXRlIiwiY2hhcnQiLCJzZXRDaGFydCIsImNoYXJ0UmVmIiwidXNlUmVmIiwidXNlRWZmZWN0IiwibXlDaGFydCIsImVjaGFydHMiLCJjdXJyZW50Iiwic2V0T3B0aW9uIiwiY29uc29sZSIsImxvZyIsIm9uIiwiZSIsIkRhdGUiLCJub3ciLCJyYW1kYSIsIndpbmRvdyIsIm9ucmVzaXplIiwicmVzaXplIiwiZGVmYXVsdFByb3BzIiwicHJvcFR5cGVzIiwiUHJvcFR5cGVzIiwibnVtYmVyIiwib2JqZWN0Iiwic3RyaW5nIiwiZnVuYyJdLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBR0EsSUFBTUEsUUFBUSxHQUFHLFNBQVhBLFFBQVcsQ0FBQ0MsR0FBRCxFQUFTO0FBQ3RCQyxRQUFNLENBQUNDLElBQVAsQ0FBWUYsR0FBWixFQUFpQkcsT0FBakIsQ0FBeUIsVUFBQUMsR0FBRyxFQUFJO0FBQzVCLFFBQUksT0FBT0osR0FBRyxDQUFDSSxHQUFELENBQVYsS0FBb0IsUUFBcEIsSUFBZ0MsQ0FBQyxDQUFDLE9BQUQsRUFBUyxTQUFULEVBQW9CLE1BQXBCLEVBQTRCLE9BQTVCLEVBQXFDLElBQXJDLEVBQTJDLFFB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O0FBQWEsU0FBSyxFQUFFRCxLQUFwQjtBQUEyQixPQUFHLEVBQUVNO0FBQWhDLElBREo7QUFHSDs7QUFFRGQsV0FBVyxDQUFDK0IsWUFBWixHQUEyQjtBQUN2QjdCLFVBQVEsRUFBRSxDQURhO0FBRXZCQyxvQkFBa0IsRUFBRSxDQUFDLENBRkU7QUFHdkJDLGVBQWEsRUFBRSxFQUhRO0FBSXZCQyxlQUFhLEVBQUUsRUFKUTtBQUt2QkMsWUFBVSxFQUFFLEVBTFc7QUFNdkJFLE9BQUssRUFBRSxFQU5nQjtBQU92QkQsUUFBTSxFQUFFO0FBUGUsQ0FBM0I7QUFVQVAsV0FBVyxDQUFDZ0MsU0FBWixHQUF3QjtBQUNwQjlCLFVBQVEsRUFBRStCLGlEQUFTLENBQUNDLE1BREE7QUFFcEIvQixvQkFBa0IsRUFBRThCLGlEQUFTLENBQUNDLE1BRlY7QUFHcEI5QixlQUFhLEVBQUU2QixpREFBUyxDQUFDRSxNQUhMO0FBSXBCOUIsZUFBYSxFQUFFNEIsaURBQVMsQ0FBQ0UsTUFKTDtBQUtwQjdCLFlBQVUsRUFBRTJCLGlEQUFTLENBQUNFLE1BTEY7QUFNcEIzQixPQUFLLEVBQUV5QixpREFBUyxDQUFDRSxNQU5HO0FBT3BCNUIsUUFBTSxFQUFFMEIsaURBQVMsQ0FBQ0UsTUFQRTs7QUFRcEI7QUFDSjtBQUNBO0FBQ0kxQixJQUFFLEVBQUV3QixpREFBUyxDQUFDRyxNQVhNOztBQVlwQjtBQUNKO0FBQ0E7QUFDQTtBQUNJMUIsVUFBUSxFQUFFdUIsaURBQVMsQ0FBQ0k7QUFoQkEsQ0FBeEI7QUFvQmVyQywwRUFBZixFIiwiZmlsZSI6ImQ3ZGJmMTAtbWFpbi13cHMtaG1yLmpzIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IFJlYWN0LCB7dXNlRWZmZWN0LCB1c2VSZWYsIHVzZVN0YXRlfSBmcm9tICdyZWFjdCc7XG5pbXBvcnQgUHJvcFR5cGVzIGZyb20gJ3Byb3AtdHlwZXMnO1xuaW1wb3J0ICogYXMgZ2wgZnJvbSAnZWNoYXJ0cy1nbCc7XG5pbXBvcnQgKiBhcyBlY2hhcnRzIGZyb20gJ2VjaGFydHMnO1xuaW1wb3J0ICogYXMgcmFtZGEgZnJvbSAncmFtZGEnO1xuaW1wb3J0ICogYXMgZWNTdGF0IGZyb20gJ2VjaGFydHMtc3RhdCc7XG5pbXBvcnQgYm1hcCBmcm9tICdlY2hhcnRzL2V4dGVuc2lvbi9ibWFwL2JtYXAnO1xuXG5cbmNvbnN0IGxvYWRGdW5zID0gKG9iaikgPT4ge1xuICAgIE9iamVjdC5rZXlzKG9iaikuZm9yRWFjaChrZXkgPT4ge1xuICAgICAgICBpZiAodHlwZW9mIG9ialtrZXldID09PSAnc3RyaW5nJyAmJiAhWydjaGFydCcsJ2VjaGFydHMnLCAnYm1hcCcsICdyYW1kYScsICdnbCcsICdlY1N0YXQnXS5pbmNsdWRlcyhrZXkpKSB7XG4gICAgICAgICAgICBjb25zdCBmdW4gPSBuZXcgRnVuY3Rpb24oXCJyZXR1cm4gXCIrb2JqW2tleV0udHJpbSgpK1wiLmJpbmQodGhpcylcIikuYmluZChvYmopXG4gICAgICAgICAgICBvYmpba2V5XSA9IGZ1bigpO1xuICAgICAgICB9XG4gICAgfSlcbn1cblxuZnVuY3Rpb24gRGFzaEVDaGFydHMocHJvcHMpICB7XG5cblxuICAgIGNvbnN0IHtcbiAgICAgICAgbl9jbGlja3MsIG5fY2xpY2tzX3RpbWVzdGFtcCxcbiAgICAgICAgbl9jbGlja3NfZGF0YSwgc2VsZWN0ZWRfZGF0YSwgYnJ1c2hfZGF0YSxcbiAgICAgICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIG5vLXVudXNlZC12YXJzXG4gICAgICAgIG9wdGlvbixcbiAgICAgICAgc3R5bGUsIGlkLCBzZXRQcm9wc1xuICAgIH0gPSBwcm9wcztcblxuICAgIGNvbnN0IFtjaGFydCwgc2V0Q2hhcnRdID0gdXNlU3RhdGUoe30pO1xuXG4gICAgY29uc3QgY2hhcnRSZWYgPSB1c2VSZWYobnVsbClcblxuXG4gICAgdXNlRWZmZWN0KCgpID0+IHtcbiAgICAgICAgLy8gbGV0IGNoYXJ0ID0gZWNoYXJ0cy5pbml0KG15Q2hhcnQpO1xuICAgICAgICAvLyBjaGFydC5zZXRPcHRpb24ob3B0aW9uKTtcbiAgICAgICAgY29uc3QgbXlDaGFydCA9IGVjaGFydHMuaW5pdChjaGFydFJlZi5jdXJyZW50KVxuICAgICAgICBteUNoYXJ0LnNldE9wdGlvbihvcHRpb24pXG4gICAgICAgIHNldENoYXJ0KG15Q2hhcnQpXG4gICAgICAgIGNvbnNvbGUubG9nKCdjb25zb2xlJylcbiAgICAgICAgbXlDaGFydC5vbihcImNsaWNrXCIsIGUgPT4ge1xuICAgICAgICAgICAgc2V0UHJvcHMoe1xuICAgICAgICAgICAgICAgIG5fY2xpY2tzOiBuX2NsaWNrcyArIDEsXG4gICAgICAgICAgICAgICAgbl9jbGlja3NfdGltZXN0YW1wOiBEYXRlLm5vdygpLFxuICAgICAgICAgICAgICAgIG5fY2xpY2tzX2RhdGE6IHJhbWRhLnBpY2soW1xuICAgICAgICAgICAgICAgICAgICAnY29tcG9uZW50VHlwZScsXG4gICAgICAgICAgICAgICAgICAgICdzZXJpZXNUeXBlJywgJ3Nlcmllc0luZGV4JywgJ3Nlcmllc05hbWUnLFxuICAgICAgICAgICAgICAgICAgICAnbmFtZScsXG4gICAgICAgICAgICAgICAgICAgICdkYXRhSW5kZXgnLCAnZGF0YScsICdkYXRhVHlwZScsXG4gICAgICAgICAgICAgICAgICAgICd2YWx1ZScsICdjb2xvcicsXG4gICAgICAgICAgICAgICAgICAgIF0sIGUpXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgfSk7XG4gICAgICAgIG15Q2hhcnQub24oXCJzZWxlY3RjaGFuZ2VkXCIsIGUgPT4ge1xuICAgICAgICAgICAgc2V0UHJvcHMoe1xuICAgICAgICAgICAgICAgIHNlbGVjdGVkX2RhdGE6IHJhbWRhLnBpY2soW1xuICAgICAgICAgICAgICAgICAgICAnZXNjYXBlQ29ubmVjdCcsXG4gICAgICAgICAgICAgICAgICAgICdmcm9tQWN0aW9uJywgJ2Zyb21BY3Rpb25QYXlsb2FkJywgJ2lzRnJvbUNsaWNrJyxcbiAgICAgICAgICAgICAgICAgICAgJ3NlbGVjdGVkJywgJ3R5cGUnXG4gICAgICAgICAgICAgICAgXSwgZSlcbiAgICAgICAgICAgIH0pO1xuICAgICAgICB9KVxuICAgICAgICBteUNoYXJ0Lm9uKFwiYnJ1c2hFbmRcIiwgZSA9PiB7XG4gICAgICAgICAgICBzZXRQcm9wcyh7XG4gICAgICAgICAgICAgICAgYnJ1c2hfZGF0YTogcmFtZGEucGljayhbXG4gICAgICAgICAgICAgICAgICAgICdhcmVhcycsICdicnVzaElkJywgJ3R5cGUnXG4gICAgICAgICAgICAgICAgXSwgZSlcbiAgICAgICAgICAgIH0pO1xuICAgICAgICB9KVxuICAgICAgICB3aW5kb3cub25yZXNpemUgPSBmdW5jdGlvbigpIHtcbiAgICAgICAgICB3aW5kb3cucmVzaXplKCk7XG4gICAgICAgIH07XG4gICAgfSwgW29wdGlvbl0pO1xuXG5cbiAgICByZXR1cm4gKFxuICAgICAgICA8ZGl2IGlkPXtpZH0gc3R5bGU9e3N0eWxlfSByZWY9e2NoYXJ0UmVmfS8+XG4gICAgKTtcbn1cblxuRGFzaEVDaGFydHMuZGVmYXVsdFByb3BzID0ge1xuICAgIG5fY2xpY2tzOiAwLFxuICAgIG5fY2xpY2tzX3RpbWVzdGFtcDogLTEsXG4gICAgbl9jbGlja3NfZGF0YToge30sXG4gICAgc2VsZWN0ZWRfZGF0YToge30sXG4gICAgYnJ1c2hfZGF0YToge30sXG4gICAgc3R5bGU6IHt9LFxuICAgIG9wdGlvbjoge30sXG59O1xuXG5EYXNoRUNoYXJ0cy5wcm9wVHlwZXMgPSB7XG4gICAgbl9jbGlja3M6IFByb3BUeXBlcy5udW1iZXIsXG4gICAgbl9jbGlja3NfdGltZXN0YW1wOiBQcm9wVHlwZXMubnVtYmVyLFxuICAgIG5fY2xpY2tzX2RhdGE6IFByb3BUeXBlcy5vYmplY3QsXG4gICAgc2VsZWN0ZWRfZGF0YTogUHJvcFR5cGVzLm9iamVjdCxcbiAgICBicnVzaF9kYXRhOiBQcm9wVHlwZXMub2JqZWN0LFxuICAgIHN0eWxlOiBQcm9wVHlwZXMub2JqZWN0LFxuICAgIG9wdGlvbjogUHJvcFR5cGVzLm9iamVjdCxcbiAgICAvKipcbiAgICAgKiBUaGUgSUQgdXNlZCB0byBpZGVudGlmeSB0aGlzIGNvbXBvbmVudCBpbiBEYXNoIGNhbGxiYWNrcy5cbiAgICAgKi9cbiAgICBpZDogUHJvcFR5cGVzLnN0cmluZyxcbiAgICAvKipcbiAgICAgKiBEYXNoLWFzc2lnbmVkIGNhbGxiYWNrIHRoYXQgc2hvdWxkIGJlIGNhbGxlZCB0byByZXBvcnQgcHJvcGVydHkgY2hhbmdlc1xuICAgICAqIHRvIERhc2gsIHRvIG1ha2UgdGhlbSBhdmFpbGFibGUgZm9yIGNhbGxiYWNrcy5cbiAgICAgKi9cbiAgICBzZXRQcm9wczogUHJvcFR5cGVzLmZ1bmNcbn07XG5cblxuZXhwb3J0IGRlZmF1bHQgRGFzaEVDaGFydHM7Il0sInNvdXJjZVJvb3QiOiIifQ==