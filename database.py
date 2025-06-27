from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "postgresql://user:password@localhost:5432/mydb"

engine = create_engine(DATABASE_URL)

def load_table(table_name):
  return pd.read_sql(f"SELECT * FROM {table_name}", engine)

def write_table(df, table_name):
  df.to_sql(table_name, engine, if_exists='replace', index=False)
