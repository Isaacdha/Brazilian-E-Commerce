<div align="center">

# Brazilian E-Commerce Data Analysis Platform 🛍️

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://brazilian-ecommerce-idha.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*An advanced analytics platform for exploring Brazilian e-commerce trends and insights*

[Live Dashboard](https://brazilian-ecommerce-idha.streamlit.app/) | [Documentation](#documentation) | [Getting Started](#getting-started) | [Contributing](#contributing)

</div>

---

## 📊 Overview

The Brazilian E-Commerce Data Analysis Platform provides comprehensive analytics and visualization tools for examining public e-commerce data from Brazil. This project combines robust data processing with interactive visualizations to deliver actionable business insights.

### Key Features
- 📈 Interactive data visualization dashboard
- 🔍 Advanced exploratory data analysis (EDA)
- 💼 Business intelligence metrics
- 🔄 Real-time data processing
- 📱 Mobile-responsive design

## 📚 Documentation

### Data Sources
The analysis is powered by the [Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), provided in partnership with [Dicoding](https://www.dicoding.com/).

### Repository Structure
```
brazilian-e-commerce/
├── Dashboard/
│   ├── ecommerce-dashboard.py     # Main dashboard application
│   ├── .streamlit/               # Local dashboard configuration
│   └── Data/                     # Local data files
├── Data/                         # Cloud deployment data
├── .streamlit/                   # Cloud configuration files
├── notebooks/
│   ├── E-Commerce Public Dataset Analysis.ipynb
│   └── E-Commerce Public Dataset Analysis _ID.ipynb
├── requirements.txt
├── url.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/Isaacdha/Brazilian-E-Commerce.git
```
   or download directly:
```bash
wget https://github.com/Isaacdha/Brazilian-E-Commerce/archive/refs/heads/main.zip
```

2. **Navigate to Project Directory**
```bash
cd Brazilian-E-Commerce
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Interactive Dashboard
Launch the Streamlit dashboard locally:
```bash
cd Dashboard
streamlit run ecommerce-dashboard.py
```
Access the dashboard at `http://localhost:8501`

### Jupyter Notebooks
Two comprehensive notebooks are provided:
- `E-Commerce Public Dataset Analysis.ipynb` (English)
- `E-Commerce Public Dataset Analysis _ID.ipynb` (Indonesian)

These notebooks contain:
- Data wrangling procedures
- Exploratory data analysis
- Business insights
- Visualization examples

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Kaggle](https://www.kaggle.com/) for providing the dataset
- [Dicoding](https://www.dicoding.com/) for educational support
- [Streamlit](https://streamlit.io/) for the visualization framework

---

<div align="center">

Made with ❤️ by [Isaacdha](https://github.com/Isaacdha)

</div>
