from dash import dcc
import plotly.express as px

def create_sample_graph(df):
    fig = px.bar(df, x="Year", y="Matematicas", title="Sample Bar Chart from Excel")
    return dcc.Graph(id="example-graph", figure=fig)

def create_subject_chart(df):
    fig = px.line(df, x="Year", y="Matematicas", title="Subject Chart Placeholder")
    return dcc.Graph(id="subject-chart", figure=fig)
