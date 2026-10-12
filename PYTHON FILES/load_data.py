import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
air = pd.read_csv("air_quality.csv")
stations = pd.read_csv("stations.csv")
weather = pd.read_csv("weather.csv")
traffic = pd.read_csv("traffic.csv")
calendar = pd.read_csv("calendar.csv")

datasets = {
    "Air Quality": air,
    "Stations": stations,
    "Weather": weather,
    "Traffic": traffic,
    "Calendar": calendar
}

# Inspect each dataset
for name, df in datasets.items():
    print("\n" + "=" * 50)
    print(f"DATASET: {name}")
    print("=" * 50)

    print("Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nData types:\n", df.dtypes)
    print("\nFirst five rows:\n", df.head())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())

#Statistics
print("\nAIR QUALITY DESCRIPTIVE STATISTICS")
print(air.describe())
