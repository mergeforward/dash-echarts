import json
import os
from setuptools import setup


with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

author, email = package['author'].split(' ')
setup(
    name=package_name,
    version=package["version"],
    author=author,
    author_email=email,
    packages=[package_name,
              f'{package_name}.examples',
              f'{package_name}.examples.gallery',
              f'{package_name}.examples.static',
              ],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    install_requires=['dash'],
    extras_require={
        'play': ['dash-bootstrap-components', 'dash_tabulator', 'dash_extensions']
    },
    classifiers = [
        'Framework :: Dash',
    ],    
    entry_points={
        'console_scripts': [
            'echarts_play=dash_echarts.examples.play:main',
            'echarts_line=dash_echarts.examples.line:main',
            'echarts_bar=dash_echarts.examples.bar:main',
            'echarts_heat=dash_echarts.examples.heat:main',
            'echarts_scatter3d=dash_echarts.examples.scatter3d:main',
            'echarts_map=dash_echarts.examples.map:main',
            'echarts_histbar=dash_echarts.examples.hist_bar:main',
            'echarts_regression=dash_echarts.examples.hist_regression:main',
            'echarts_customprofit=dash_echarts.examples.custom_profit:main',
            'echarts_air=dash_echarts.examples.air:main',
            'echarts_line_race=dash_echarts.examples.line_race:main',
            'echarts_bar_race=dash_echarts.examples.bar_race:main',
            'echarts_bar_style=dash_echarts.examples.bar_style:main',
        ]
    },
)
