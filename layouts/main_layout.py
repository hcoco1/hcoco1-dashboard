from dash import html
import dash_bootstrap_components as dbc
from components import dropdowns, graphs, tables

def create_layout(df):
    return html.Div(
        className='container',
        children=[
            dbc.Card(
                dbc.CardBody(html.H1("Student Performance Dashboard")),
                className='Title card'
            ),
            dbc.Card(
                dbc.CardBody(html.Div("Average Grade Placeholder")),
                className='Average-Grade card'
            ),
            html.Div(
                className='DropdownMenus',
                children=[
                    dropdowns.language_dropdown,
                    dropdowns.create_student_dropdown(df, default_value='John Doe'),
                    dropdowns.create_grade_dropdown(df)
                ]
            ),
            dbc.Card(
                dbc.CardBody(html.Img(src='https://via.placeholder.com/300', className='Image', style={'width': '100%', 'height': 'auto'})),
                className='Image card'
            ),
            dbc.Card(
                dbc.CardBody(tables.create_summary_table()),
                className='Summary-Table card'
            ),
            dbc.Card(
                dbc.CardBody(
                    graphs.create_sample_graph(df)
                ),
                className='Summary-Chart card'
            ),
            html.Div(
                className='Subjects',
                children=[
                    dropdowns.subject_dropdown,
                    tables.subject_table(),
                    graphs.create_subject_chart(df)
                ]
            )
        ]
    )
