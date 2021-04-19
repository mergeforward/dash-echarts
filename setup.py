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
    packages=[package_name, f'{package_name}.examples'],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    install_requires=['dash'],
    extras_require={
        'play': ['dash-bootstrap-components']
    },
    classifiers = [
        'Framework :: Dash',
    ],    
    entry_points={
        'console_scripts': [
            'echarts_line=dash_echarts.examples.line:main',
            'echarts_bar=dash_echarts.examples.bar:main',
            'echarts_heat=dash_echarts.examples.heat:main',
            'echarts_scatter3d=dash_echarts.examples.scatter3d:main',
            'echarts_map=dash_echarts.examples.map:main',
            'echarts_histbar=dash_echarts.examples.hist_bar:main',
            'echarts_regression=dash_echarts.examples.hist_regression:main',
            'echarts_customprofit=dash_echarts.examples.custom_profit:main',
            'echarts_air=dash_echarts.examples.air:main',
        ]
    },
)
