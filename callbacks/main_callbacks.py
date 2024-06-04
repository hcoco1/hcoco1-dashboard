from dash.dependencies import Input, Output
import plotly.express as px
import components.graphs as graphs

def register_callbacks(app, df):
    @app.callback(
        Output('grade-dropdown', 'options'),
        [Input('student-dropdown', 'value')]
    )
    def update_grades_dropdown(selected_student):
        if selected_student is None:
            return []
        filtered_df = df[df['Name'] == selected_student]
        grades = filtered_df['Year'].unique()
        return [{'label': grade, 'value': grade} for grade in grades]

    @app.callback(
        [Output('student-image', 'src'),
        
         
         Output('final-average', 'children')],
        [Input('student-dropdown', 'value')]
    )
    def update_student_info(selected_student):
        if selected_student is None:
            return 'https://via.placeholder.com/300', '', "Average Grade: N/A", "Final Average: N/A"
        filtered_df = df[df['Name'] == selected_student]
        if not filtered_df.empty:
            image_url = filtered_df['Image URL'].values[0] if 'Image URL' in filtered_df.columns else 'https://via.placeholder.com/300'
            
            
            final_average = f"Final Average: {filtered_df['Final Average'].values[0]}"
            return image_url, final_average
        return 'https://via.placeholder.com/300', selected_student, "Average Grade: N/A", "Final Average: N/A"

    @app.callback(
        Output('summary-table', 'data'),
        [Input('student-dropdown', 'value'),
         Input('grade-dropdown', 'value')]
    )
    def update_summary_table(selected_student, selected_grade):
        if selected_student is None or selected_grade is None:
            return []
        filtered_df = df[(df['Name'] == selected_student) & (df['Year'] == selected_grade)]
        print(f"Filtered Data for Summary Table: {filtered_df}")  # Debug statement
        return filtered_df.to_dict('records')

    @app.callback(
        Output('sample-graph', 'figure'),
        [Input('student-dropdown', 'value'),
         Input('grade-dropdown', 'value')]
    )
    def update_sample_graph(selected_student, selected_grade):
        if selected_student is None or selected_grade is None:
            return px.bar(title='Select a student and grade')
        return graphs.create_sample_graph(df, selected_student, selected_grade)

    @app.callback(
        [Output('exam-results-table', 'columns'),
         Output('exam-results-table', 'data'),
         Output('exam-results-chart', 'figure')],
        [Input('student-dropdown', 'value'),
         Input('grade-dropdown', 'value'),
         Input('subject-dropdown', 'value')]
    )
    def update_exam_results(selected_student, selected_grade, selected_subject):
        if selected_student is None or selected_grade is None or selected_subject is None:
            return [], [], px.line(title='Please select all dropdowns.')

        filtered_df = df[(df['Name'] == selected_student) & (df['Year'] == selected_grade)]
        if filtered_df.empty:
            return [], [], px.line(title=f'No data for {selected_student} in Grade {selected_grade} for {selected_subject}')

        exam_columns = [f"{selected_subject} Exam 1", f"{selected_subject} Exam 2", f"{selected_subject} Exam 3"]
        exam_data = filtered_df[exam_columns].to_dict('records')
        exam_columns_formatted = [{"name": col, "id": col} for col in exam_columns]

        # Add Name and Year to each exam result record
        for record in exam_data:
            record['Name'] = selected_student
            record['Year'] = selected_grade

        subject_chart = graphs.create_exam_results_chart(df, selected_student, selected_grade, selected_subject)
        return exam_columns_formatted, exam_data, subject_chart
