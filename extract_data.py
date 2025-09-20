import os
import pyodbc
import pandas as pd
from dotenv import load_dotenv

def extract_data():
    
    load_dotenv()
    server = os.getenv("SQL_SERVER")
    database = os.getenv("SQL_DATABASE")

    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
    )
        
    with pyodbc.connect(conn_str) as conn:
        print("✅ Connected!")

        query = "SELECT St_ID, FirstName, MiddleName, LastName, DateOfBirth, Address, Gender, Supervisor_ID FROM Student"
        df = pd.read_sql(query, conn)

        return df
