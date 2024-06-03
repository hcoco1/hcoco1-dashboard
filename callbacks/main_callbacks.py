from dash.dependencies import Input, Output
import components.graphs as graphs

def register_callbacks(app, df):
    @app.callback(
        Output('grade-dropdown', 'options'),
        [Input('student-dropdown', 'value')]
    )
    def update_grades_dropdown(selected_student):
        filtered_df = df[df['Name'] == selected_student]
        grades = filtered_df['Year'].unique()
        return [{'label': grade, 'value': grade} for grade in grades]

    @app.callback(
        Output('summary-table', 'data'),
        [Input('student-dropdown', 'value'),
         Input('grade-dropdown', 'value')]
    )
    def update_summary_table(selected_student, selected_grade):
        filtered_df = df[(df['Name'] == selected_student) & (df['Year'] == selected_grade)]
        return filtered_df.to_dict('records')

    @app.callback(
        [Output('sample-graph', 'figure'),
         Output('subject-chart', 'figure')],
        [Input('student-dropdown', 'value'),
         Input('grade-dropdown', 'value')]
    )
    def update_charts(selected_student, selected_grade):
        sample_fig = graphs.create_sample_graph(df, selected_student, selected_grade)
        subject_fig = graphs.create_subject_chart(df, selected_student, selected_grade)
        return sample_fig, subject_fig
