# Python Retail Sales Analysis

A portfolio project using **Python, pandas, and matplotlib** to clean, analyze, and visualize a synthetic retail sales dataset.

## Project Goal

The goal of this project is to demonstrate how Python can be used to turn transactional sales data into practical business insights.

The analysis answers questions such as:

- How much revenue and profit did the business generate?
- Which months performed best?
- Which product categories drove the most revenue?
- Which products performed strongest?
- Which regions generated the most sales?
- What does repeat-customer behavior look like?
- What business actions could be taken from these findings?

## Skills Demonstrated

- Python
- pandas
- Data cleaning
- Missing-value handling
- Data validation
- Grouping and aggregation
- Calculated business metrics
- Customer analysis
- Product and regional analysis
- matplotlib visualization
- Business interpretation

## Repository Structure

```text
python-retail-sales-analysis/
├── README.md
├── retail_sales.csv
├── analysis.ipynb
├── analysis.py
├── requirements.txt
└── charts/
    ├── monthly_revenue.png
    ├── category_revenue.png
    └── regional_revenue.png
```

## Dataset

The included dataset is **synthetic and created specifically for this portfolio project**. It contains 650 retail transactions from 2025 with fields for:

- order ID and date
- customer ID
- region
- product category
- product
- quantity
- unit price
- unit cost
- discount percentage
- revenue
- cost
- profit
- profit margin

A small number of missing values are intentionally included so the project demonstrates basic data-cleaning steps.

## Key Findings

Using the included synthetic dataset:

- **Total revenue:** $56,764.22
- **Total profit:** $28,122.22
- **Overall profit margin:** 49.5%
- **Average order value:** $87.33
- **Highest-revenue month:** 2025-11 ($6,535.76)
- **Top revenue category:** Electronics ($29,241.63)
- **Top region:** South ($18,552.51)
- **Top product:** Smart Watch ($12,277.51)
- **Repeat customer rate:** 80.3%

## Business Recommendations

1. Focus inventory and marketing on the strongest product categories and best-performing products.
2. Use monthly revenue patterns to plan promotions and staffing ahead of demand peaks.
3. Study the strongest region and test whether its performance drivers can be replicated elsewhere.
4. Build retention campaigns around repeat customers and high-value buyers.
5. Track discount levels alongside profit margin to protect profitability.

## How to Run

### Option 1: Jupyter Notebook

Open:

```text
analysis.ipynb
```

and run the cells in order.

### Option 2: Python Script

Install dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python analysis.py
```

## Portfolio Context

This project was built specifically as a student portfolio project to demonstrate foundational Python analytics skills. The dataset is simulated and does not represent a real company or customer base.

## Author

**Myiah Roseman**  
Computer Information Systems  
Georgia State University
