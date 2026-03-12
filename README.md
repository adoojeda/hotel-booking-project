# Hotel Booking Business Intelligence Project

An end-to-end data engineering and analytics project that transforms raw hotel booking data into actionable business insights. This project identifies revenue leakage, cancellation patterns, and high-value geographic markets.

## Project Overview
The hospitality industry faces high volatility due to cancellations. This project builds a robust pipeline to:
1. **Ingest** raw CSV data into a structured SQLite database.
2. **Clean & Transform** data using Python (Pandas) for analytical readiness.
3. **Analyze** key business metrics using SQL and Python.
4. **Visualize** insights to drive strategic decision-making.

## Project Structure
```text
hotel-booking-project/
├── data/               # Raw and processed SQLite database
├── notebooks/          # Jupyter Notebooks with visual analysis & insights
├── sql/                # SQL scripts for business logic and KPIs
├── src/                # Python source code (ingestion & transformation)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## Tech Stack
1. **Language:** Python 3.x
2. **Database:** SQLite
3. **Libraries:** Pandas, Plotly (Visualizations), SQLAlchemy
4. **Environment:** VS Code / Jupyter Notebooks

## Key Business Insights
- **Revenue Leakage:** Identified over €10M in potential loss due to cancellations in the City Hotel segment.
- **The "Long Term" Risk:** Discovered that bookings made >90 days in advance have a 50.8% cancellation rate, suggesting a need for non-refundable policies.
- **Premium Markets:** Identified Top 5 countries with the highest ADR, providing a roadmap for targeted marketing spend.

## How to Run
1. **Clone the repository:**
```text
git clone https://github.com/adoojeda/hotel-booking-project.git
```

2. **Install dependencies:**
```text
pip install -r requirements.txt
```

3. **Run the pipeline:**
- To create the database:
```text
python src/ingest_to_db.py 
```

- To process analytics table:
```text
python src/transform_data.py (To process analytics tables)
```

4. **Explore the Analysis:** in notebooks/analysis.ipynb to view the full executive report.