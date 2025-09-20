#📌 Student Data ETL Pipeline & Visualization Dashboard

##📝 Project Overview

This project demonstrates the design and implementation of a complete ETL (Extract, Transform, Load) pipeline for student data using Python and SQL Server. The pipeline extracts raw data from a database, applies thorough cleaning and transformation, reloads the structured dataset into a new database table, and visualizes meaningful insights through a dashboard built with Matplotlib and Seaborn.

The project was developed as part of the Digital Egypt Pioneers Initiative (DEPI), under the supervision of Abdullah Mahmoud.


---

##⚙ Key Features

🔹 Extract

Connected securely to SQL Server using pyodbc.

Pulled student records including personal details, demographics, and supervisor information.

Used environment variables (.env) for secure credential management.


🔹 Transform & Clean

Replaced missing values (Nulls) with defaults or placeholders.

Standardized text fields (names, addresses, gender) for consistency.

Converted Supervisor_ID into integers with proper handling of missing references.

Transformed DOB into valid DATE format (YYYY-MM-DD).

Calculated student age dynamically from DOB.

Renamed columns for readability and analysis.


🔹 Load

Stored the transformed dataset into a new table Student_Cleaned in SQL Server.

Implemented loading via SQLAlchemy for reliability and scalability.


🔹 Visualization Dashboard

An interactive dashboard was created in Jupyter Notebook using Matplotlib and Seaborn to explore insights such as:

📊 Histogram: Age distribution of students.

🥧 Pie Chart: Gender distribution.

🏙 Bar Chart: Students per city.

📦 Box Plot: Outlier detection in age.

🔥 Heatmap: Correlation analysis between attributes.

✨ Scatter & Line Plots: Trends and patterns over data points.


Custom gradient color palettes 🎨 were applied to deliver a visually appealing and professional look.


---

##📈 Results

A clean, structured, and analysis-ready dataset stored in SQL Server.

A reusable and automated ETL pipeline.

A visualization dashboard providing clear and actionable insights into the student data.



---

##🚀 Tech Stack

Python: pandas, pyodbc, SQLAlchemy, matplotlib, seaborn

Database: Microsoft SQL Server

Tools: Jupyter Notebook, VS Code

Version Control: Git & GitHub



---

##📂 Project Structure

├── extract_data.py        # Extract student data from SQL Server
├── transform_data.py      # Clean and transform raw data
├── load_data.py           # Load cleaned data back into SQL Server
├── dashboard.ipynb        # Visualization dashboard
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation


---

🔗 Repository

The full project and code are available here on GitHub
