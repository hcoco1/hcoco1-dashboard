from dash import dash_table

def create_summary_table():
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
        data=[],
        page_size=10,
    )

def subject_table():
    # Placeholder function, you can customize this further based on your needs
    return dash_table.DataTable(
        id='subject-table',
        columns=[{"name": "Subject", "id": "subject"}],
        data=[],
        page_size=10,
    )
