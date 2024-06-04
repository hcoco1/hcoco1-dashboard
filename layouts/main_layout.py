from dash import html, dcc
import dash_bootstrap_components as dbc
from components import dropdowns, tables


def create_layout(df):
    return html.Div(
        className='container',
        children=[
            dbc.Card(
                dbc.CardBody(html.H3("Student Performance Dashboard", style={'text-align': 'center'})),
                className='Title card',
                
                
            ),
            html.Div(
                className='DropdownMenus',
                children=[
                    dropdowns.language_dropdown,
                    dropdowns.create_student_dropdown(df),
                    dropdowns.create_grade_dropdown(df)
                ]
            ),
           dbc.Card(
                dbc.CardBody([
                   
                    html.Img(id='student-image', className='Image', style={'width': '100%',}),
                    html.H6(id='final-average', className='FinalAverage', style={'text-align': 'center'})
                ]),
                className='Image card'
            ),
            dbc.Card(
                dbc.CardBody(tables.create_summary_table(df)),
                className='Summary-Table card'
            ),
            dbc.Card(
                dbc.CardBody(
                    dcc.Graph(id='sample-graph')
                ),
                className='Summary-Chart card'
            ),
          dbc.Card(
                dbc.CardBody(
                    html.Div(
                        className='Subjects',
                        children=[
                            html.Div(dropdowns.create_subject_dropdown(), className='Subjects-Dropdown'),
                            html.Div(tables.create_exam_results_table(), className='Subject-Table'),
                            html.Div(dcc.Graph(id='exam-results-chart'), className='Subjects-Chart')
                        ]
                    )
                ),
                className='Subjects card'
          )
        ]
    )
