import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
data = pd.read_csv("cleaned_air_quality.csv")
print("Dataset shape:", data.shape)
print("\nBasic statistics:")
print(data.describe())

# Air quality at different stations
station_aqi = data.groupby("station")["AQI"].mean()

station_aqi.plot(kind="bar")
plt.title("Average AQI at Different Stations")
plt.xlabel("Station")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Pollution during different hours
hour_aqi = data.groupby("hour")["AQI"].mean()

hour_aqi.plot(kind="line", marker="o")
plt.title("Average AQI by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Average AQI")
plt.grid()
plt.tight_layout()
plt.show()

#Traffic and AQI
plt.scatter(data["traffic_volume"], data["AQI"])
plt.title("Traffic Volume vs AQI")
plt.xlabel("Traffic Volume")
plt.ylabel("AQI")
plt.tight_layout()
plt.show()

# Rain and AQI
rain_aqi = data.groupby(
    pd.cut(data["rain"], bins=5, duplicates="drop"),
    observed=False
)["AQI"].mean()

rain_aqi.plot(kind="bar")
plt.title("Rainfall and Average AQI")
plt.xlabel("Rainfall Range")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Seasonal pollution pattern
if "season" in data.columns:
    season_aqi = data.groupby("season")["AQI"].mean()
    season_aqi.plot(kind="bar")
    plt.title("Average AQI by Season")
    plt.xlabel("Season")
    plt.ylabel("Average AQI")
    plt.tight_layout()
    plt.show()

# Correlation between numerical variables
print("\nCorrelation:")
print(data[["PM2.5", "PM10", "NO2", "AQI",
            "wind", "rain", "traffic_volume"]].corr())

sns.heatmap(
    data[["PM2.5", "PM10", "NO2", "AQI",
          "wind", "rain", "traffic_volume"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
