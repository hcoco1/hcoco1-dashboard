from dash import Input, Output

def register_callbacks(app, df):
    @app.callback(
        Output('summary-table', 'data'),
        [Input('student-dropdown', 'value'),
         Input('grade-dropdown', 'value')]
    )
    def update_table(selected_student, selected_grade):
        # Filter data based on selections
        filtered_df = df
        if selected_student:
            filtered_df = filtered_df[filtered_df['Name'] == selected_student]
        if selected_grade:
            filtered_df = filtered_df[filtered_df['Year'] == selected_grade]

        if filtered_df.empty:
            return []

        return filtered_df.to_dict('records')
