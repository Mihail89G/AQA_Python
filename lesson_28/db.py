from sqlalchemy import create_engine

def get_engine():

    url = "mssql+pyodbc://sa:YourStrong!Passw0rd@mssql:1433/test_db?driver=ODBC+Driver+17+for+SQL+Server"
    return create_engine(url, echo=True)