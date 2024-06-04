import plotly.express as px

def create_sample_graph(df, selected_student, selected_grade):
    # Filter the DataFrame based on the selected student and grade
    filtered_df = df[(df['Name'] == selected_student) & (df['Year'] == selected_grade)]
    
    # Calculate the average grade for each subject
    subject_columns = ['Matematicas', 'Literatura', 'English', 'Deporte', 'Geography', 'Art', 'Biologia', 'Orientacion', 'Participacion']
    averages = filtered_df[subject_columns].mean().reset_index()
    averages.columns = ['Subject', 'Average Grade']
    
    # Create the bar chart
    fig = px.bar(averages, x='Subject', y='Average Grade', title=f'Average Grade per Subject for {selected_student} in Grade {selected_grade}')
    return fig

def create_exam_results_chart(df, selected_student, selected_grade, selected_subject):
    filtered_df = df[(df['Name'] == selected_student) & (df['Year'] == selected_grade)]
    if filtered_df.empty or selected_subject is None:
        return px.line(title=f'No data for {selected_student} in Grade {selected_grade} for {selected_subject}')
    
    exam_columns = [f"{selected_subject} Exam 1", f"{selected_subject} Exam 2", f"{selected_subject} Exam 3"]
    exam_results = filtered_df[exam_columns].melt(var_name='Exam', value_name='Score')
    
    fig = px.line(exam_results, x='Exam', y='Score', title=f'{selected_subject} Exam Results for {selected_student} Over Time')
    return fig

