# 🌦️ Weather Data Visualizer  
A mini project for the course **Programming for Problem Solving using Python**, focused on analyzing, processing, and visualizing real-world weather data using **Pandas, NumPy, and Matplotlib**.

---

## 📌 Project Overview  
This project loads a real weather dataset, cleans and preprocesses it, performs statistical and seasonal analysis, and generates multiple visualizations.  
It also exports a cleaned dataset and produces a final summary report describing trends and insights.

The project demonstrates practical skills in:
- Data acquisition  
- Data cleaning & preprocessing  
- Statistical analysis  
- Visualization  
- Grouping and aggregation  
- Storytelling with data  

---

## 📂 Folder Structure  

weather-data-visualizer-yourname
│
├── data/
│ ├── raw_weather.csv
│ └── cleaned_weather.csv
│
├── images/
│ ├── daily_temperature.png
│ ├── monthly_rainfall.png
│ ├── humidity_vs_temp.png
│ └── combined_plots.png
│
├── src/
│ └── weather_visualizer.py
│
├── reports/
│ └── summary.md
│
└── README.md

yaml
Copy code

---

## 🗂️ Dataset Description  

The dataset contains real weather observations, downloaded from **Kaggle/IMD/NOAA**.  
It includes the following important columns:

| Column        | Description |
|---------------|-------------|
| `date`        | Date of weather observation |
| `temperature` | Daily temperature (°C) |
| `rainfall`    | Rainfall amount (mm) |
| `humidity`    | Relative humidity (%) |

After processing, missing values are handled, dates are converted to proper format, and unnecessary columns are removed.

---

## 🧹 Task 1 & 2: Data Loading & Cleaning  
- Loaded CSV using Pandas  
- Checked head, info, describe  
- Converted `date` to datetime format  
- Filled numerical missing values with mean  
- Selected required columns only  
- Exported cleaned dataset to `cleaned_weather.csv`

---

## 📊 Task 3: Statistical Analysis  
Using **NumPy & Pandas**, the following were calculated:

- Mean, Min, Max, STD of temperature  
- Monthly averages  
- Monthly rainfall totals  
- Seasonal statistics (Winter, Summer, Monsoon, Autumn)

---

## 📈 Task 4: Visualization  

The following PNG charts were generated and saved inside `/images`:

1. **Daily Temperature Trend** (Line chart)  
2. **Monthly Rainfall Totals** (Bar chart)  
3. **Humidity vs Temperature** (Scatter plot)  
4. **Combined Temperature & Rainfall Subplot**

All plots were created using **Matplotlib**.

---

## 📅 Task 5: Grouping & Aggregation  
Grouping performed using:
- `groupby('month')`  
- `groupby('season')`  

Aggregated values include:
- Monthly & seasonal mean temperature  
- Monthly rainfall totals  
- Seasonal rainfall totals  

---

## 📤 Task 6: Exporting & Storytelling  
Exports created:
- Cleaned dataset → `/data/cleaned_weather.csv`
- Plots → `/images/*.png`
- Summary interpretation report → `/reports/summary.md`

The summary report includes:
- Key statistical findings  
- Seasonal patterns  
- Visual insights  
- Observed anomalies  

---

## 🛠️ Technologies Used  
- **Python**  
- **Pandas**  
- **NumPy**  
- **Matplotlib**  
- **Jupyter Notebook** (optional)  
- Git & GitHub  

---

## ▶️ How to Run the Project  

1. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib
Run the script:

bash
Copy code
cd src
python weather_visualizer.py
View outputs in:

/images → all charts

/data → cleaned CSV

/reports → summary report

📘 Academic Details
Course: Programming for Problem Solving using Python
Assignment Title: Weather Data Visualizer
Type: Mini Project
Weightage: 5 Marks

✍️ Author
HARSH
B.Tech CSE — Year/Sem
K.R. Mangalam University

📎 License
This project is for educational purposes only.
Dataset belongs to its respective owner (Kaggle/IMD/NOAA).

yaml
Copy code

---

If you want, I can also give you:

✅ **summary.md (full report)**  
✅ **Python code as separate tasks**  
✅ **Jupyter Notebook file**  
Just tell me!
