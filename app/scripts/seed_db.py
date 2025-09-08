import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

def seed_database():
    """
    Connects to the Postgres database, reads the raw retail data from an Excel file,
    and loads it into a new table called 'raw_orders'.
    """
    load_dotenv()
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_URL environment variable is not set.")

    print("Connecting to the database...")
    engine = create_engine(database_url)
    print("Connection successful.")

    # Define the path to our data file
    # **Note: The file extension is now .xlsx**
    excel_path = os.path.join("app", "data", "online_retail_II.xlsx")

    print(f"Reading data from {excel_path}...")
    try:
        # **Change: Use read_excel instead of read_csv**
        # The data is in the first sheet, which is the default.
        df = pd.read_excel(excel_path)
        print(f"Successfully read {len(df)} rows from Excel file.")
    except FileNotFoundError:
        print(f"Error: The file was not found at {excel_path}")
        return

    # Load the data into a SQL table named 'raw_orders'
    print("Loading data into 'raw_orders' table... This may take several minutes from Excel.")
    df.to_sql(
        'raw_orders',
        con=engine,
        if_exists='replace',
        index=False
    )
    print("Data loading complete. 'raw_orders' table created.")

if __name__ == "__main__":
    seed_database()