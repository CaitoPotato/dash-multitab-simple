import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_1_layout = html.Div([
    html.H1('Supply Chain Inputs'),
    html.Div([
        html.Div([
            html.H6('Choose an electricity generation method:'),
            dcc.Dropdown(
                id='page-1-dropdown',
                options=[{'label': i, 'value': i} for i in ['Solar PV', 'Onshore Wind', 'CCGT w/CCS']],
                value='Solar PV',
                style = dict(
                            width = '70%',
                            display = 'inline-block',
                            verticalAlign = "middle"
                            ),
            ),
        ], className='eight columns'),
        html.Div([
            html.H6(id='page-1-content')
        ], className='twelve columns'),
    ], className='twelve columns'),
], className='twelve columns')
