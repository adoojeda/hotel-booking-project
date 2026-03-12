-- ==========================================================
-- PROJECT: Data Analysis for Hotel Bookings
-- PURPOSE: Queries to analyze booking patterns, cancellation rates, and revenue impacts.
-- ==========================================================

-- 1. Analysis of Lost Revenue by Cancellation
-- Helps understand the direct financial impact.
SELECT 
    hotel,
    is_canceled,
    COUNT(*) as total_bookings,
    ROUND(SUM(adr * total_nights), 2) as estimated_revenue
FROM bookings_analytics
GROUP BY 1, 2;

-- 2. Cancellation Rate by Lead Time
-- Is there a correlation between how early bookings are made and the likelihood of cancellation?
SELECT 
    CASE 
        WHEN lead_time < 7 THEN 'Last Minute'
        WHEN lead_time BETWEEN 7 AND 30 THEN 'Short Term'
        WHEN lead_time BETWEEN 31 AND 90 THEN 'Medium Term'
        ELSE 'Long Term'
    END as booking_window,
    AVG(is_canceled) * 100 as cancellation_rate
FROM bookings_analytics
GROUP BY 1
ORDER BY cancellation_rate DESC;

-- 3. Top 5 Countries with Highest Average Daily Rate (Confirmed Bookings Only)
-- Identify high-value markets.
SELECT 
    country,
    COUNT(*) as total_bookings,
    ROUND(AVG(adr), 2) as avg_daily_rate
FROM bookings_analytics
WHERE is_canceled = 0
GROUP BY country
HAVING total_bookings > 100
ORDER BY avg_daily_rate DESC
LIMIT 5;