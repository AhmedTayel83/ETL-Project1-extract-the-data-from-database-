import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from extract_data import extract_data
from transform_data import transform_data

df_raw = extract_data()
df = transform_data(df_raw)

load_dotenv()
server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")

connection_string = f"mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
engine = create_engine(connection_string)

table_name = "Student_Cleaned"

df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)

print(f"Data loaded successfully into table: {table_name}")