<div align="center"><h1>Ivan Arias</h1></div>
<div align="center"><h2>Full-Stack Developer | Junior Penetration Tester | AWS Enthusiast</h2></div>

<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/hcoco1/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.youtube.com/channel/UCban0ilP3jBC9rdmL-fPy_Q">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  <a href="https://twitter.com/hcoco1">
    <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
  </a>
</div>  


##  Student Performance Dashboard

This project creates an interactive dashboard to visualize and analyze the grades of high school students over time. The dashboard is built using Python, Dash, and Plotly, with Bootstrap for styling.

- Username: **hcoco1**

- Password: **pythonpython**

This dashboard is designed for both English and Spanish speakers and is currently being translated.

Features

- Student Selection: Choose a student from a dropdown to view their grades.
- Year Selection: Filter grades by academic year.
- Subject Performance: View performance in different subjects.
- Grade Average: See the average grade for each student.
- Detailed Exam Scores: Examine scores for individual exams.
- Performance Over Time: Visualize performance trends across multiple exams.

---

![how this app works](https://github.com/hcoco1/hcoco1-dashboard/blob/main/dash_app.gif?raw=true) 
 
---

## Installation

Ensure you have Python 3 and `pip` installed. Follow these steps to set up your environment:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/hcoco1/hcoco1-dashboard.git
    cd hcoco1-dashboard
    ```

2. **Set up a virtual environment:**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Running the App

1. **Navigate to the source directory:**
    ```sh
    cd hcoco1-dashboard/src
    ```

2. **Run the application:**
    ```sh
    python3 app.py
    ```

3. **Access the dashboard:**
   Open your web browser and go to `http://127.0.0.1:8050/`.

## Application Structure

```sh
.
├── dash_app.gif
├── Procfile
├── README.md
├── render.yaml
├── requirements.txt
├── runtime.txt
└── src
    ├── app.py
    ├── assets
    │   └── styles.css
    ├── callbacks
    │   ├── main_callbacks.py
    │ 
    ├── components
    │   ├── dropdowns.py
    │   ├── graphs.py
    │   │── tables.py
    └── layouts
        ├── __init__.py
        ├── main_layout.py
                    
8 directories, 20 files
```
