

# Brazilian E-Commerce Data Analysis

![Brazilian E-Commerce Data Dashboard](dashboard.gif)

[Explore the Brazilian E-Commerce Data Dashboard on Streamlit](https://brazilian-ecommerce-idha.streamlit.app/)

## Table of Contents
- [Overview](#overview)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)

## Overview
This project focuses on analyzing and visualizing public data from Brazilian e-commerce. It includes scripts for data wrangling, exploratory data analysis (EDA), answering business questions, and a Streamlit dashboard deployment for interactive data exploration. The goal is to derive insights from Brazilian E-Commerce Public Dataset.

## Data Sources
The project utilizes the E-Commerce Public Dataset from the [Brazilian E-Commerce Public Data](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and was used in course offered by [Dicoding](https://www.dicoding.com/).

## Project Structure
- `dashboard/`: Contains `ecommerce-dashboard.py`, which generates the data analysis dashboards.\
   -- '.streamlit/' 
- `data/`: Holds the raw CSV data files from the source
- `E-Commerce Public Dataset Analysis.ipynb`: Jupyter notebook for performing data task such as wrangling, exploration, analysis, and question answering.
- `E-Commerce Public Dataset Analysis _ID.ipynb`: Indonesian version of `notebook.ipynb`.
- `README.md`: This documentation file.

## Installation
1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/mhdhfzz/data-analyst-dicoding.git
    ```
2. Navigate to the project directory:
    ```sh
    cd data-analyst-dicoding
    ```
3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. **Data Wrangling**: Use the `notebook.ipynb` file to clean and prepare the data.
2. **Exploratory Data Analysis (EDA)**: Analyze the data using the provided scripts to uncover patterns in the e-commerce dataset.
3. **Visualization**: Launch the Streamlit dashboard for interactive data exploration:
    ```sh
    cd data-analyst-dicoding/dashboard
    streamlit run dashboard.py
    ```
    Access the dashboard in your web browser at `http://localhost:8501`.


