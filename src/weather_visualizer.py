# ------------------------
# WEATHER DATA VISUALIZER
# ------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Create folders if not exist
os.makedirs("../images", exist_ok=True)
os.makedirs("../data", exist_ok=True)

# -----------------------------
# TASK 1: LOAD THE CSV DATA
# -----------------------------
df = pd.read_csv("../data/raw_weather.csv")

print("=== HEAD ===")
print(df.head(), "\n")

print("=== INFO ===")
print(df.info(), "\n")

print("=== DESCRIBE ===")
print(df.describe(), "\n")


# -----------------------------
# TASK 2: DATA CLEANING
# -----------------------------

# Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows where date failed
df = df.dropna(subset=['date'])

# Fill missing numerical values
num_cols = ['temperature', 'rainfall', 'humidity']

for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

# Keep only required columns
df = df[['date', 'temperature', 'rainfall', 'humidity']]

print("Cleaned Data:\n", df.head(), "\n")


# -----------------------------
# TASK 3: STATISTICAL ANALYSIS
# -----------------------------

daily_mean = df['temperature'].mean()
daily_max = df['temperature'].max()
daily_min = df['temperature'].min()
daily_std = df['temperature'].std()

print("Temperature Statistics:")
print("Mean:", daily_mean)
print("Max:", daily_max)
print("Min:", daily_min)
print("STD:", daily_std, "\n")


# ---- Monthly statistics ----
df['month'] = df['date'].dt.month
monthly_stats = df.groupby('month').agg({
    'temperature': ['mean', 'max', 'min'],
    'rainfall': ['sum', 'mean']
})

print("Monthly Statistics:\n")
print(monthly_stats, "\n")


# -----------------------------
# TASK 4: VISUALIZATIONS
# -----------------------------

# ---- Line chart for daily temperature ----
plt.figure(figsize=(10,5))
plt.plot(df['date'], df['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.savefig("../images/daily_temperature.png")
plt.close()

# ---- Bar chart for monthly rainfall ----
monthly_rainfall = df.groupby('month')['rainfall'].sum()

plt.figure(figsize=(10,5))
plt.bar(monthly_rainfall.index, monthly_rainfall.values)
plt.title("Monthly Rainfall Totals")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.savefig("../images/monthly_rainfall.png")
plt.close()

# ---- Scatter: humidity vs temperature ----
plt.figure(figsize=(8,5))
plt.scatter(df['temperature'], df['humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity (%)")
plt.savefig("../images/humidity_vs_temp.png")
plt.close()

# ---- Combined Plot ----
plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.plot(df['date'], df['temperature'], label="Temperature")
plt.title("Combined Temperature & Rainfall Plot")
plt.ylabel("Temperature")

plt.subplot(2,1,2)
plt.bar(monthly_rainfall.index, monthly_rainfall.values)
plt.xlabel("Month")
plt.ylabel("Rainfall")

plt.tight_layout()
plt.savefig("../images/combined_plots.png")
plt.close()


# -----------------------------
# TASK 5: GROUPING & AGGREGATION
# -----------------------------
season_map = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Summer", 4: "Summer", 5: "Summer",
    6: "Monsoon", 7: "Monsoon", 8: "Monsoon",
    9: "Autumn", 10: "Autumn", 11: "Autumn"
}

df['season'] = df['month'].map(season_map)

season_stats = df.groupby('season').agg({
    'temperature': ['mean', 'max', 'min'],
    'rainfall': ['sum']
})

print("Season Statistics:\n")
print(season_stats, "\n")


# -----------------------------
# TASK 6: EXPORT CLEANED DATA
# -----------------------------
df.to_csv("../data/cleaned_weather.csv", index=False)

print("Cleaned dataset exported ✔")
print("Plots generated ✔")
print("Analysis completed ✔")
