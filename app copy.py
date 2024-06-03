import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create some sample data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 30, 40]
})

# Create a Plotly Express bar chart
fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")

# Define the layout of the app
app.layout = html.Div(
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
                dbc.Card(
                    dbc.CardBody([
                        html.Label("Language"),
                        dcc.Dropdown(
                            options=[
                                {'label': 'English', 'value': 'EN'},
                                {'label': 'French', 'value': 'FR'}
                            ],
                            placeholder="Select a Language",
                        )
                    ]),
                    className='Language-Dropdown card'
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.Label("Student"),
                        dcc.Dropdown(
                            options=[
                                {'label': 'Student A', 'value': 'A'},
                                {'label': 'Student B', 'value': 'B'}
                            ],
                            placeholder="Select a Student",
                        )
                    ]),
                    className='Student-Dropdown card'
                ),
                dbc.Card(
                    dbc.CardBody([
                        html.Label("Grade"),
                        dcc.Dropdown(
                            options=[
                                {'label': 'Grade 1', 'value': '1'},
                                {'label': 'Grade 2', 'value': '2'}
                            ],
                            placeholder="Select a Grade",
                        )
                    ]),
                    className='Grade-dropdown card'
                )
            ]
        ),
        dbc.Card(
            dbc.CardBody(html.Img(src='https://via.placeholder.com/300', className='Image', style={'width': '100%', 'height': 'auto'})),
            className='Image card'
        ),
        dbc.Card(
            dbc.CardBody(html.Div("Summary Table Placeholder")),
            className='Summary-Table card'
        ),
        dbc.Card(
            dbc.CardBody(
                dcc.Graph(id="example-graph", figure=fig)
            ),
            className='Summary-Chart card'
        ),
        html.Div(
            className='Subjects',
            children=[
                dbc.Card(
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
                ),
                dbc.Card(
                    dbc.CardBody(html.Div("Subject Table Placeholder")),
                    className='Subject-Table card'
                ),
                dbc.Card(
                    dbc.CardBody(html.Div("Subject Chart Placeholder")),
                    className='Subjects-Chart card'
                )
            ]
        )
    ]
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
