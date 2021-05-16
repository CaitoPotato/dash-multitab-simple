import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_1_layout = html.Div([
    html.H1('Page 1'),
    html.Div([
        html.Div([
            html.H6('Select one:'),
            dcc.Dropdown(
                id='page-1-dropdown',
                options=[{'label': i, 'value': i} for i in ['Solar PV', 'Onshore Wind', 'CCGT w/CCS']],
                value='Electricity Generation',
                style = dict(
                            width = '70%',
                            display = 'inline-block',
                            verticalAlign = "middle"
                            ),
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='Choose an electricity generation method')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')
