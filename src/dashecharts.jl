
module DashEcharts
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.8"

include("dashecharts.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_echarts",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_echarts.min.js",
    external_url = "https://unpkg.com/dash_echarts@0.0.8/dash_echarts/dash_echarts.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_echarts.min.js.map",
    external_url = "https://unpkg.com/dash_echarts@0.0.8/dash_echarts/dash_echarts.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
