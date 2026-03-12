import pandas as pd
import sqlite3
import os

def load_data_to_sqlite():
    csv_path = 'data/hotel_bookings.csv'
    db_path = 'data/hotel_database.db'

    if not os.path.exists(csv_path):
        print("Error: I can't find the CSV file at the specified path. Please check the path and try again.")   
        return

    df = pd.read_csv(csv_path)
    print(f"Data loaded successfully from {csv_path}. Here's a preview:")
    print(df.head())

    conn = sqlite3.connect(db_path)
    
    df.to_sql('bookings_raw', conn, if_exists='replace', index=False)
    
    conn.close()
    print(f"Success! The data is now in {db_path} inside the 'bookings_raw' table.")

if __name__ == "__main__":
    load_data_to_sqlite()