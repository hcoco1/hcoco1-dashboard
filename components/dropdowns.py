from dash import dcc, html
import dash_bootstrap_components as dbc

def create_student_dropdown(df, default_value=None):
    students = df['Name'].unique()
    return dbc.Card(
        dbc.CardBody([
            html.Label("Student"),
            dcc.Dropdown(
                id='student-dropdown',
                options=[{'label': student, 'value': student} for student in students],
                value='John Doe',  # Set default value here
                placeholder="Select a Student",
            )
        ]),
        className='Student-Dropdown card'
    )

def create_grade_dropdown(df):
    grades = df['Year'].unique()
    return dbc.Card(
        dbc.CardBody([
            html.Label("Grade"),
            dcc.Dropdown(
                id='grade-dropdown',
                options=[{'label': grade, 'value': grade} for grade in grades],
                placeholder="Select a Grade",
                value='K',  # Set default value here
            )
        ]),
        className='Grade-dropdown card'
    )

# Static dropdowns remain unchanged
language_dropdown = dbc.Card(
    dbc.CardBody([
        html.Label("Language"),
        dcc.Dropdown(
            id='language-dropdown',
            options=[
                {'label': 'English', 'value': 'EN'},
                {'label': 'French', 'value': 'FR'}
            ],
            placeholder="Select a Language",
        )
    ]),
    className='Language-Dropdown card'
)

subject_dropdown = dbc.Card(
    dbc.CardBody([
        html.Label("Subject"),
        dcc.Dropdown(
            options=[
                {'label': 'Math', 'value': 'Math'},
                {'label': 'Science', 'value': 'Science'}
            ],
            placeholder="Select a Subject",
        )
    ]),
    className='Subjects-Dropdown card'
)
