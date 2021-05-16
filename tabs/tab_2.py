import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_2_layout = html.Div([
    html.H1('Supply Chain Inputs'),
    html.Div([
        html.Div([
            html.H6('Select a production rate:'),
            dcc.RadioItems(
                id='page-2-radios',
                options=[{'label': i, 'value': i} for i in ['10 TPD', '50 TPD', '100 TPD']],
                value='Orange',
                style = dict(
                    width = '70%',
                    display = 'inline-block',
                    verticalAlign = "middle"
                    ),
            ),
        ], className='eight columns'),
        html.Div([
            html.H6(id='page-2-content')
        ], className='twelve columns'),
    ], className='twelve columns'),
], className='twelve columns')
