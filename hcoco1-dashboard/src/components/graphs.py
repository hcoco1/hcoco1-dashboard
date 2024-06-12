import plotly.express as px

def create_sample_graph(df, selected_student, selected_grade):
    # Filter the DataFrame based on the selected student and grade
    filtered_df = df[(df['Name'] == selected_student) & (df['Year'] == selected_grade)]
    
    # Calculate the average grade for each subject
    subject_columns = ['Matematicas', 'Literatura', 'English', 'Deporte', 'Geography', 'Art', 'Biologia', 'Orientacion', 'Participacion']
    averages = filtered_df[subject_columns].mean().reset_index()
    averages.columns = ['Subject', 'Average Grade']
    
    # Create the bar chart with different colors for each bar
    fig = px.bar(
        averages, 
        x='Subject', 
        y='Average Grade', 
        title=f'Average Grade per Subject for {selected_student} in Grade {selected_grade}',
        color='Subject',
        color_discrete_sequence=px.colors.qualitative.Plotly  # You can choose a different color sequence if you prefer
    )
    return fig



import plotly.graph_objects as go

def create_exam_results_chart(df, selected_student, selected_grade, selected_subject):
    filtered_df = df[(df['Name'] == selected_student) & (df['Year'] == selected_grade)]
    
    if filtered_df.empty or selected_subject is None:
        return go.Figure().update_layout(title=f'No data for {selected_student} in Grade {selected_grade} for {selected_subject}')
    
    exam_columns = [f"{selected_subject} Exam 1", f"{selected_subject} Exam 2", f"{selected_subject} Exam 3"]
    exam_results = filtered_df[exam_columns].melt(var_name='Exam', value_name='Score')
    
    # Create the line chart
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=exam_results['Exam'],
            y=exam_results['Score'],
            mode='lines+markers',
            line_shape='spline',
            line=dict(color='royalblue', width=4),
            marker=dict(size=10, color='red', symbol='circle')
        )
    )
    
    # Add a horizontal line at y=10
    fig.add_shape(
        type='line',
        x0=0,
        y0=10,
        x1=1,
        y1=10,
        xref='paper',  # Use 'paper' reference to make the line span the entire plot width
        yref='y',
        line=dict(color='red', width=1, dash='dash')
    )
    
    fig.add_shape(
        type='line',
        x0=0,
        y0=15,
        x1=1,
        y1=15,
        xref='paper',  # Use 'paper' reference to make the line span the entire plot width
        yref='y',
        line=dict(color='cyan', width=1, dash='dash')
    )
    fig.add_shape(
        type='line',
        x0=0,
        y0=18,
        x1=1,
        y1=18,
        xref='paper',  # Use 'paper' reference to make the line span the entire plot width
        yref='y',
        line=dict(color='green', width=1, dash='dash')
    )
    
    # Customize layout
    fig.update_layout(
        title={
            'text': f'{selected_subject} Exam Results for {selected_student} Over Time',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title='Exam',
        yaxis_title='Score',
        template='plotly_white',
        xaxis=dict(
            tickmode='array',
            tickvals=['Exam 1', 'Exam 2', 'Exam 3']
        )
    )
    
    return fig



