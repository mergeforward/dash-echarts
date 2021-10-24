import random
import dash_html_components as html
import dash_echarts
from datetime import datetime
import dash, sys
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


def main():
    '''
    dash_echarts examples
    name: air with echarts
    author: dameng <pingf0@gmail.com>
    '''
    external_scripts = [
        # f'https://webapi.amap.com/maps?v=1.4.15&key={sys.argv[1]}&plugin=Map3D,AMap.Driving',
        f'https://webapi.amap.com/maps?v=1.4.15&key={sys.argv[1]}&plugin=AMap.Map3D,AMap.Driving,AMap.TruckDriving',
        "https://a.amap.com/jsapi_demos/static/demo-center/model/js/three.js",
        "https://a.amap.com/jsapi_demos/static/demo-center/model/js/loaders/MTLLoader.js",
        "https://a.amap.com/jsapi_demos/static/demo-center/model/js/loaders/LoaderSupport.js",
        "https://a.amap.com/jsapi_demos/static/demo-center/model/js/loaders/OBJLoader2.js",

    ]
    app = dash.Dash(__name__,
        external_scripts=external_scripts
    )
    data = [
        [113.625328, 34.746611, 12600574],  # 郑州
        [121.4737021, 31.2303904, 24870895],  # 上海
        [116.3474879, 39.9432725, 21893095],  # 北京
        [116.625328, 34.746611, 12600574],  # 郑州
        [124.4737021, 31.2303904, 24870895],  # 上海
        [111.3474879, 39.9432725, 21893095],  # 北京
    ]

    def convert(e):
        e[2] /= 10000
        return e

    def get_data():
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        # print(a, b, '<<<<<<<<<<<<')
        # if data[a][0] == data[b][0] and data[a][1] == data[b][1]:
        #     b = random.randint(0, 5)
        r = [convert(data[a]), convert(data[b])]
        print(r, '???')
        return r

    option = {
          'amap': {

              'viewMode': '3D',
              'center': [116.472605, 39.992075],
              'resizeEnable': True,
              'mapStyle': 'amap://styles/light',
              'renderOnMoving': True,
              'echartsLayerInteractive': True,
              'largeMode': True,
              'zoom': 10,
              'showBuildingBlock': False,

            # 'viewMode': '3D',
            # # 'center': [116.472605, 39.992075],
            #   'center': [16.397428, 39.90923],
            # 'resizeEnable': True,
            # 'mapStyle': 'amap://styles/light',
            # 'renderOnMoving': True,
            # 'echartsLayerInteractive': True,
            # 'largeMode': True,
            # 'zoom': 17,
            # 'pitch': 55,
            # # 'rotation': -15,
            # 'showBuildingBlock': False,
          },
          'series': [
            {
                'type': 'scatter',
                'coordinateSystem': 'amap',
                'symbolSize': 'div10',
                'data': get_data(),
                'encode': {
                  # encode the third element of data item as the `value` dimension
                  'value': 2
                }
            },
        ]
          # 'series': [
          #   {
          #     'type': 'scatter3D',
          #     'coordinateSystem': 'amap',
          #     'data': [[120, 30, 8], [120.1, 30.2, 20]],
          #     'encode': {
          #       # encode the third element of data item as the `value` dimension
          #       'value': 2
          #     }
          #   }
          # ]
        }

    app.layout = html.Div([
        dash_echarts.DashECharts(
            option = option,
            id='echarts',

            fun_values= ["div10", "init"],
            fun_loaded= ["init"],
            funs= {
                'div10': '''
                function(val) {
                    return val[2] / 10;
                }
                ''',
                'init': '''
function init() {
    console.log('---------->1', this.chart);
    console.log('---------->2', this.amap);
    var d = this.chart.getOption().series[0].data;
    console.log(d);
    var amapComponent = this.chart.getModel().getComponent('amap');
    // Get the instance of AMap
    var map = amapComponent.getAMap();
            var loadModel = function () {
                var modelName = 'building';
                var scope = this;
                var objLoader = new THREE.OBJLoader2();
                var callbackOnLoad = function ( event ) {
                    var object3Dlayer = new AMap.Object3DLayer();
                    var meshes = event.detail.loaderRootNode.children;
                    for(var i=0;i<meshes.length;i++){
                        var vecticesF3 = meshes[i].geometry.attributes.position;
                        var vecticesNormal3 = meshes[i].geometry.attributes.normal;
                        var vecticesUV2 = meshes[i].geometry.attributes.uv;
                        
                        var vectexCount =  vecticesF3.count;

                        mesh = new AMap.Object3D.MeshAcceptLights();

                        var geometry = mesh.geometry;
                    
                        //底部一圈
                        // debugger

                        var c,opacity;

                        var material = meshes[i].material[0]||meshes[i].material;
                        // debugger
                        if(material.map)
                        mesh.textures.push('https://a.amap.com/jsapi_demos/static/demo-center/model/1519/1519.bmp')
                        
                        c = material.color;
                        opacity = material.opacity
                        
                        // debugger
                        for(var j=0;j<vectexCount;j+=1){
                            var s = j*3;
                            geometry.vertices.push(vecticesF3.array[s],vecticesF3.array[s+2],-vecticesF3.array[s+1]);
                        
                            if(vecticesNormal3) {
                                geometry.vertexNormals.push(vecticesNormal3.array[s],vecticesNormal3.array[s+2],-vecticesNormal3.array[s+1]);
                            }
                            if(vecticesUV2) {
                                geometry.vertexUVs.push(vecticesUV2.array[j*2],1-vecticesUV2.array[j*2+1]);
                            }
                            geometry.vertexColors.push(c.r,c.g,c.b,opacity)
                        }
                        // debugger
                        mesh.DEPTH_TEST = material.depthTest
                        // mesh.backOrFront = 'both'
                        mesh.transparent = opacity<1;
                        mesh.scale(6,6,6)
                        mesh.rotateZ(-48)
                        mesh.position(new AMap.LngLat(116.472605,39.992075))
                        object3Dlayer.add(mesh)
                    }
                    map.add(object3Dlayer)
                };

                var onLoadMtl = function ( materials ) {
                    // for(var i=0;i<materials.length;i+=1){
                    // 	materials[i].side=2;
                    // }
                    objLoader.setModelName( modelName );
                    objLoader.setMaterials( materials );
                    objLoader.load( 'https://a.amap.com/jsapi_demos/static/demo-center/model/1519/1519.obj', callbackOnLoad, null, null, null, false );
                };
                objLoader.loadMtl( 'https://a.amap.com/jsapi_demos/static/demo-center/model/1519/1519.mtl', null, onLoadMtl );
            };
            loadModel()
            console.log(AMap, '<<<<');
            console.log(Object.getOwnPropertyNames(AMap), '????');
    if (this.driving) {}
    else {
        this.driving = new AMap.Driving({
            map: map,
            panel: "panel"
        }); 
    }
    
    console.log(Object.getOwnPropertyNames(AMap));
    this.driving.search(new AMap.LngLat(116.379028, 39.865042), new AMap.LngLat(116.427281, 39.903719), function(status, result) {
        // result 即是对应的驾车导航信息，相关数据结构文档请参考  https://lbs.amap.com/api/javascript-api/reference/route-search#m_DrivingResult
        if (status === 'complete') {
            log.success('绘制驾车路线完成')
        } else {
            log.error('获取驾车数据失败：' + result)
        }
    });
    
}
                ''',
            },
            style={
                "width": '100vw',
                "height": '100vh',
            }
        ),
        html.Div(id='panel'),
        dcc.Interval(id="interval", interval=5* 1000, n_intervals=0),
    ])
    # @app.callback(
    #     Output('echarts', 'option'),
    #     [Input('interval', 'n_intervals')],
    #     [State('echarts', 'option')]
    # )
    # def update_echarts(n_intervals, option):
    #     option['series'][0]['data'] = get_data()
    #     return option
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
