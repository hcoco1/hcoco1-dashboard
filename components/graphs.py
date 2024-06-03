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

def create_subject_chart(df, selected_student, selected_grade):
    # Filter the DataFrame based on the selected student and grade
    filtered_df = df[(df['Name'] == selected_student) & (df['Year'] == selected_grade)]
    
    # Calculate the average grade for each subject
    subject_columns = ['Matematicas', 'Literatura', 'English', 'Deporte', 'Geography', 'Art', 'Biologia', 'Orientacion', 'Participacion']
    averages = filtered_df[subject_columns].mean().reset_index()
    averages.columns = ['Subject', 'Average Grade']
    
    # Create the bar chart
    fig = px.bar(averages, x='Subject', y='Average Grade', title=f'Average Grade per Subject for {selected_student} in Grade {selected_grade}')
    return fig
