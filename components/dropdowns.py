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
                value=default_value if default_value else students[0],  # Set default value here
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
                value=grades[0],  # Set default value here
            )
        ]),
        className='Grade-dropdown card'
    )

def create_subject_dropdown():
    subjects = [
        "Matematicas", "Literatura", "English", "Deporte", "Geography",
        "Art", "Biologia", "Orientacion", "Participacion"
    ]
    return dbc.Card(
        dbc.CardBody([
            html.Label("Subject"),
            dcc.Dropdown(
                id='subject-dropdown',
                options=[{'label': subject, 'value': subject} for subject in subjects],
                placeholder="Select a Subject",
                value=subjects[0]  # Set default value here
            )
        ]),
        className='Subject-Dropdown card'
    )

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
            value='EN'  # Set default value here
        )
    ]),
    className='Language-Dropdown card'
)
