from dash import dash_table

def create_summary_table(df):
    return dash_table.DataTable(
        id='summary-table',
        columns=[
            {"name": "Student", "id": "Name"},
            {"name": "Grade", "id": "Year"},
            {"name": "Mathematics", "id": "Matematicas"},
            {"name": "Literature", "id": "Literatura"},
            {"name": "English", "id": "English"},
            {"name": "Sport", "id": "Deporte"},
            {"name": "Geography", "id": "Geography"},
            {"name": "Art", "id": "Art"},
            {"name": "Biology", "id": "Biologia"},
            {"name": "Guidance", "id": "Orientacion"},
            {"name": "Participation", "id": "Participacion"},
            {"name": "Average", "id": "Grade Average"}
        ],
        data=df.to_dict('records'),
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold',
            'textAlign': 'center'
        },
        style_cell={
            'textAlign': 'left',
            'padding': '5px',
            'whiteSpace': 'normal',
            'height': 'auto',
            'textAlign': 'center'
        },
        style_data={
            'color': 'black',
            'backgroundColor': 'white'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ]
    )

def subject_table():
    return dash_table.DataTable(
        id='subject-table',
        columns=[
            {"name": "Subject", "id": "Subject"},
            {"name": "Average Grade", "id": "Average Grade"}
        ],
        data=[],
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold',
            'textAlign': 'center'
        },
        style_cell={
            'textAlign': 'left',
            'padding': '5px',
            'whiteSpace': 'normal',
            'height': 'auto',
            'textAlign': 'center'
        },
        style_data={
            'color': 'black',
            'backgroundColor': 'white',
            'textAlign': 'center'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ]
    )
