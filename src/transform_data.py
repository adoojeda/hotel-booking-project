import sqlite3
import pandas as pd
import numpy as np

def transform_data():
    db_path = 'data/hotel_database.db'
    conn = sqlite3.connect(db_path)
    
    print("--- Initiating Data Transformation Process ---")
    
    df = pd.read_sql('SELECT * FROM bookings_raw', conn)
    total_original = len(df)
    
    df['children'] = df['children'].fillna(0).astype(int)
    mask_ghost = (df['adults'] + df['children'] + df['babies']) > 0
    df = df[mask_ghost]
    rows_ghost = total_original - len(df)

    month_map = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    df['arrival_date_month_num'] = df['arrival_date_month'].map(month_map)
    
    df['arrival_date'] = pd.to_datetime(
        df['arrival_date_year'].astype(str) + '-' + 
        df['arrival_date_month_num'].astype(str).str.zfill(2) + '-' + 
        df['arrival_date_day_of_month'].astype(str).str.zfill(2)
    )

    df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
    
    df['is_family'] = np.where((df['children'] > 0) | (df['babies'] > 0), 1, 0)
    
    df = df[df['adr'] > 0]
    rows_adr_issues = (total_original - rows_ghost) - len(df)

    df.to_sql('bookings_analytics', conn, if_exists='replace', index=False)
    
    print(f"\nData transformation completed. Summary:")
    print(f"   - Rows processed: {total_original}")
    print(f"   - Rows removed (0 guests): {rows_ghost}")
    print(f"   - Rows removed (Invalid ADR): {rows_adr_issues}")
    print(f"   - Final rows in 'bookings_analytics': {len(df)}")
    print(f"   - New columns created: [arrival_date, total_nights, is_family]")
    
    conn.close()

if __name__ == "__main__":
    transform_data()