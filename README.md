# Interactive Sales Dashboard for Store Franchise

This project consists of an **Interactive Sales Dashboard**, developed to provide management with an intuitive, visually impactful, and highly functional tool for **data analysis, monitoring KPIs and metrics**, and assisting in **strategic decision-making**.

## Objectives

- Provide a **clear and dynamic visualization** of sales data.
- Facilitate the **monitoring of key performance indicators (KPIs)**.
- Allow **detailed analysis by region, product category, salesperson, and time period**.
- Offer an interface for **exploration and download of raw data**.

## Technologies and Frameworks Used

- **Python** — main programming language.
- **Streamlit** — for building the interactive web interface.
- **Pandas** — for data manipulation and processing.
- **Plotly Express** — for generating interactive and visually impactful charts.
- **Requests** — for retrieving data via API.
- **NumPy** — supports numerical processing.

## Project Structure

The project was carefully modularized to promote **organization, code reusability, and scalability**:

- `app.py` — Main file responsible for the interface, filters, chart display, and metrics.
- `load_data.py` — Module for **loading data from a public API**.
- `preprocessing.py` — Responsible for **processing and generating analytical tables**.
- `visualizations.py` — Functions for creating **interactive charts** with Plotly.
- `utils.py` — Utilities such as a function to **format monetary values**.
- `pages/Dados_brutos.py` — Page dedicated to **exploring and downloading raw data**, with multiple customizable filters.

## Features

✅ Interactive filters by region, year, and salesperson.  
✅ Revenue and sales quantity charts by state, month, and product category.  
✅ Geographical maps for spatial visualization of sales and revenue.  
✅ **Top salesperson** analysis, by revenue and sales volume.  
✅ Raw data download with customizable filters and **CSV export**.  
✅ Clear modularization that facilitates **system maintenance and expansion**.

## How to Run

1. Clone the repository.
2. Install the dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
  ```bash
  streamlit run app.py
  ```

## Requirements

- Python 3.10+
- Plotly 6.0.1
- Pandas 2.2.3
- Numpy 2.2.5
- Requests 2.32.3

## Highlights

- Intuitive and responsive design with a tabbed and column-based layout.
- Use of multiple Streamlit pages to separate sales analysis and raw data.
- Interactive charts that support rich exploratory analysis.
- Clean code architecture and modular design.

## Data

The data used in this project is automatically retrieved from a public product API:  
[https://labdados.com/produtos](https://labdados.com/produtos)

## Expected Results

This dashboard provides a strategic and detailed view of the franchise's sales operations, offering valuable insights for decisions related to marketing, inventory, regional performance, and business goals.
