import dash
import dash_bootstrap_components as dbc
from layouts import main_layout
from callbacks import main_callbacks
import pandas as pd

# Initialize the Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Read data from Excel file
df = pd.read_excel('data.xlsx')

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

# Prepare the summary table with only final grades
summary_df = df[
    ["Name", "Year"] + subjects + ["Grade Average"]
]

# Set the app layout
app.layout = main_layout.create_layout(summary_df)

# Register callbacks
main_callbacks.register_callbacks(app, summary_df)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
