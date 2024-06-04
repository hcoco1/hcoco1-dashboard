import dash
import dash_bootstrap_components as dbc
from layouts import main_layout
from callbacks import main_callbacks
import pandas as pd

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Read data from Excel file
df = pd.read_excel('data.xlsx')
#df = pd.read_excel('https://raw.githubusercontent.com/hcoco1/dashboards-data/9da8e1be15f92c55dc9e9805be8caf955f938f1b/data.xlsx')


# Ensure grades are numeric
for col in df.columns[3:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Calculate final grades by averaging sublevels
subjects = [
    "Matematicas",
    "Literatura",
    "English",
    "Deporte",
    "Geography",
    "Art",
    "Biologia",
    "Orientacion",
    "Participacion",
]
for subject in subjects:
    df[subject] = (
        df[[f"{subject} Exam 1", f"{subject} Exam 2", f"{subject} Exam 3"]]
        .mean(axis=1)
        .round(0)
    )

# Calculate the final grade average across all subjects
df["Grade Average"] = df[subjects].mean(axis=1).round(0)

# Calculate the final average across all years for each student
final_averages = df.groupby('Name')[['Grade Average']].mean().round(2).reset_index()
final_averages.columns = ['Name', 'Final Average']

# Merge final averages back into the main dataframe
df = pd.merge(df, final_averages, on='Name')

# Check if 'Image URL' column exists, if not, add a placeholder
if 'Image URL' not in df.columns:
    df['Image URL'] = 'https://via.placeholder.com/300'

# Prepare the summary table with only final grades
summary_df = df[
    ["Name", "Year", "Image URL"] + subjects + ["Grade Average"]
]

# Set the app layout
app.layout = main_layout.create_layout(summary_df)

# Register callbacks
main_callbacks.register_callbacks(app, df)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
