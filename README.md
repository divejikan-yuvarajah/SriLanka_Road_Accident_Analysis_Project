# Sri Lanka Road Accident Data Analysis

This project analyzes road accident data in Sri Lanka to uncover key insights into when, where, and how accidents happen. The goal is to better understand the impact of time, weather, location, and vehicle types on accident patterns and severity.

## 📊 Project Overview

Using a dataset of road accidents across Sri Lanka, this Python project performs:

- Data cleaning and feature extraction
- Visual exploration using bar charts, pie charts, histograms, and heatmaps
- District-wise, time-wise, and weather-based accident insights
- Severity and fatality trend analysis
- Optional insights based on available columns like `location`, `vehicle_type`, and `date`

## 🛠️ Technologies Used

- **Python**
- **Pandas** for data manipulation
- **Matplotlib** & **Seaborn** for data visualization
- **MySQL

## 📁 Dataset

- Assumed dataset: `road_accidents_srilanka.csv`
- Columns used: `district`, `time`, `date`, `fatalities`, `injuries`, `severity`, `weather`, `location`, `vehicle_type`

> Note: Code dynamically adjusts based on available columns.

## 📈 Key Analysis & Visualizations

1. **District-wise Accident Count**
2. **Hourly Distribution of Accidents**
3. **Weather Condition vs Accidents**
4. **Severity-wise Fatalities and Injuries**
5. **Top 10 Accident-Prone Locations** *(if available)*
6. **Accidents by Day of the Week**
7. **Vehicle Type Involvement**
8. **Correlation Heatmap of Numerical Features**
9. **Pie Chart of Accident Severity**
10. **Fatal vs Non-Fatal by District**

All graphs are automatically saved as `.png` files in the project directory.

## 📷 Sample Outputs

| Graph                          | Description                            |
|-------------------------------|----------------------------------------|
| `District_Accidents.png`       | Number of accidents per district       |
| `Hourly_Accidents.png`         | Accidents across hours of the day      |
| `Weather_Accidents.png`        | Weather conditions and accident frequency |
| `Fatal_vs_Nonfatal_District.png` | Comparison of fatal vs non-fatal incidents |

## 🚀 How to Run

```bash
pip install pandas matplotlib seaborn
python analysis_script.py
