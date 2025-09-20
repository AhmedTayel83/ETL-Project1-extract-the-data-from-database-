import pandas as pd

def transform_data(df):

    text_cols = ['FirstName', 'MiddleName', 'LastName', 'Address', 'Gender']
    
    for col in text_cols:
        df[col] = df[col].fillna('Unknown')
        df[col] = df[col].str.title()

    df = df.rename(columns = {
        'St_ID' : 'StudentID',
        'FirstName' : 'First_Name',
        'MiddleName' : 'Middle_Name',
        'LastName' : 'Last_Name',
        'DateOfBirth' : 'DOB',
        'Address': 'Address',
        'Gender' : 'Gender',
        'Supervisor_ID' : 'SupervisorID'
    })

    df['SupervisorID'] = df['SupervisorID'].fillna(0).astype(int)

    df['DOB'] = pd.to_datetime(df['DOB'], errors = 'coerce').dt.date

    today = pd.Timestamp.today()

    df['Age'] = df['DOB'].apply(lambda x: today.year - x.year if pd.notnull(x) else None)

    return df

if __name__ == "__main__":
    from extract_data import extract_data

    df_raw = extract_data()
    df_transformed = transform_data(df_raw)

    print("Data after transform and cleaning: ")
    print(df_transformed.head())

