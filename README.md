# Product Sales Analysis System

## Overview
A complete data analysis project using MySQL and Python to analyze 5,000+ product sales records and generate business insights.

## Tech Stack
- **Database**: MySQL 8.0
- **Language**: Python 3
- **Libraries**: Pandas, Matplotlib, mysql-connector-python

## Database Design
3 normalized tables:
- `products` — 20 products across 7 categories
- `customers` — 300 customers across 4 regions
- `sales` — 5,000+ transaction records

## Key Business Insights
- Total Revenue: ₹38.81 Crore
- Average Order Value: ₹77,621
- Best Category: Electronics (dominates 80%+ of revenue)
- Best Product: Dell Laptop
- Peak Quarter: Q4 2023

## SQL Queries (20+)
- Top selling products by revenue and quantity
- Monthly and quarterly revenue trends
- Revenue by category and region
- Customer spending analysis
- Running totals using window functions
- Subqueries and JOIN operations

## Python Analysis
- Connected Python to MySQL using mysql-connector
- Loaded data into Pandas DataFrames
- Generated 4 business insight charts

## Charts Generated
| Chart | Insight |
|---|---|
| Revenue by Category | Electronics leads by huge margin |
| Monthly Revenue Trend | Consistent growth over 2 years |
| Top 10 Products | Dell Laptop is #1 |
| Revenue by Region | South region dominates |

## Files
- `insert_data.py` — generates and inserts 5000+ records
- `analysis.py` — Python analysis and chart generation
- `chart1_category_revenue.png`
- `chart2_monthly_trend.png`
- `chart3_top_products.png`
- `chart4_region_revenue.png`